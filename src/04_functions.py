"""
Python Functions Concepts

This module demonstrates:
- Function definition and calling
- Parameters and arguments
- Return values
- Default parameters
- *args and **kwargs
- Scope and namespaces
- Docstrings
"""

# ============================================================================
# BASIC FUNCTION
# ============================================================================

print("=" * 60)
print("BASIC FUNCTION")
print("=" * 60)

def greet():
    """Simple function with no parameters."""
    print("Hello, World!")

greet()

# ============================================================================
# FUNCTION WITH PARAMETERS
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTION WITH PARAMETERS")
print("=" * 60)

def greet_person(name):
    """Function that takes a parameter."""
    print(f"Hello, {name}!")

greet_person("Alice")

# Multiple parameters
def add(a, b):
    """Function that takes two parameters."""
    print(f"{a} + {b} = {a + b}")

add(5, 3)

# ============================================================================
# FUNCTION WITH RETURN VALUE
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTION WITH RETURN VALUE")
print("=" * 60)

def multiply(a, b):
    """Function that returns a value."""
    return a * b

result = multiply(4, 5)
print(f"multiply(4, 5) = {result}")

# Multiple return values (as tuple)
def get_coordinates():
    """Function that returns multiple values."""
    return 10, 20, 30

x, y, z = get_coordinates()
print(f"Coordinates: x={x}, y={y}, z={z}")

# ============================================================================
# DEFAULT PARAMETERS
# ============================================================================

print("\n" + "=" * 60)
print("DEFAULT PARAMETERS")
print("=" * 60)

def introduce(name, age=25, city="New York"):
    """Function with default parameters."""
    print(f"Name: {name}, Age: {age}, City: {city}")

introduce("Bob")  # Uses default age and city
introduce("Charlie", 30)  # Uses default city
introduce("Diana", 28, "Los Angeles")  # All specified

# ============================================================================
# VARIABLE-LENGTH ARGUMENTS (*args)
# ============================================================================

print("\n" + "=" * 60)
print("VARIABLE-LENGTH ARGUMENTS (*args)")
print("=" * 60)

def sum_numbers(*args):
    """Function that accepts variable number of positional arguments."""
    print(f"Arguments: {args}")
    total = sum(args)
    return total

result1 = sum_numbers(1, 2, 3)
print(f"sum_numbers(1, 2, 3) = {result1}")

result2 = sum_numbers(1, 2, 3, 4, 5)
print(f"sum_numbers(1, 2, 3, 4, 5) = {result2}")

# ============================================================================
# KEYWORD ARGUMENTS (**kwargs)
# ============================================================================

print("\n" + "=" * 60)
print("KEYWORD ARGUMENTS (**kwargs)")
print("=" * 60)

def print_info(**kwargs):
    """Function that accepts variable number of keyword arguments."""
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print("Info:")
print_info(name="Eve", age=26, job="Engineer")

# ============================================================================
# COMBINING *args AND **kwargs
# ============================================================================

print("\n" + "=" * 60)
print("COMBINING *args AND **kwargs")
print("=" * 60)

def flexible_function(a, b, *args, **kwargs):
    """Function combining positional, variable, and keyword arguments."""
    print(f"Required: a={a}, b={b}")
    print(f"*args: {args}")
    print(f"**kwargs: {kwargs}")

flexible_function(1, 2, 3, 4, 5, name="Frank", age=35)

# ============================================================================
# UNPACKING WITH * AND **
# ============================================================================

print("\n" + "=" * 60)
print("UNPACKING WITH * AND **")
print("=" * 60)

def calculate(x, y, z):
    """Simple function for demonstration."""
    return x + y + z

# Unpack list with *
numbers = [10, 20, 30]
result = calculate(*numbers)
print(f"calculate(*{numbers}) = {result}")

# Unpack dictionary with **
def show_person(name, age, city):
    """Simple function for demonstration."""
    print(f"Name: {name}, Age: {age}, City: {city}")

