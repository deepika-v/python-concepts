"""
Logging Middleware

This module provides:
- Request/response logging middleware
- Correlation ID tracking
"""

import time
import uuid

import structlog
from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

logger = structlog.get_logger()

class LoggingMiddleware(BaseHTTPMiddleware):
    """Middleware for logging HTTP requests and responses."""

    async def dispatch(self, request: Request, call_next):
        # Generate correlation ID
        correlation_id = str(uuid.uuid4())
        structlog.contextvars.bind_contextvars(correlation_id=correlation_id)

        start_time = time.time()

        # Log request
        logger.info(
            "Request started",
            method=request.method,
            url=str(request.url),
            headers=dict(request.headers),
            client=request.client.host if request.client else None,
        )

        try:
            response = await call_next(request)
            process_time = time.time() - start_time

            # Log response
            logger.info(
                "Request completed",
                status_code=response.status_code,
                process_time=f"{process_time:.4f}s",
            )

            # Add correlation ID to response headers
            response.headers["X-Correlation-ID"] = correlation_id
            return response

        except Exception as exc:
            process_time = time.time() - start_time
            logger.error(
                "Request failed",
                exc_info=exc,
                process_time=f"{process_time:.4f}s",
            )
            raise