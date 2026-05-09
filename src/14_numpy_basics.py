"""
Python NumPy Concepts

This module demonstrates NumPy fundamentals:
- Arrays and array operations
- Array creation and manipulation
- Mathematical operations
- Indexing and slicing
- Broadcasting
- Statistical functions
- Linear algebra basics
"""

import numpy as np

# ============================================================================
# ARRAY CREATION
# ============================================================================

print("=" * 60)
print("NUMPY ARRAY CREATION")
print("=" * 60)

# From Python lists
list_data = [1, 2, 3, 4, 5]
arr1 = np.array(list_data)
print(f"From list: {arr1}, Type: {type(arr1)}, dtype: {arr1.dtype}")

# 2D array from nested lists
matrix_data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
arr2d = np.array(matrix_data)
print(f"2D array:\n{arr2d}")
print(f"Shape: {arr2d.shape}, Dimensions: {arr2d.ndim}")

# Special arrays
zeros = np.zeros((3, 4))
ones = np.ones((2, 3))
identity = np.eye(4)
random_arr = np.random.rand(3, 3)

print(f"\nZeros array:\n{zeros}")
print(f"Ones array:\n{ones}")
print(f"Identity matrix:\n{identity}")
print(f"Random array:\n{random_arr}")

# ============================================================================
# ARRAY PROPERTIES
# ============================================================================

print("\n" + "=" * 60)
print("ARRAY PROPERTIES")
print("=" * 60)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(f"Array:\n{arr}")
print(f"Shape: {arr.shape}")
print(f"Size: {arr.size}")
print(f"Data type: {arr.dtype}")
print(f"Number of dimensions: {arr.ndim}")
print(f"Item size (bytes): {arr.itemsize}")
print(f"Total bytes: {arr.nbytes}")

# ============================================================================
# ARRAY INDEXING AND SLICING
# ============================================================================

print("\n" + "=" * 60)
print("ARRAY INDEXING AND SLICING")
print("=" * 60)

arr = np.arange(12).reshape(3, 4)
print(f"Original array:\n{arr}")

# Basic indexing
print(f"Element at [1, 2]: {arr[1, 2]}")

# Row slicing
print(f"First row: {arr[0, :]}")
print(f"Last row: {arr[-1, :]}")

# Column slicing
print(f"Second column: {arr[:, 1]}")

# Subarray slicing
print(f"Top-left 2x2:\n{arr[:2, :2]}")
print(f"Bottom-right 2x2:\n{arr[1:, 2:]}")

# ============================================================================
# ARRAY OPERATIONS
# ============================================================================

print("\n" + "=" * 60)
print("ARRAY OPERATIONS")
print("=" * 60)

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(f"a: {a}")
print(f"b: {b}")

# Element-wise operations
print(f"a + b: {a + b}")
print(f"a - b: {a - b}")
print(f"a * b: {a * b}")
print(f"a / b: {a / b}")
print(f"a ** 2: {a ** 2}")

# Mathematical functions
print(f"sin(a): {np.sin(a)}")
print(f"sqrt(a): {np.sqrt(a)}")
print(f"exp(a): {np.exp(a)}")

# ============================================================================
# BROADCASTING
# ============================================================================

print("\n" + "=" * 60)
print("BROADCASTING")
print("=" * 60)

# Broadcasting allows operations between arrays of different shapes
arr = np.array([[1, 2, 3], [4, 5, 6]])
scalar = 10

print(f"Array:\n{arr}")
print(f"Scalar: {scalar}")
print(f"Array + scalar:\n{arr + scalar}")

# Broadcasting with different shapes
arr1 = np.array([[1], [2], [3]])  # Shape (3, 1)
arr2 = np.array([10, 20, 30])     # Shape (3,)

print(f"\narr1 shape {arr1.shape}:\n{arr1}")
print(f"arr2 shape {arr2.shape}: {arr2}")
print(f"arr1 + arr2:\n{arr1 + arr2}")

# ============================================================================
# STATISTICAL FUNCTIONS
# ============================================================================

print("\n" + "=" * 60)
print("STATISTICAL FUNCTIONS")
print("=" * 60)

data = np.random.randn(1000)  # 1000 random numbers

