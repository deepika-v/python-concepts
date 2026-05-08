"""
Python Decorators Concepts

This module demonstrates:
- Function decorators
- Decorator syntax (@)
- Decorators with arguments
- Stacking decorators
- Class decorators
"""

# ============================================================================
# BASIC FUNCTION DECORATOR
# ============================================================================

print("=" * 60)
print("BASIC FUNCTION DECORATOR")
print("=" * 60)

def simple_decorator(func):
    """A simple decorator that prints before and after function call."""
    def wrapper():
        print("Before function call")
        func()
        print("After function call")
    return wrapper

# Without decorator
def greet():
    print("Hello!")

print("Without decorator:")
greet()

# With decorator using @ syntax
@simple_decorator
def greet_decorated():
    print("Hello from decorated function!")

print("\nWith decorator:")
greet_decorated()

# ============================================================================
# DECORATOR WITH ARGUMENTS
# ============================================================================

print("\n" + "=" * 60)
print("DECORATOR WITH ARGUMENTS")
print("=" * 60)

def decorator_with_args(func):
    """Decorator that preserves function arguments."""
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Arguments: {args}, Keyword Arguments: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Result: {result}")
        return result
    return wrapper

@decorator_with_args
def add(a, b):
    """Add two numbers."""
    return a + b

print("Adding 5 and 3:")
add(5, 3)

print("\nWith keyword arguments:")
@decorator_with_args
def greet_person(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet_person("Alice", greeting="Hi")

# ============================================================================
# DECORATOR WITH PARAMETERS
# ============================================================================

print("\n" + "=" * 60)
print("DECORATOR WITH PARAMETERS")
print("=" * 60)

def repeat(times):
    """Decorator that repeats function execution."""
    def decorator(func):
        def wrapper(*args, **kwargs):
            results = []
            for i in range(times):
                result = func(*args, **kwargs)
                results.append(result)
            return results
        return wrapper
    return decorator

@repeat(times=3)
def say_hello():
    return "Hello!"

print("Repeating 'say_hello' 3 times:")
print(say_hello())

# ============================================================================
# TIMING DECORATOR
# ============================================================================

print("\n" + "=" * 60)
print("TIMING DECORATOR")
print("=" * 60)

import time

def timer(func):
    """Decorator to measure function execution time."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start:.6f} seconds")
        return result
    return wrapper

@timer
def slow_function():
    """Simulate slow function."""
    time.sleep(0.5)
    return "Done"

print("Timing slow function:")
slow_function()

# ============================================================================
# DECORATOR WITH FUNCTOOLS WRAPS
# ============================================================================

print("\n" + "=" * 60)
print("DECORATOR WITH FUNCTOOLS WRAPS")
print("=" * 60)

from functools import wraps

def good_decorator(func):
    """Decorator that preserves metadata using functools.wraps."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

@good_decorator
def example_function():
    """This is an example function."""
    return "Result"

print(f"Function name: {example_function.__name__}")
print(f"Function docstring: {example_function.__doc__}")

# ============================================================================
# STACKING DECORATORS
# ============================================================================

print("\n" + "=" * 60)
print("STACKING DECORATORS")
print("=" * 60)

def decorator_one(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 1 - Before")
        result = func(*args, **kwargs)
        print("Decorator 1 - After")
        return result
    return wrapper

def decorator_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Decorator 2 - Before")
        result = func(*args, **kwargs)
        print("Decorator 2 - After")
        return result
    return wrapper

@decorator_one
@decorator_two
def multi_decorated():
    print("Main function")
    return "Done"

print("Calling multi-decorated function:")
multi_decorated()

print("\nNote: Decorators apply bottom-up (decorator_two first)")

# ============================================================================
# CLASS DECORATOR
# ============================================================================

print("\n" + "=" * 60)
print("CLASS DECORATOR")
print("=" * 60)

def add_greeting(cls):
    """Decorator that adds a method to a class."""
    def greet(self):
        return f"Hello from {cls.__name__}"
    cls.greet = greet
    return cls

@add_greeting
class MyClass:
    pass

obj = MyClass()
print(obj.greet())

# ============================================================================
# VALIDATION DECORATOR
# ============================================================================

print("\n" + "=" * 60)
print("VALIDATION DECORATOR")
print("=" * 60)

def validate_int(*type_checks):
    """Decorator that validates argument types."""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Validate positional arguments
            for arg, expected_type in zip(args, type_checks):
                if not isinstance(arg, expected_type):
                    raise TypeError(
                        f"Argument must be {expected_type.__name__}, "
                        f"got {type(arg).__name__}"
                    )
            return func(*args, **kwargs)
        return wrapper
    return decorator

@validate_int(int, int)
def multiply(a, b):
    return a * b

print("Valid call: multiply(3, 4) =", multiply(3, 4))

print("\nInvalid call:")
try:
    multiply("3", 4)
except TypeError as e:
    print(f"Error: {e}")

# ============================================================================
# MEMOIZATION DECORATOR
# ============================================================================

print("\n" + "=" * 60)
print("MEMOIZATION DECORATOR - CACHING")
print("=" * 60)

def memoize(func):
    """Decorator that caches function results."""
    cache = {}
    
    @wraps(func)
    def wrapper(*args):
        if args in cache:
            print(f"Returning cached result for {args}")
            return cache[args]
        else:
            print(f"Computing result for {args}")
            result = func(*args)
            cache[args] = result
            return result
    
    return wrapper

@memoize
def fibonacci(n):
    """Calculate fibonacci number."""
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci(5):")
fibonacci(5)

print("\nFibonacci(5) again (cached):")
fibonacci(5)

# ============================================================================
# LOGGING DECORATOR
# ============================================================================

print("\n" + "=" * 60)
print("LOGGING DECORATOR")
print("=" * 60)

def log_call(func):
    """Decorator that logs function calls."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"LOG: Calling {func.__name__}")
        print(f"LOG: Arguments: {args}, Keyword args: {kwargs}")
        try:
            result = func(*args, **kwargs)
            print(f"LOG: {func.__name__} returned {result}")
            return result
        except Exception as e:
            print(f"LOG: {func.__name__} raised {type(e).__name__}: {e}")
            raise
    return wrapper

@log_call
def divide(a, b):
    return a / b

print("Dividing 10 by 2:")
divide(10, 2)

print("\nDividing by zero:")
try:
    divide(10, 0)
except ZeroDivisionError:
    print("Caught exception")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Decorator: Function that modifies another function/class
2. @syntax: Shorthand for function decoration
3. def decorator(func): Returns a wrapper function
4. *args, **kwargs: Preserve original function arguments
5. functools.wraps: Preserves metadata (__name__, __doc__)
6. Decorator parameters: Decorator factory (decorator returning decorator)
7. Stacking: Multiple @ decorators applied bottom-up
8. Use cases: Logging, timing, validation, caching, authentication
9. Class decorators: Add/modify class methods and attributes
10. Memoization: Cache results for performance
""")
