"""
NumPy Advanced Operations Demo

This module demonstrates advanced NumPy concepts:
- Advanced indexing and fancy indexing
- Broadcasting rules
- Universal functions (ufuncs)
- Structured arrays
- Memory layout and performance
- Random number generation
"""

import numpy as np
import time

# ============================================================================
# FANCY INDEXING
# ============================================================================

print("=" * 60)
print("FANCY INDEXING")
print("=" * 60)

# Create sample array
arr = np.arange(20)
print(f"Original array: {arr}")

# Fancy indexing with integer arrays
indices = [2, 5, 8, 11, 14]
fancy_result = arr[indices]
print(f"Fancy indexing [2,5,8,11,14]: {fancy_result}")

# Multiple fancy indexing
rows = np.array([0, 1, 2])
cols = np.array([0, 2, 4])
matrix = np.arange(15).reshape(3, 5)
print(f"\nMatrix:\n{matrix}")
print(f"Elements at (rows, cols): {matrix[rows, cols]}")

# Boolean indexing
bool_mask = arr > 10
print(f"\nBoolean mask (arr > 10): {bool_mask}")
print(f"Elements where arr > 10: {arr[bool_mask]}")

# Combined indexing
combined = arr[(arr > 5) & (arr < 15)]
print(f"Elements 5 < x < 15: {combined}")

# ============================================================================
# ADVANCED BROADCASTING
# ============================================================================

print("\n" + "=" * 60)
print("ADVANCED BROADCASTING")
print("=" * 60)

# Broadcasting rules demonstration
print("Broadcasting Rules:")
print("1. If arrays have different dimensions, pad with 1s on the left")
print("2. If dimensions don't match, one of them must be 1")
print("3. Result has maximum of each dimension")

# Example 1: Scalar broadcasting
scalar = 5
vector = np.array([1, 2, 3, 4])
result = scalar + vector
print(f"\nScalar + Vector: {scalar} + {vector} = {result}")

# Example 2: Different shapes
A = np.array([[1], [2], [3]])  # Shape (3, 1)
B = np.array([10, 20, 30])     # Shape (3,)
result = A + B
print(f"\nMatrix + Vector:\n{A} +\n{B} =\n{result}")

# Example 3: Outer product
x = np.array([1, 2, 3])  # Shape (3,)
y = np.array([4, 5])     # Shape (2,)
result = x[:, np.newaxis] + y  # Broadcasting
print(f"\nOuter sum:\n{result}")

# ============================================================================
# UNIVERSAL FUNCTIONS (UFUNCS)
# ============================================================================

print("\n" + "=" * 60)
print("UNIVERSAL FUNCTIONS (UFUNCS)")
print("=" * 60)

# Ufuncs are vectorized functions that operate element-wise
x = np.array([1, 2, 3, 4, 5])
y = np.array([0.1, 0.2, 0.3, 0.4, 0.5])

print(f"x: {x}")
print(f"y: {y}")

# Arithmetic ufuncs
print(f"\nArithmetic:")
print(f"  x + y: {x + y}")
print(f"  x - y: {x - y}")
print(f"  x * y: {x * y}")
print(f"  x / y: {x / y}")
print(f"  x // y: {x // y}")  # Floor division
print(f"  x % y: {x % y}")    # Modulo
print(f"  x ** y: {x ** y}")  # Power

# Trigonometric functions
angles = np.array([0, np.pi/4, np.pi/2, np.pi])
print(f"\nTrigonometric (angles in radians): {angles}")
print(f"  sin: {np.sin(angles)}")
print(f"  cos: {np.cos(angles)}")
print(f"  tan: {np.tan(angles)}")

# Exponential and logarithmic
values = np.array([1, 2, np.e, 10])
print(f"\nExponential/Logarithmic: {values}")
print(f"  exp: {np.exp(values)}")
print(f"  log: {np.log(values)}")
print(f"  log10: {np.log10(values)}")

# Aggregation functions
data = np.random.randn(1000)
print(f"\nAggregation on 1000 random numbers:")
print(f"  sum: {np.sum(data):.4f}")
print(f"  mean: {np.mean(data):.4f}")
print(f"  std: {np.std(data):.4f}")
print(f"  min: {np.min(data):.4f}")
print(f"  max: {np.max(data):.4f}")

# ============================================================================
# STRUCTURED ARRAYS
# ============================================================================

print("\n" + "=" * 60)
print("STRUCTURED ARRAYS")
print("=" * 60)

# Define structured array dtype
employee_dtype = np.dtype([
    ('name', 'U20'),      # Unicode string, max 20 chars
    ('age', 'i4'),        # 4-byte integer
    ('salary', 'f8'),     # 8-byte float
    ('department', 'U15') # Unicode string, max 15 chars
])

# Create structured array
employees = np.array([
    ('Alice', 30, 50000.0, 'Engineering'),
    ('Bob', 25, 45000.0, 'Sales'),
    ('Charlie', 35, 60000.0, 'Marketing'),
    ('Diana', 28, 52000.0, 'Engineering')
], dtype=employee_dtype)

print("Employee structured array:")
print(employees)

# Access fields
print(f"\nNames: {employees['name']}")
print(f"Ages: {employees['age']}")
print(f"Salaries: {employees['salary']}")

# Conditional access
engineering = employees[employees['department'] == 'Engineering']
print(f"\nEngineering employees:\n{engineering}")