print(f"Mean: {np.mean(data):.4f}")
print(f"Median: {np.median(data):.4f}")
print(f"Standard deviation: {np.std(data):.4f}")
print(f"Variance: {np.var(data):.4f}")
print(f"Min: {np.min(data):.4f}")
print(f"Max: {np.max(data):.4f}")
print(f"25th percentile: {np.percentile(data, 25):.4f}")
print(f"75th percentile: {np.percentile(data, 75):.4f}")

# ============================================================================
# LINEAR ALGEBRA BASICS
# ============================================================================

print("\n" + "=" * 60)
print("LINEAR ALGEBRA BASICS")
print("=" * 60)

# Matrix multiplication
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print(f"A:\n{A}")
print(f"B:\n{B}")
print(f"A @ B (matrix multiplication):\n{A @ B}")
print(f"np.dot(A, B):\n{np.dot(A, B)}")

# Transpose
print(f"A transpose:\n{A.T}")

# Determinant
det_A = np.linalg.det(A)
print(f"Determinant of A: {det_A}")

# Inverse (if determinant != 0)
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print(f"Inverse of A:\n{inv_A}")
    print(f"A @ inv(A):\n{A @ inv_A}")  # Should be identity matrix

# ============================================================================
# ARRAY MANIPULATION
# ============================================================================

print("\n" + "=" * 60)
print("ARRAY MANIPULATION")
print("=" * 60)

arr = np.arange(12)
print(f"Original: {arr}")

# Reshaping
reshaped = arr.reshape(3, 4)
print(f"Reshaped to 3x4:\n{reshaped}")

# Flattening
flattened = reshaped.flatten()
print(f"Flattened: {flattened}")

# Concatenation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
concatenated = np.concatenate([a, b])
print(f"Concatenated: {concatenated}")

# Stacking
stacked_v = np.vstack([a, b])  # Vertical stack
stacked_h = np.hstack([a, b])  # Horizontal stack
print(f"Vertical stack:\n{stacked_v}")
print(f"Horizontal stack: {stacked_h}")

# ============================================================================
# BOOLEAN INDEXING AND MASKING
# ============================================================================

print("\n" + "=" * 60)
print("BOOLEAN INDEXING AND MASKING")
print("=" * 60)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(f"Array: {arr}")

# Boolean mask
mask = arr > 5
print(f"Mask (arr > 5): {mask}")
print(f"Elements > 5: {arr[mask]}")

# Multiple conditions
mask2 = (arr >= 3) & (arr <= 7)
print(f"Elements between 3 and 7: {arr[mask2]}")

# Conditional assignment
arr_copy = arr.copy()
arr_copy[arr_copy % 2 == 0] = -1  # Replace even numbers with -1
print(f"After replacing evens with -1: {arr_copy}")

# ============================================================================
# PERFORMANCE COMPARISON
# ============================================================================

print("\n" + "=" * 60)
print("PERFORMANCE COMPARISON")
print("=" * 60)

import time

# Large arrays
size = 1000000
python_list = list(range(size))
numpy_array = np.arange(size)

# Python list operation
start = time.time()
python_result = [x * 2 for x in python_list]
python_time = time.time() - start

# NumPy array operation
start = time.time()
numpy_result = numpy_array * 2
numpy_time = time.time() - start

print(f"Python list time: {python_time:.4f} seconds")
print(f"NumPy array time: {numpy_time:.4f} seconds")
print(f"NumPy is {python_time/numpy_time:.1f}x faster")

# ============================================================================
# SUMMARY
# ============================================================================

print("\n" + "=" * 60)
print("KEY TAKEAWAYS")
print("=" * 60)
print("""
1. NumPy arrays are faster and more memory-efficient than Python lists
2. Arrays have fixed data types and support vectorized operations
3. Broadcasting allows operations between arrays of different shapes
4. Rich set of mathematical and statistical functions
5. Powerful indexing and slicing capabilities
6. Linear algebra operations built-in
7. Boolean indexing for conditional operations
8. Easy array manipulation (reshape, concatenate, stack)
9. Use np.arange() for sequences, np.zeros/ones/eye() for special arrays
10. Vectorized operations are preferred over loops for performance
""")
