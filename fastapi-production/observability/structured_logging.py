"""
Structured Logging Setup

This module provides:
- Structured logging configuration with structlog
- JSON output format
- Contextual logging
"""

import logging
import sys

import structlog
from structlog.dev import ConsoleRenderer
from structlog.processors import JSONRenderer
from structlog.stdlib import LogFormatter

def setup_structured_logging():
    """Setup structured logging for the application."""

    # Configure standard library logging
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=logging.INFO,
    )

    # Configure structlog
    shared_processors = [
        structlog.stdlib.filter_by_level,
        structlog.processors.TimeStamper(fmt="iso"),
        structlog.stdlib.add_logger_name,
        structlog.stdlib.add_log_level,
        structlog.stdlib.PositionalArgumentsFormatter(),
        structlog.processors.StackInfoRenderer(),
        structlog.processors.format_exc_info,
        structlog.processors.UnicodeDecoder(),
    ]

    # Development: console output
    if __debug__:
        processors = shared_processors + [
            structlog.stdlib.ProcessorFormatter.wrap_for_formatter,
        ]
        formatter = LogFormatter(
            processors=[
                structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                ConsoleRenderer(colors=True),
            ],
        )
    else:
        # Production: JSON output
        processors = shared_processors + [
            structlog.processors.JSONRenderer(),
        ]
        formatter = LogFormatter(
            processors=[
                structlog.stdlib.ProcessorFormatter.remove_processors_meta,
                JSONRenderer(),
            ],
        )

    # Apply configuration
    structlog.configure(
        processors=processors,
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )

    # Set formatter for standard library handlers
    handler = logging.getLogger().handlers[0]
    handler.setFormatter(formatter)