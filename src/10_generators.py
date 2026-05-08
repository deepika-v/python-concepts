"""
Python Generators Concepts

This module demonstrates:
- Generator functions (yield)
- Generator expressions
- Generator advantages (memory efficiency)
- Sending values to generators
- Generator methods
"""

# ============================================================================
# BASIC GENERATOR
# ============================================================================

print("=" * 60)
print("BASIC GENERATOR")
print("=" * 60)

def simple_generator():
    """A simple generator that yields values."""
    print("Generator started")
    yield 1
    print("Between first and second")
    yield 2
    print("Between second and third")
    yield 3
    print("Generator finished")

# Create generator object
gen = simple_generator()
print(f"Generator object: {gen}")
print(f"Type: {type(gen)}")

# Get values from generator
print("\nGetting values:")
print(f"First: {next(gen)}")
print(f"Second: {next(gen)}")
print(f"Third: {next(gen)}")

# This would raise StopIteration
try:
    print(f"Fourth: {next(gen)}")
except StopIteration:
    print("No more values - StopIteration raised")

# ============================================================================
# GENERATOR WITH FOR LOOP
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR WITH FOR LOOP")
print("=" * 60)

def count_up(n):
    """Generator that counts up to n."""
    i = 1
    while i <= n:
        yield i
        i += 1

print("Using for loop:")
for num in count_up(5):
    print(f"  {num}")

# ============================================================================
# RANGE ALTERNATIVE WITH GENERATOR
# ============================================================================

print("\n" + "=" * 60)
print("RANGE ALTERNATIVE WITH GENERATOR")
print("=" * 60)

def my_range(start, end, step=1):
    """Generator that works like range()."""
    current = start
    while current < end:
        yield current
        current += step

print("Using my_range(2, 10, 2):")
for num in my_range(2, 10, 2):
    print(f"  {num}")

# ============================================================================
# GENERATOR EXPRESSIONS
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR EXPRESSIONS")
print("=" * 60)

# List comprehension (creates full list in memory)
list_comp = [x ** 2 for x in range(5)]
print(f"List comprehension: {list_comp}")

# Generator expression (memory efficient)
gen_exp = (x ** 2 for x in range(5))
print(f"Generator expression: {gen_exp}")

# Convert to list to see values
print(f"Generator values: {list(gen_exp)}")

# ============================================================================
# FIBONACCI GENERATOR
# ============================================================================

print("\n" + "=" * 60)
print("FIBONACCI GENERATOR")
print("=" * 60)

def fibonacci(n):
    """Generate fibonacci sequence up to n terms."""
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("First 10 fibonacci numbers:")
fib_list = list(fibonacci(10))
print(fib_list)

# ============================================================================
# MEMORY EFFICIENCY COMPARISON
# ============================================================================

print("\n" + "=" * 60)
print("MEMORY EFFICIENCY COMPARISON")
print("=" * 60)

import sys

# List comprehension
large_list = [x ** 2 for x in range(1000000)]
print(f"List size: {sys.getsizeof(large_list)} bytes")

# Generator expression
large_gen = (x ** 2 for x in range(1000000))
print(f"Generator size: {sys.getsizeof(large_gen)} bytes")

# ============================================================================
# SENDING VALUES TO GENERATOR
# ============================================================================

print("\n" + "=" * 60)
print("SENDING VALUES TO GENERATOR")
print("=" * 60)

def echo_generator():
    """Generator that receives and yields values."""
    value = None
    while True:
        value = yield value
        print(f"Received: {value}")

gen = echo_generator()
next(gen)  # Prime the generator (move to first yield)

print("Sending values:")
print(f"Sent 'Hello': {gen.send('Hello')}")
print(f"Sent 'World': {gen.send('World')}")

# ============================================================================
# GENERATOR WITH CONDITION
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR WITH CONDITION")
print("=" * 60)

def even_numbers(start, end):
    """Generator that yields only even numbers."""
    for num in range(start, end):
        if num % 2 == 0:
            yield num

print("Even numbers from 1 to 20:")
evens = list(even_numbers(1, 20))
print(evens)

# ============================================================================
# INFINITE GENERATOR
# ============================================================================

print("\n" + "=" * 60)
print("INFINITE GENERATOR")
print("=" * 60)

def infinite_counter(start=0):
    """Infinite generator - counts forever."""
    num = start
    while True:
        yield num
        num += 1

# Use itertools.islice to limit output
from itertools import islice

print("First 5 numbers from infinite counter:")
counter = infinite_counter()
first_five = islice(counter, 5)
print(list(first_five))

# ============================================================================
# GENERATOR WITH FILE READING
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR WITH FILE READING (EXAMPLE)")
print("=" * 60)

def read_file_lines(filename):
    """Generator that reads file line by line."""
    try:
        with open(filename, 'r') as f:
            for line in f:
                yield line.strip()
    except FileNotFoundError:
        print(f"File '{filename}' not found")

# Create a sample file
with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")

print("Reading lines from file:")
for line in read_file_lines("sample.txt"):
    print(f"  {line}")

# ============================================================================
# GENERATOR CHAINING
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR CHAINING")
print("=" * 60)

def gen1():
    """First generator."""
    for i in range(3):
        print(f"gen1 yielding {i}")
        yield i

def gen2():
    """Second generator."""
    for i in range(3, 6):
        print(f"gen2 yielding {i}")
        yield i

def chained():
    """Chain two generators."""
    yield from gen1()
    yield from gen2()

print("Chained generators:")
for value in chained():
    print(f"  Received: {value}")

# ============================================================================
# GENERATOR WITH CLOSE() AND THROW()
# ============================================================================

print("\n" + "=" * 60)
print("GENERATOR METHODS: close() AND throw()")
print("=" * 60)

def cleanup_generator():
    """Generator with cleanup."""
    print("Initializing")
    try:
        yield "Value 1"
        yield "Value 2"
    finally:
        print("Cleanup!")

print("Using close():")
gen = cleanup_generator()
print(next(gen))
gen.close()

print("\nUsing throw():")
gen = cleanup_generator()
print(next(gen))
try:
    gen.throw(ValueError, "An error occurred")
except ValueError as e:
    print(f"Caught: {e}")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. yield: Keyword that turns function into generator
2. Generator: Iterator that produces values lazily
3. next(): Get next value from generator (raises StopIteration at end)
4. Generator expression: (expr for item in iterable)
5. Memory efficient: Only stores current state, not entire sequence
6. Infinite generators: Useful with itertools.islice()
7. send(): Send values into generator
8. close(): Stop generator and trigger finally block
9. throw(): Send exception into generator
10. yield from: Delegate to sub-generator
11. Use cases: Reading large files, infinite sequences, pipelines
12. For loops automatically handle StopIteration
""")