# Calculate statistics
avg_salary = np.mean(employees['salary'])
print(f"Average salary: ${avg_salary:.2f}")

# ============================================================================
# MEMORY LAYOUT AND PERFORMANCE
# ============================================================================

print("\n" + "=" * 60)
print("MEMORY LAYOUT AND PERFORMANCE")
print("=" * 60)

# Create large arrays
size = 10000

# C-order (row-major) vs F-order (column-major)
print("Memory layout comparison:")

# C-order array
arr_c = np.arange(size * size, dtype=np.float64).reshape(size, size)
print(f"C-order array shape: {arr_c.shape}, flags.C_CONTIGUOUS: {arr_c.flags.c_contiguous}")

# F-order array
arr_f = np.arange(size * size, dtype=np.float64).reshape(size, size, order='F')
print(f"F-order array shape: {arr_f.shape}, flags.F_CONTIGUOUS: {arr_f.flags.f_contiguous}")

# Performance test: row-wise vs column-wise access
def time_access(arr, order_name):
    start = time.time()
    if order_name == 'C':
        # Row-wise access (good for C-order)
        for i in range(size):
            row_sum = np.sum(arr[i, :])
    else:
        # Column-wise access (good for F-order)
        for j in range(size):
            col_sum = np.sum(arr[:, j])
    end = time.time()
    return end - start

c_time = time_access(arr_c, 'C')
f_time = time_access(arr_f, 'F')

print(f"\nPerformance test ({size}x{size} array):")
print(f"C-order array, row access: {c_time:.4f} seconds")
print(f"F-order array, column access: {f_time:.4f} seconds")

# ============================================================================
# RANDOM NUMBER GENERATION
# ============================================================================

print("\n" + "=" * 60)
print("RANDOM NUMBER GENERATION")
print("=" * 60)

# Set seed for reproducibility
np.random.seed(42)

# Uniform random numbers
uniform = np.random.rand(5)
print(f"Uniform [0,1): {uniform}")

# Normal distribution
normal = np.random.randn(5)
print(f"Normal (μ=0, σ=1): {normal}")

# Integers in range
integers = np.random.randint(1, 100, 5)
print(f"Random integers [1,100): {integers}")

# Choice from array
colors = ['red', 'blue', 'green', 'yellow']
chosen = np.random.choice(colors, size=3, replace=True)
print(f"Random choice from {colors}: {chosen}")

# Shuffle array
arr = np.arange(10)
print(f"Original array: {arr}")
np.random.shuffle(arr)
print(f"After shuffle: {arr}")

# ============================================================================
# ADVANCED ARRAY OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("ADVANCED ARRAY OPERATIONS")
print("=" * 60)

# Meshgrid for coordinate matrices
x = np.linspace(-5, 5, 5)
y = np.linspace(-3, 3, 4)
X, Y = np.meshgrid(x, y)
print(f"X coordinates:\n{X}")
print(f"Y coordinates:\n{Y}")

# Vectorized conditional operations
arr = np.random.randn(10)
print(f"\nArray: {arr}")
print(f"Where positive: {np.where(arr > 0, arr, 0)}")
print(f"Where negative: {np.where(arr < 0, arr, 0)}")

# Clip values
clipped = np.clip(arr, -1, 1)
print(f"Clipped to [-1, 1]: {clipped}")

# Unique values and counts
data = np.random.randint(1, 6, 20)  # Dice rolls
unique_vals, counts = np.unique(data, return_counts=True)
print(f"\nDice rolls: {data}")
print(f"Unique values: {unique_vals}")
print(f"Counts: {counts}")

# Cumulative operations
arr = np.arange(1, 6)
print(f"\nArray: {arr}")
print(f"Cumulative sum: {np.cumsum(arr)}")
print(f"Cumulative product: {np.cumprod(arr)}")

# ============================================================================
# PERFORMANCE OPTIMIZATION TIPS
# ============================================================================

print("\n" + "=" * 60)
print("PERFORMANCE OPTIMIZATION TIPS")
print("=" * 60)

print("""
1. Use vectorized operations instead of loops
2. Choose appropriate data types (int32 vs int64, float32 vs float64)
3. Use in-place operations when possible (arr += 1 instead of arr = arr + 1)
4. Consider memory layout (C-order vs F-order) for access patterns
5. Use np.where() for conditional operations instead of loops
6. Leverage broadcasting to avoid unnecessary array creation
7. Use views instead of copies when possible
8. Consider using numba for extremely performance-critical sections
9. Profile your code with timeit or cProfile to identify bottlenecks
10. Use appropriate algorithms for large datasets (consider dask for very large arrays)
""")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. Fancy indexing: Use arrays of indices for complex selections
2. Broadcasting: Automatic expansion of arrays for operations
3. Ufuncs: Vectorized functions for element-wise operations
4. Structured arrays: Arrays with named fields (like database records)
5. Memory layout: C-order (row-major) vs F-order (column-major)
6. Random generation: Comprehensive random number capabilities
7. Advanced operations: meshgrid, where, clip, unique, cumsum
8. Performance: Vectorization, appropriate dtypes, memory layout awareness
9. NumPy ecosystem: Integrates with SciPy, pandas, matplotlib, etc.
10. Best practices: Use vectorized operations, choose right dtypes, profile code
""")
