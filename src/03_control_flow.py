"""
Python Control Flow Concepts

This module demonstrates:
- Conditional statements (if, elif, else)
- Loops (for, while)
- Loop control (break, continue)
- Pass statement
"""

# ============================================================================
# IF STATEMENT
# ============================================================================

print("=" * 60)
print("IF STATEMENT")
print("=" * 60)

age = 25

if age >= 18:
    print(f"Age {age}: You are an adult")

# ============================================================================
# IF-ELSE STATEMENT
# ============================================================================

print("\n" + "=" * 60)
print("IF-ELSE STATEMENT")
print("=" * 60)

score = 45

if score >= 50:
    print(f"Score {score}: Passed")
else:
    print(f"Score {score}: Failed")

# ============================================================================
# IF-ELIF-ELSE STATEMENT
# ============================================================================

print("\n" + "=" * 60)
print("IF-ELIF-ELSE STATEMENT")
print("=" * 60)

grade_score = 85

if grade_score >= 90:
    grade = "A"
elif grade_score >= 80:
    grade = "B"
elif grade_score >= 70:
    grade = "C"
elif grade_score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {grade_score}, Grade: {grade}")

# ============================================================================
# NESTED IF STATEMENTS
# ============================================================================

print("\n" + "=" * 60)
print("NESTED IF STATEMENTS")
print("=" * 60)

user_age = 22
has_license = True

if user_age >= 18:
    print(f"Age {user_age}: Adult")
    if has_license:
        print("Can drive")
    else:
        print("Cannot drive (no license)")
else:
    print(f"Age {user_age}: Minor")

# ============================================================================
# TERNARY OPERATOR (CONDITIONAL EXPRESSION)
# ============================================================================

print("\n" + "=" * 60)
print("TERNARY OPERATOR")
print("=" * 60)

number = 10
result = "Even" if number % 2 == 0 else "Odd"
print(f"{number} is {result}")

# Multiple ternary (not recommended for readability)
value = 15
category = "Positive" if value > 0 else "Zero" if value == 0 else "Negative"
print(f"{value} is {category}")

# ============================================================================
# FOR LOOP (ITERATING OVER SEQUENCES)
# ============================================================================

print("\n" + "=" * 60)
print("FOR LOOP - BASIC ITERATION")
print("=" * 60)

# Loop over a list
fruits = ["apple", "banana", "cherry"]
print("Fruits:")
for fruit in fruits:
    print(f"  - {fruit}")

# Loop with range
print("\nNumbers 0 to 4:")
for i in range(5):
    print(f"  {i}", end=" ")
print()

# Loop with range (start, stop, step)
print("\nNumbers 1 to 10 (step 2):")
for i in range(1, 11, 2):
    print(f"  {i}", end=" ")
print()

# ============================================================================
# FOR LOOP WITH ENUMERATE
# ============================================================================

print("\n" + "=" * 60)
print("FOR LOOP WITH ENUMERATE")
print("=" * 60)

colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"  Index {index}: {color}")

# Custom starting index
print("\nWith starting index 1:")
for index, color in enumerate(colors, start=1):
    print(f"  Index {index}: {color}")

# ============================================================================
# FOR LOOP WITH ZIP
# ============================================================================

print("\n" + "=" * 60)
print("FOR LOOP WITH ZIP")
print("=" * 60)

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 28]

for name, age in zip(names, ages):
    print(f"  {name}: {age} years old")

# ============================================================================
# FOR LOOP WITH DICTIONARY
# ============================================================================

print("\n" + "=" * 60)
print("FOR LOOP WITH DICTIONARY")
print("=" * 60)

student = {"name": "John", "age": 20, "grade": "A"}

# Loop over keys
print("Keys:")
for key in student:
    print(f"  {key}")

# Loop over keys and values
print("\nKey-value pairs:")
for key, value in student.items():
    print(f"  {key}: {value}")

# ============================================================================
# WHILE LOOP
# ============================================================================

print("\n" + "=" * 60)
print("WHILE LOOP")
print("=" * 60)

print("Countdown from 5:")
count = 5
while count > 0:
    print(f"  {count}")
    count -= 1
print("  Blast off!")

# ============================================================================
# WHILE LOOP WITH USER INPUT
# ============================================================================

print("\n" + "=" * 60)
print("WHILE LOOP WITH CONDITIONS")
print("=" * 60)

# Simulated condition
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    print(f"Attempt {attempts + 1} of {max_attempts}")
    attempts += 1

print("Max attempts reached")

# ============================================================================
# BREAK STATEMENT
# ============================================================================

print("\n" + "=" * 60)
print("BREAK STATEMENT - EXIT LOOP EARLY")
print("=" * 60)

print("Search for 3 in list:")
numbers = [1, 2, 3, 4, 5]
for num in numbers:
    if num == 3:
        print(f"  Found {num}!")
        break
    print(f"  Checking {num}...")

# ============================================================================
# CONTINUE STATEMENT
# ============================================================================

print("\n" + "=" * 60)
print("CONTINUE STATEMENT - SKIP TO NEXT ITERATION")
print("=" * 60)

print("Print only even numbers:")
for i in range(1, 6):
    if i % 2 != 0:
        continue  # Skip odd numbers
    print(f"  {i}")

# ============================================================================
# PASS STATEMENT
# ============================================================================

print("\n" + "=" * 60)
print("PASS STATEMENT - PLACEHOLDER")
print("=" * 60)

# Pass is a null operation - when executed, nothing happens
# Used as a placeholder when a statement is required

for i in range(3):
    pass  # Do nothing for now, implement later

print("Pass statement used as placeholder")

# ============================================================================
# ELSE WITH LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("ELSE WITH LOOPS")
print("=" * 60)

# Else executes when loop completes normally (without break)
print("For loop with else (no break):")
for i in range(3):
    print(f"  Loop iteration: {i}")
else:
    print("  Loop completed normally")

print("\nFor loop with else (with break):")
for i in range(5):
    if i == 2:
        print(f"  Breaking at i={i}")
        break
    print(f"  Loop iteration: {i}")
else:
    print("  This won't print (loop was broken)")

# ============================================================================
# NESTED LOOPS
# ============================================================================

print("\n" + "=" * 60)
print("NESTED LOOPS")
print("=" * 60)

print("Multiplication table (3x3):")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"  {i}*{j}={i*j}", end="  ")
    print()

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. if: Execute code if condition is True
2. elif: Additional conditions
3. else: Execute if all conditions are False
4. for: Loop over sequences (iterable)
5. while: Loop while condition is True
6. break: Exit loop immediately
7. continue: Skip to next iteration
8. pass: Placeholder (does nothing)
9. else with loops: Executes when loop completes normally
10. Use range(start, stop, step) for numeric sequences
11. Use enumerate() to get index and value
12. Use zip() to combine multiple sequences
""")
