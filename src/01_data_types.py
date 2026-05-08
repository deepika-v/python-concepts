"""
Python Data Types Concepts

This module demonstrates Python's fundamental data types:
- Numbers (int, float, complex)
- Strings
- Booleans
- Collections (list, tuple, dict, set)
"""

# ============================================================================
# NUMERIC DATA TYPES
# ============================================================================

print("=" * 60)
print("NUMERIC DATA TYPES")
print("=" * 60)

# Integer (whole numbers)
num_int = 42
print(f"Integer: {num_int}, Type: {type(num_int)}")

# Float (decimal numbers)
num_float = 3.14
print(f"Float: {num_float}, Type: {type(num_float)}")

# Complex (with imaginary part)
num_complex = 3 + 4j
print(f"Complex: {num_complex}, Type: {type(num_complex)}")

# ============================================================================
# STRING DATA TYPE
# ============================================================================

print("\n" + "=" * 60)
print("STRING DATA TYPE")
print("=" * 60)

# String creation (single, double, triple quotes)
single_quote = 'Hello'
double_quote = "World"
triple_quote = """This is a
multi-line string"""

print(f"Single: {single_quote}")
print(f"Double: {double_quote}")
print(f"Triple:\n{triple_quote}")

# String operations
text = "Python"
print(f"Length of '{text}': {len(text)}")
print(f"Uppercase: {text.upper()}")
print(f"Lowercase: {text.lower()}")
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")

# ============================================================================
# BOOLEAN DATA TYPE
# ============================================================================

print("\n" + "=" * 60)
print("BOOLEAN DATA TYPE")
print("=" * 60)

is_active = True
is_deleted = False

print(f"is_active: {is_active}, Type: {type(is_active)}")
print(f"is_deleted: {is_deleted}, Type: {type(is_deleted)}")

# Boolean comparisons
x, y = 10, 20
print(f"x > y: {x > y}")
print(f"x < y: {x < y}")
print(f"x == y: {x == y}")

# ============================================================================
# LIST (ORDERED, MUTABLE COLLECTION)
# ============================================================================

print("\n" + "=" * 60)
print("LIST - ORDERED, MUTABLE COLLECTION")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]
mixed_list = [1, "Hello", 3.14, True]

print(f"Numbers: {numbers}")
print(f"Mixed list: {mixed_list}")
print(f"First element: {numbers[0]}")
print(f"Last element: {numbers[-1]}")

# List operations
numbers.append(6)
print(f"After append(6): {numbers}")

numbers.extend([7, 8])
print(f"After extend([7, 8]): {numbers}")

removed = numbers.pop()
print(f"Popped {removed}, list now: {numbers}")

# ============================================================================
# TUPLE (ORDERED, IMMUTABLE COLLECTION)
# ============================================================================

print("\n" + "=" * 60)
print("TUPLE - ORDERED, IMMUTABLE COLLECTION")
print("=" * 60)

coordinates = (10, 20, 30)
person = ("Alice", 30, "Engineer")

print(f"Coordinates: {coordinates}, Type: {type(coordinates)}")
print(f"Person: {person}")
print(f"First element: {coordinates[0]}")

# Tuples are immutable - this would cause an error:
# coordinates[0] = 15  # TypeError: 'tuple' object does not support item assignment

# Tuple unpacking
x, y, z = coordinates
print(f"Unpacked: x={x}, y={y}, z={z}")

# ============================================================================
# DICTIONARY (KEY-VALUE PAIRS, MUTABLE)
# ============================================================================

print("\n" + "=" * 60)
print("DICTIONARY - KEY-VALUE PAIRS")
print("=" * 60)

student = {
    "name": "Bob",
    "age": 25,
    "grade": "A",
    "courses": ["Math", "Science"]
}

print(f"Dictionary: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student.get('age')}")

# Dictionary operations
student['email'] = "bob@example.com"
print(f"After adding email: {student}")

# Iterate through dictionary
print("Dictionary items:")
for key, value in student.items():
    print(f"  {key}: {value}")

# ============================================================================
# SET (UNORDERED, UNIQUE ELEMENTS)
# ============================================================================

print("\n" + "=" * 60)
print("SET - UNORDERED, UNIQUE ELEMENTS")
print("=" * 60)

colors = {"red", "blue", "green"}
numbers_set = {1, 2, 3, 4, 5, 5, 5}  # Duplicates are removed

print(f"Colors: {colors}")
print(f"Numbers (duplicates removed): {numbers_set}")

# Set operations
colors.add("yellow")
print(f"After add('yellow'): {colors}")

colors.discard("red")
print(f"After discard('red'): {colors}")

# Set math operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")
print(f"Intersection: {set1 & set2}")
print(f"Difference: {set1 - set2}")

# ============================================================================
# TYPE CONVERSION
# ============================================================================

print("\n" + "=" * 60)
print("TYPE CONVERSION")
print("=" * 60)

# Convert to int
str_num = "123"
converted_int = int(str_num)
print(f"String '{str_num}' to int: {converted_int}")

# Convert to float
converted_float = float("3.14")
print(f"String '3.14' to float: {converted_float}")

# Convert to string
converted_str = str(42)
print(f"Number 42 to string: '{converted_str}'")

# Convert to list
tuple_data = (1, 2, 3)
converted_list = list(tuple_data)
print(f"Tuple {tuple_data} to list: {converted_list}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Python has dynamic typing - variables can change types
2. Numbers: int, float, complex
3. Strings: immutable sequences of characters
4. Booleans: True/False for logical operations
5. Collections:
   - List: mutable, ordered, allows duplicates
   - Tuple: immutable, ordered, allows duplicates
   - Dictionary: mutable, key-value pairs
   - Set: mutable, unordered, unique elements only
6. Use type() to check data type
7. Use type conversion functions: int(), float(), str(), list(), etc.
""")
