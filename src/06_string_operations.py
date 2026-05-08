"""
Python String Operations Concepts

This module demonstrates:
- String creation and basic operations
- String methods
- String formatting
- String slicing and indexing
- Regular expressions basics
"""

# ============================================================================
# STRING CREATION AND BASIC OPERATIONS
# ============================================================================

print("=" * 60)
print("STRING CREATION AND BASIC OPERATIONS")
print("=" * 60)

# Different ways to create strings
single = 'Hello'
double = "World"
triple = """This is
a multi-line
string"""

print(f"Single: {single}")
print(f"Double: {double}")
print(f"Triple:\n{triple}")

# String concatenation
combined = single + " " + double
print(f"Concatenation: {combined}")

# String repetition
repeated = "Ha" * 3
print(f"Repetition: {repeated}")

# ============================================================================
# STRING INDEXING AND SLICING
# ============================================================================

print("\n" + "=" * 60)
print("STRING INDEXING AND SLICING")
print("=" * 60)

text = "Python"

# Indexing (0-based)
print(f"First character: {text[0]}")
print(f"Last character: {text[-1]}")
print(f"Third character: {text[2]}")

# Slicing
print(f"First 3 characters: {text[0:3]}")
print(f"From index 2 to end: {text[2:]}")
print(f"Last 3 characters: {text[-3:]}")
print(f"Every 2nd character: {text[::2]}")
print(f"Reversed: {text[::-1]}")

# ============================================================================
# STRING METHODS - CASE CONVERSION
# ============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - CASE CONVERSION")
print("=" * 60)

text = "Hello World"
print(f"Original: {text}")
print(f"Upper: {text.upper()}")
print(f"Lower: {text.lower()}")
print(f"Title: {text.title()}")
print(f"Swap: {text.swapcase()}")
print(f"Capitalize: {text.capitalize()}")

# ============================================================================
# STRING METHODS - SEARCHING AND REPLACING
# ============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - SEARCHING AND REPLACING")
print("=" * 60)

text = "The quick brown fox jumps over the lazy dog"

# Find and count
print(f"Original: {text}")
print(f"Find 'fox': {text.find('fox')}")
print(f"Count 'o': {text.count('o')}")
print(f"Starts with 'The': {text.startswith('The')}")
print(f"Ends with 'dog': {text.endswith('dog')}")

# Replace
replaced = text.replace("fox", "cat")
print(f"Replace 'fox' with 'cat': {replaced}")

# ============================================================================
# STRING METHODS - SPLIT AND JOIN
# ============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - SPLIT AND JOIN")
print("=" * 60)

text = "apple,banana,cherry,date"

# Split
words = text.split(",")
print(f"Original: {text}")
print(f"Split by comma: {words}")

# Join
joined = "-".join(words)
print(f"Joined by dash: {joined}")

# Split lines
multiline = "Line1\nLine2\nLine3"
lines = multiline.split("\n")
print(f"Lines: {lines}")

# ============================================================================
# STRING METHODS - STRIPPING AND PADDING
# ============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - STRIPPING AND PADDING")
print("=" * 60)

text = "  Hello World  "

# Strip whitespace
print(f"Original: '{text}'")
print(f"Strip: '{text.strip()}'")
print(f"Lstrip: '{text.lstrip()}'")
print(f"Rstrip: '{text.rstrip()}'")

# Center and align
text = "Python"
print(f"\nOriginal: {text}")
print(f"Center (20): '{text.center(20)}'")
print(f"Left align (20): '{text.ljust(20)}'")
print(f"Right align (20): '{text.rjust(20)}'")

# Padding with character
print(f"Zfill (10): '{text.zfill(10)}'")

# ============================================================================
# STRING FORMATTING - OLD STYLE (%)
# ============================================================================

print("\n" + "=" * 60)
print("STRING FORMATTING - OLD STYLE (%)")
print("=" * 60)

name = "Alice"
age = 30
height = 5.6

# Basic formatting
print("Name: %s, Age: %d, Height: %.2f" % (name, age, height))

# Flags
print("Integer with padding: %05d" % 42)
print("Float with precision: %.2f" % 3.14159)

# ============================================================================
# STRING FORMATTING - .format() METHOD
# ============================================================================

print("\n" + "=" * 60)
print("STRING FORMATTING - .format() METHOD")
print("=" * 60)

# Positional arguments
print("Hello {}, you are {} years old".format("Bob", 25))

# Named arguments
print("Name: {name}, Age: {age}".format(name="Charlie", age=35))

# Index access
items = ["apple", "banana", "cherry"]
print("First: {0}, Second: {1}, Third: {2}".format(*items))

# Formatting options
print("Number: {:.2f}".format(3.14159))
print("Integer padding: {:05d}".format(42))

# ============================================================================
# STRING FORMATTING - f-strings (PREFERRED)
# ============================================================================

print("\n" + "=" * 60)
print("STRING FORMATTING - f-strings (PYTHON 3.6+)")
print("=" * 60)

name = "Diana"
age = 28
price = 19.99

# Basic f-strings
print(f"Hello {name}, you are {age} years old")

# Expressions
print(f"Next year: {age + 1}")
print(f"Price: ${price:.2f}")

# Alignment
print(f"Left: {name:<20}")
print(f"Right: {name:>20}")
print(f"Center: {name:^20}")

# ============================================================================
# STRING METHODS - CHECKING
# ============================================================================

print("\n" + "=" * 60)
print("STRING METHODS - CHECKING")
print("=" * 60)

# Check types
strings = ["abc123", "12345", "HELLO", "Hello World"]

for s in strings:
    print(f"'{s}':")
    print(f"  isalpha(): {s.isalpha()}")      # Only letters
    print(f"  isdigit(): {s.isdigit()}")      # Only digits
    print(f"  isalnum(): {s.isalnum()}")      # Letters and digits
    print(f"  isspace(): {s.isspace()}")      # Only whitespace
    print(f"  isupper(): {s.isupper()}")      # All uppercase
    print(f"  islower(): {s.islower()}")      # All lowercase

# ============================================================================
# REGULAR EXPRESSIONS BASICS
# ============================================================================

print("\n" + "=" * 60)
print("REGULAR EXPRESSIONS BASICS")
print("=" * 60)

import re

text = "My email is user@example.com and another is test@test.org"

# Find pattern
pattern = r"\w+@\w+\.\w+"
matches = re.findall(pattern, text)
print(f"Emails found: {matches}")

# Search (first match)
match = re.search(r"\d+", "The number is 42")
if match:
    print(f"Number found: {match.group()}")

# Replace
text = "I like red apples and red cars"
replaced = re.sub(r"red", "blue", text)
print(f"Original: {text}")
print(f"Replaced: {replaced}")

# Split by pattern
text = "apple,banana;cherry:date"
parts = re.split(r"[,;:]", text)
print(f"Split: {parts}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Strings are immutable sequences
2. Indexing: text[0] gets first character
3. Slicing: text[start:end:step]
4. String concatenation: str1 + str2
5. String repetition: str * n
6. Common methods: upper(), lower(), strip(), split(), join()
7. find(), count(), startswith(), endswith()
8. replace() for substitution
9. Formatting: %, .format(), f-strings (preferred)
10. Type checking: isalpha(), isdigit(), isspace(), etc.
11. Regular expressions: re module for pattern matching
12. Strings are immutable - create new instead of modifying
""")
