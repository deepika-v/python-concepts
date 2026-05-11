"""
Prometheus Metrics Setup

This module provides:
- HTTP request metrics
- Response time histograms
- Error counters
"""

from fastapi import FastAPI, Request, Response
from prometheus_client import Counter, Histogram, generate_latest

# Define metrics
REQUEST_COUNT = Counter(
    'http_requests_total',
    'Total number of HTTP requests',
    ['method', 'endpoint', 'status_code']
)

REQUEST_LATENCY = Histogram(
    'http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint']
)

ERROR_COUNT = Counter(
    'http_errors_total',
    'Total number of HTTP errors',
    ['method', 'endpoint', 'status_code']
)

def setup_metrics(app: FastAPI):
    """Setup Prometheus metrics for the FastAPI app."""

    @app.middleware("http")
    async def metrics_middleware(request: Request, call_next):
        start_time = REQUEST_LATENCY._timer()
        method = request.method
        endpoint = request.url.path

        try:
            response = await call_next(request)
            status_code = response.status_code

            # Record metrics
            REQUEST_COUNT.labels(method=method, endpoint=endpoint, status_code=status_code).inc()
            REQUEST_LATENCY.labels(method=method, endpoint=endpoint).observe(start_time())

            # Count errors (4xx and 5xx)
            if status_code >= 400:
                ERROR_COUNT.labels(method=method, endpoint=endpoint, status_code=status_code).inc()

            return response

        except Exception as exc:
            # Record error metrics for unhandled exceptions
            ERROR_COUNT.labels(method=method, endpoint=endpoint, status_code=500).inc()
            raise

    @app.get("/metrics")
    async def metrics():
        """Prometheus metrics endpoint."""
        return generate_latest()