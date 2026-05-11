"""
Rate Limiting Middleware

This module provides:
- Rate limiting based on IP address
- Configurable limits and windows
"""

import time
from collections import defaultdict

from fastapi import HTTPException, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

class RateLimitMiddleware(BaseHTTPMiddleware):
    """Middleware for rate limiting requests."""

    def __init__(self, app, requests_per_minute: int = 60):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.requests = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        # Clean old requests (older than 1 minute)
        self.requests[client_ip] = [
            req_time for req_time in self.requests[client_ip]
            if current_time - req_time < 60
        ]

        # Check rate limit
        if len(self.requests[client_ip]) >= self.requests_per_minute:
            raise HTTPException(
                status_code=429,
                detail="Too many requests. Please try again later."
            )

        # Add current request
        self.requests[client_ip].append(current_time)

        response = await call_next(request)
        return response