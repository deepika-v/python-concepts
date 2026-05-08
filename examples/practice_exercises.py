"""
Practice Exercises for Python Concepts

This module contains exercises to practice various Python concepts.
Uncomment exercises and try solving them!
"""

# ============================================================================
# EXERCISE 1: BASIC CALCULATIONS
# ============================================================================

print("=" * 60)
print("EXERCISE 1: BASIC CALCULATIONS")
print("=" * 60)

# TODO: Write a program that:
# 1. Takes two numbers as input (use hardcoded values)
# 2. Calculates and prints their sum, difference, product, division
# 3. Also print remainder and exponentiation

# Solution
def exercise1():
    a, b = 10, 3
    print(f"a = {a}, b = {b}")
    print(f"Sum: {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product: {a * b}")
    print(f"Division: {a / b}")
    print(f"Remainder: {a % b}")
    print(f"Exponentiation: {a ** b}")

exercise1()

# ============================================================================
# EXERCISE 2: STRING REVERSAL AND MANIPULATION
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 2: STRING REVERSAL AND MANIPULATION")
print("=" * 60)

# TODO: Write a function that:
# 1. Takes a string as input
# 2. Returns the string reversed
# 3. Returns the string in uppercase
# 4. Returns the length of the string

# Solution
def string_operations(text):
    reversed_text = text[::-1]
    uppercase = text.upper()
    length = len(text)
    return reversed_text, uppercase, length

text = "python"
reversed_t, upper_t, len_t = string_operations(text)
print(f"Original: {text}")
print(f"Reversed: {reversed_t}")
print(f"Uppercase: {upper_t}")
print(f"Length: {len_t}")

# ============================================================================
# EXERCISE 3: LIST OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 3: LIST OPERATIONS")
print("=" * 60)

# TODO: Write a function that:
# 1. Takes a list of numbers
# 2. Returns the sum, average, max, min

# Solution
def list_statistics(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return total, average, maximum, minimum

numbers = [10, 20, 30, 40, 50]
total, avg, max_val, min_val = list_statistics(numbers)
print(f"Numbers: {numbers}")
print(f"Sum: {total}")
print(f"Average: {avg}")
print(f"Max: {max_val}")
print(f"Min: {min_val}")

# ============================================================================
# EXERCISE 4: FIBONACCI SEQUENCE
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 4: FIBONACCI SEQUENCE")
print("=" * 60)

# TODO: Write a function that generates the first n Fibonacci numbers

# Solution
def fibonacci(n):
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence

fib_sequence = fibonacci(10)
print(f"First 10 Fibonacci numbers: {fib_sequence}")

# ============================================================================
# EXERCISE 5: PALINDROME CHECK
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 5: PALINDROME CHECK")
print("=" * 60)

# TODO: Write a function that checks if a string is a palindrome
# (reads the same forwards and backwards)

# Solution
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

test_strings = ["racecar", "hello", "A man a plan a canal Panama"]
for s in test_strings:
    result = is_palindrome(s)
    print(f"'{s}' is palindrome: {result}")

# ============================================================================
# EXERCISE 6: PRIME NUMBER CHECKER
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 6: PRIME NUMBER CHECKER")
print("=" * 60)

# TODO: Write a function that checks if a number is prime

# Solution
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [2, 3, 4, 5, 10, 17, 20, 23]
primes = [n for n in numbers if is_prime(n)]
print(f"Numbers: {numbers}")
print(f"Primes: {primes}")

# ============================================================================
# EXERCISE 7: DICTIONARY OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 7: DICTIONARY OPERATIONS")
print("=" * 60)

# TODO: Create a dictionary of students with their grades
# and write functions to:
# 1. Find the student with highest grade
# 2. Calculate class average

# Solution
def student_stats(grades_dict):
    highest_student = max(grades_dict, key=grades_dict.get)
    highest_grade = grades_dict[highest_student]
    average = sum(grades_dict.values()) / len(grades_dict)
    return highest_student, highest_grade, average

students = {"Alice": 95, "Bob": 87, "Charlie": 92, "Diana": 88}
top_student, top_grade, avg = student_stats(students)
print(f"Students: {students}")
print(f"Top student: {top_student} ({top_grade})")
print(f"Class average: {avg:.2f}")

# ============================================================================
# EXERCISE 8: LIST COMPREHENSION
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 8: LIST COMPREHENSION")
print("=" * 60)

# TODO: Use list comprehensions to:
# 1. Create a list of squares of numbers 1-10
# 2. Create a list of even numbers 0-20
# 3. Create a list of words capitalized

# Solution
squares = [x**2 for x in range(1, 11)]
evens = [x for x in range(0, 21) if x % 2 == 0]
words = ["hello", "world", "python"]
capitalized = [w.capitalize() for w in words]

print(f"Squares (1-10): {squares}")
print(f"Evens (0-20): {evens}")
print(f"Capitalized: {capitalized}")

# ============================================================================
# EXERCISE 9: SORTING
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 9: SORTING")
print("=" * 60)

# TODO: Sort lists and dictionaries in different ways

# Solution
numbers = [5, 2, 8, 1, 9, 3]
print(f"Original: {numbers}")
print(f"Sorted ascending: {sorted(numbers)}")
print(f"Sorted descending: {sorted(numbers, reverse=True)}")

# Sort dictionary by value
scores = {"Alice": 95, "Bob": 87, "Charlie": 92}
sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(f"\nScores sorted by value:")
for name, score in sorted_scores:
    print(f"  {name}: {score}")

# ============================================================================
# EXERCISE 10: COUNTING OCCURRENCES
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISE 10: COUNTING OCCURRENCES")
print("=" * 60)

# TODO: Write a function that counts character occurrences

# Solution
def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char.isalpha():
            char_count[char] = char_count.get(char, 0) + 1
    return char_count

text = "programming"
char_freq = count_characters(text)
print(f"Text: '{text}'")
print(f"Character frequency: {char_freq}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("EXERCISES COMPLETED!")
print("=" * 60)
print("""
Try modifying these exercises:
1. Add more test cases
2. Add error handling
3. Make functions more efficient
4. Add type hints
5. Create classes to organize related functions
""")