person_dict = {"name": "George", "age": 40, "city": "Boston"}
show_person(**person_dict)

# ============================================================================
# SCOPE AND NAMESPACES
# ============================================================================

print("\n" + "=" * 60)
print("SCOPE AND NAMESPACES")
print("=" * 60)

# Global variable
global_var = "I'm global"

def test_scope():
    """Function to demonstrate scope."""
    # Local variable
    local_var = "I'm local"
    print(f"Inside function - global: {global_var}")
    print(f"Inside function - local: {local_var}")

print(f"Outside function - global: {global_var}")
test_scope()

# Local scope doesn't exist outside function
# print(f"Outside function - local: {local_var}")  # NameError

# ============================================================================
# GLOBAL AND NONLOCAL KEYWORDS
# ============================================================================

print("\n" + "=" * 60)
print("GLOBAL AND NONLOCAL KEYWORDS")
print("=" * 60)

counter = 0

def increment_global():
    """Function using global keyword."""
    global counter
    counter += 1
    print(f"Counter: {counter}")

increment_global()
increment_global()

# Nonlocal example
def outer():
    """Outer function."""
    x = "outer"
    
    def inner():
        """Inner function using nonlocal."""
        nonlocal x
        x = "modified"
        print(f"Inside inner: {x}")
    
    inner()
    print(f"Inside outer after inner: {x}")

outer()

# ============================================================================
# LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)
# ============================================================================

print("\n" + "=" * 60)
print("LAMBDA FUNCTIONS (ANONYMOUS FUNCTIONS)")
print("=" * 60)

# Simple lambda
square = lambda x: x ** 2
print(f"square(5) = {square(5)}")

# Lambda with multiple parameters
add = lambda x, y: x + y
print(f"add(3, 4) = {add(3, 4)}")

# Lambda with map
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(f"Squared: {squared}")

# Lambda with filter
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {evens}")

# ============================================================================
# DOCSTRINGS AND HELP
# ============================================================================

print("\n" + "=" * 60)
print("DOCSTRINGS AND HELP")
print("=" * 60)

def documented_function(param1, param2):
    """
    This is a docstring explaining the function.
    
    Args:
        param1: First parameter description
        param2: Second parameter description
    
    Returns:
        Description of return value
    """
    return param1 + param2

print("Function docstring:")
print(documented_function.__doc__)

# Or use help()
print("\nUsing help():")
help(documented_function)

# ============================================================================
# FUNCTION ANNOTATIONS
# ============================================================================

print("\n" + "=" * 60)
print("FUNCTION ANNOTATIONS")
print("=" * 60)

def annotated_function(name: str, age: int) -> str:
    """Function with type hints (annotations)."""
    return f"{name} is {age} years old"

result = annotated_function("Henry", 45)
print(f"Result: {result}")

# Annotations are stored in __annotations__
print(f"Annotations: {annotated_function.__annotations__}")

# ============================================================================
# CLOSURE
# ============================================================================

print("\n" + "=" * 60)
print("CLOSURE")
print("=" * 60)

def make_multiplier(n):
    """Returns a function that multiplies by n."""
    def multiplier(x):
        return x * n
    return multiplier

multiply_by_3 = make_multiplier(3)
multiply_by_5 = make_multiplier(5)

print(f"multiply_by_3(10) = {multiply_by_3(10)}")
print(f"multiply_by_5(10) = {multiply_by_5(10)}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. def: Keyword to define a function
2. Parameters: Defined in function signature
3. Arguments: Passed when calling function
4. return: Returns value(s) from function
5. *args: Accept variable positional arguments
6. **kwargs: Accept variable keyword arguments
7. Default parameters: Provide fallback values
8. Global: Access/modify global variables
9. Nonlocal: Access/modify variables in outer scope
10. Lambda: Anonymous single-line functions
11. Docstrings: Document functions
12. Type hints: Annotations for parameter/return types
13. Closure: Functions that capture variables
""")
