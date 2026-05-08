"""
Python List, Set, and Dictionary Comprehension Concepts

This module demonstrates:
- List comprehensions
- Set comprehensions
- Dictionary comprehensions
- Nested comprehensions
- Conditional comprehensions
- Generator expressions
"""

# ============================================================================
# BASIC LIST COMPREHENSION
# ============================================================================

print("=" * 60)
print("BASIC LIST COMPREHENSION")
print("=" * 60)

# Traditional way
squares_traditional = []
for x in range(5):
    squares_traditional.append(x ** 2)
print(f"Traditional: {squares_traditional}")

# Using list comprehension
squares_comprehension = [x ** 2 for x in range(5)]
print(f"Comprehension: {squares_comprehension}")

# ============================================================================
# LIST COMPREHENSION WITH CONDITION
# ============================================================================

print("\n" + "=" * 60)
print("LIST COMPREHENSION WITH CONDITION")
print("=" * 60)

# Get even numbers
numbers = range(10)
evens = [x for x in numbers if x % 2 == 0]
print(f"Even numbers: {evens}")

# Get odd numbers
odds = [x for x in numbers if x % 2 != 0]
print(f"Odd numbers: {odds}")

# Multiple conditions
result = [x for x in range(20) if x % 2 == 0 if x % 3 == 0]
print(f"Divisible by 2 and 3: {result}")

# ============================================================================
# LIST COMPREHENSION WITH CONDITIONAL EXPRESSION
# ============================================================================

print("\n" + "=" * 60)
print("LIST COMPREHENSION WITH IF-ELSE")
print("=" * 60)

# Convert values: even -> "even", odd -> "odd"
result = ["even" if x % 2 == 0 else "odd" for x in range(5)]
print(f"Even/Odd labels: {result}")

# Convert numbers: keep if divisible by 2, otherwise 0
result = [x if x % 2 == 0 else 0 for x in range(5)]
print(f"Keep evens, zero odds: {result}")

# ============================================================================
# LIST COMPREHENSION WITH TRANSFORMATION
# ============================================================================

print("\n" + "=" * 60)
print("LIST COMPREHENSION WITH TRANSFORMATION")
print("=" * 60)

# Convert to uppercase
words = ["apple", "banana", "cherry"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")

# Extract length of each word
lengths = [len(word) for word in words]
print(f"Lengths: {lengths}")

# Combine strings
combined = [f"{i}-{word}" for i, word in enumerate(words)]
print(f"Combined: {combined}")

# ============================================================================
# NESTED LIST COMPREHENSION
# ============================================================================

print("\n" + "=" * 60)
print("NESTED LIST COMPREHENSION")
print("=" * 60)

# Create matrix (2D list)
matrix = [[i*j for j in range(1, 4)] for i in range(1, 4)]
print("Matrix (3x3):")
for row in matrix:
    print(f"  {row}")

# Flatten a 2D list
matrix_2d = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [x for row in matrix_2d for x in row]
print(f"\nOriginal 2D: {matrix_2d}")
print(f"Flattened: {flattened}")

# ============================================================================
# SET COMPREHENSION
# ============================================================================

print("\n" + "=" * 60)
print("SET COMPREHENSION")
print("=" * 60)

# Basic set comprehension
squares_set = {x ** 2 for x in range(5)}
print(f"Squares: {squares_set}")

# Remove duplicates automatically
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique = {x for x in numbers}
print(f"Original: {numbers}")
print(f"Unique: {unique}")

# Set comprehension with condition
evens_set = {x for x in range(10) if x % 2 == 0}
print(f"Even set: {evens_set}")

# ============================================================================
# DICTIONARY COMPREHENSION
# ============================================================================

print("\n" + "=" * 60)
print("DICTIONARY COMPREHENSION")
print("=" * 60)

# Create dictionary from range
squares_dict = {x: x**2 for x in range(5)}
print(f"Squares dict: {squares_dict}")

# Convert list to dictionary
keys = ["a", "b", "c", "d"]
values = [1, 2, 3, 4]
dictionary = {k: v for k, v in zip(keys, values)}
print(f"Combined dict: {dictionary}")

# Invert dictionary (swap keys and values)
original = {"name": "John", "age": 30, "city": "NYC"}
inverted = {v: k for k, v in original.items()}
print(f"Original: {original}")
print(f"Inverted: {inverted}")

# Dictionary comprehension with condition
words = ["apple", "banana", "cherry", "date"]
word_lengths = {word: len(word) for word in words if len(word) > 4}
print(f"Words > 4 chars with lengths: {word_lengths}")

# ============================================================================
# GENERATOR EXPRESSIONS
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR EXPRESSIONS")
print("=" * 60)

# Generator expression (memory efficient for large datasets)
# Syntax similar to list comprehension but with parentheses
gen = (x ** 2 for x in range(10))
print(f"Generator object: {gen}")
print(f"Type: {type(gen)}")

# Convert to list to see results
results = list(gen)
print(f"Results: {results}")

# Generators are lazy - values computed on demand
gen = (x for x in range(5))
print(f"Next value: {next(gen)}")
print(f"Next value: {next(gen)}")
print(f"Next value: {next(gen)}")

# Use generator with sum() without creating list
total = sum(x ** 2 for x in range(5))
print(f"\nSum of squares 0-4: {total}")

# ============================================================================
# ADVANCED EXAMPLES
# ============================================================================

print("\n" + "=" * 60)
print("ADVANCED EXAMPLES")
print("=" * 60)

# Parse strings into integers
strings = ["1", "2", "3", "4", "5"]
integers = [int(s) for s in strings]
print(f"Strings to integers: {integers}")

# Filter and transform
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
double_evens = [x * 2 for x in numbers if x % 2 == 0]
print(f"Double even numbers: {double_evens}")

# Create pairs
letters = ["a", "b", "c"]
pairs = [(l, n) for l in letters for n in range(1, 3)]
print(f"Letter-number pairs: {pairs}")

# Transpose matrix
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
transposed = [[row[i] for row in matrix] for i in range(3)]
print(f"Original matrix: {matrix}")
print(f"Transposed: {transposed}")

# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

print("\n" + "=" * 60)
print("PERFORMANCE COMPARISON")
print("=" * 60)

import time

# List comprehension performance
start = time.time()
result = [x ** 2 for x in range(10000)]
time_comp = time.time() - start
print(f"List comprehension: {time_comp:.6f} seconds")

# Traditional loop
start = time.time()
result = []
for x in range(10000):
    result.append(x ** 2)
time_loop = time.time() - start
print(f"Traditional loop: {time_loop:.6f} seconds")

# Generator expression
start = time.time()
result = list(x ** 2 for x in range(10000))
time_gen = time.time() - start
print(f"Generator (converted to list): {time_gen:.6f} seconds")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. List comprehension: [expr for item in iterable]
2. With condition: [expr for item in iterable if condition]
3. With if-else: [expr_true if condition else expr_false for item in iterable]
4. Set comprehension: {expr for item in iterable}
5. Dict comprehension: {key: value for item in iterable}
6. Nested comprehension: [expr for item1 in iter1 for item2 in iter2]
7. Generator expression: (expr for item in iterable)
8. Generators: Memory efficient for large datasets
9. Use comprehensions for cleaner, more readable code
10. List comprehensions are usually faster than loops
""")
