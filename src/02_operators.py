"""
Python Operators Concepts

This module demonstrates different types of operators:
- Arithmetic operators
- Comparison operators
- Logical operators
- Bitwise operators
- Assignment operators
- Identity and Membership operators
"""

# ============================================================================
# ARITHMETIC OPERATORS
# ============================================================================

print("=" * 60)
print("ARITHMETIC OPERATORS")
print("=" * 60)

a, b = 10, 3

print(f"a = {a}, b = {b}")
print(f"Addition (a + b): {a + b}")
print(f"Subtraction (a - b): {a - b}")
print(f"Multiplication (a * b): {a * b}")
print(f"Division (a / b): {a / b}")              # Returns float
print(f"Floor Division (a // b): {a // b}")      # Returns integer
print(f"Modulus (a % b): {a % b}")               # Remainder
print(f"Exponentiation (a ** b): {a ** b}")      # Power

# ============================================================================
# COMPARISON OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("COMPARISON OPERATORS")
print("=" * 60)

x, y = 15, 10

print(f"x = {x}, y = {y}")
print(f"x == y (equal): {x == y}")
print(f"x != y (not equal): {x != y}")
print(f"x > y (greater than): {x > y}")
print(f"x < y (less than): {x < y}")
print(f"x >= y (greater or equal): {x >= y}")
print(f"x <= y (less or equal): {x <= y}")

# Comparison returns boolean
result = x > y
print(f"Result type: {type(result)}")

# ============================================================================
# LOGICAL OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("LOGICAL OPERATORS")
print("=" * 60)

# AND operator
cond1 = True
cond2 = False
print(f"cond1 = {cond1}, cond2 = {cond2}")
print(f"cond1 AND cond2: {cond1 and cond2}")

# OR operator
print(f"cond1 OR cond2: {cond1 or cond2}")

# NOT operator
print(f"NOT cond1: {not cond1}")
print(f"NOT cond2: {not cond2}")

# Short-circuit evaluation
print("\nShort-circuit evaluation:")
print(f"False and (10/0): ", end="")
try:
    print(False and (10/0))  # Won't evaluate 10/0
except ZeroDivisionError:
    print("Error")

print(f"True or (10/0): ", end="")
print(True or (10/0))  # Won't evaluate 10/0

# ============================================================================
# BITWISE OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("BITWISE OPERATORS")
print("=" * 60)

# Binary representation for clarity
num1, num2 = 5, 3  # 0101, 0011

print(f"num1 = {num1} (binary: {bin(num1)})")
print(f"num2 = {num2} (binary: {bin(num2)})")

# Bitwise AND
print(f"num1 & num2 (AND): {num1 & num2}")

# Bitwise OR
print(f"num1 | num2 (OR): {num1 | num2}")

# Bitwise XOR (exclusive OR)
print(f"num1 ^ num2 (XOR): {num1 ^ num2}")

# Bitwise NOT
print(f"~num1 (NOT): {~num1}")

# Left shift
print(f"num1 << 1 (left shift): {num1 << 1}")

# Right shift
print(f"num1 >> 1 (right shift): {num1 >> 1}")

# ============================================================================
# ASSIGNMENT OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("ASSIGNMENT OPERATORS")
print("=" * 60)

# Basic assignment
var = 10
print(f"var = 10: {var}")

# Augmented assignment
var += 5
print(f"var += 5: {var}")

var -= 3
print(f"var -= 3: {var}")

var *= 2
print(f"var *= 2: {var}")

var /= 4
print(f"var /= 4: {var}")

var //= 2
print(f"var //= 2: {var}")

var **= 2
print(f"var **= 2: {var}")

var %= 5
print(f"var %= 5: {var}")

# ============================================================================
# IDENTITY OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("IDENTITY OPERATORS")
print("=" * 60)

# 'is' checks if two variables refer to the same object in memory
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1

print(f"list1 = {list1}")
print(f"list2 = {list2}")
print(f"list3 = list1")

print(f"list1 is list2: {list1 is list2}")  # False - different objects
print(f"list1 == list2: {list1 == list2}")  # True - same content
print(f"list1 is list3: {list1 is list3}")  # True - same object

# None comparison
value = None
print(f"\nvalue = None")
print(f"value is None: {value is None}")  # Correct way
print(f"value == None: {value == None}")  # Also works but less Pythonic

# ============================================================================
# MEMBERSHIP OPERATORS
# ============================================================================

print("\n" + "=" * 60)
print("MEMBERSHIP OPERATORS")
print("=" * 60)

numbers = [1, 2, 3, 4, 5]
word = "Python"

print(f"numbers = {numbers}")
print(f"word = '{word}'")

print(f"\n3 in numbers: {3 in numbers}")
print(f"6 in numbers: {6 in numbers}")

print(f"\n'P' in word: {'P' in word}")
print(f"'x' in word: {'x' in word}")

print(f"\n'P' not in word: {'P' not in word}")
print(f"'x' not in word: {'x' not in word}")

# ============================================================================
# OPERATOR PRECEDENCE
# ============================================================================

print("\n" + "=" * 60)
print("OPERATOR PRECEDENCE")
print("=" * 60)

print("""
Precedence (highest to lowest):
1. ** (Exponentiation)
2. +x, -x, ~x (Unary plus, minus, bitwise NOT)
3. *, /, //, % (Multiplication, division, floor division, modulus)
4. +, - (Addition, subtraction)
5. <<, >> (Bitwise shifts)
6. & (Bitwise AND)
7. ^ (Bitwise XOR)
8. | (Bitwise OR)
9. ==, !=, <, <=, >, >=, is, is not, in, not in (Comparisons)
10. not (Logical NOT)
11. and (Logical AND)
12. or (Logical OR)
""")

# Examples
result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # Multiplication first: 2 + 12 = 14

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # Parentheses first: 5 * 4 = 20

result3 = 10 - 3 - 2
print(f"10 - 3 - 2 = {result3}")  # Left to right: 7 - 2 = 5

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Arithmetic: +, -, *, /, //, %, **
2. Comparison: ==, !=, <, <=, >, >=
3. Logical: and, or, not
4. Bitwise: &, |, ^, ~, <<, >>
5. Assignment: =, +=, -=, *=, /=, //=, **=, %=
6. Identity: is, is not (checks object identity)
7. Membership: in, not in (checks collection membership)
8. Use parentheses for clarity in complex expressions
""")
