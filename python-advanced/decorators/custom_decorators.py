"""
Custom Decorators Examples

This file demonstrates:
- Writing decorators that wrap functions
- Using functools.wraps to preserve metadata
- Decorators with arguments
- Simple memoization decorator
"""

from functools import wraps


def simple_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__} with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"{func.__name__} returned {result}")
        return result

    return wrapper


def retry(times=3):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            last_exception = None
            for attempt in range(1, times + 1):
                try:
                    print(f"Attempt {attempt} for {func.__name__}")
                    return func(*args, **kwargs)
                except Exception as exc:
                    last_exception = exc
                    print(f"Failed attempt {attempt}: {exc}")
            raise last_exception

        return wrapper

    return decorator


def memoize(func):
    cache = {}

    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Cache hit for {func.__name__}{args}")
            return cache[args]
        print(f"Cache miss for {func.__name__}{args}")
        result = func(*args)
        cache[args] = result
        return result

    return wrapper


@simple_logger
@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


@retry(times=2)
def fragile_action(value):
    if value < 5:
        raise ValueError("Value is too small")
    return f"Success with {value}"


def main():
    print("Custom Decorators Demonstration")
    print("=" * 30)
    print(f"Fibonacci(6): {fibonacci(6)}")
    try:
        print(fragile_action(3))
    except ValueError as exc:
        print("Final exception after retries:", exc)


if __name__ == "__main__":
    main()