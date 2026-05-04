# NumPy Introduction and Operations

import numpy as np

print("========== NUMPY ARRAYS ==========\n")

# Creating array object
arr = np.array([[1, 2, 3],
                [4, 2, 5]])

print("Array:")
print(arr)

# Printing type of arr object
print("\nArray is of type:", type(arr))

# Printing array dimensions
print("No. of dimensions:", arr.ndim)

# Printing shape of array
print("Shape of array:", arr.shape)

# Printing size of array
print("Size of array:", arr.size)

# Printing type of elements
print("Array stores elements of type:", arr.dtype)

print("\n========== ARRAY CREATION ==========\n")

# Creating array from list with float type
a = np.array([[1, 2, 4],
              [5, 8, 7]], dtype='float')

print("Array created using passed list:")
print(a)

# Creating array from tuple
b = np.array((1, 3, 2))

print("\nArray created using passed tuple:")
print(b)

print("\n========== ARRAY INDEXING ==========\n")

# Creating a 2D array
index_arr = np.array([[1, 2, 3],
                      [4, 5, 6],
                      [7, 8, 9]])

print("Original array:")
print(index_arr)

# Accessing element
print("\nElement at row 1, column 2:")
print(index_arr[1, 2])

print("\n========== ARRAY MANIPULATION ==========\n")

# Create 1D array
manip_arr = np.array([1, 2, 3, 4, 5])

# Add 10 to each element
arr_add = manip_arr + 10

# Multiply each element by 2
arr_mul = manip_arr * 2

print("Original array:", manip_arr)
print("Array after adding 10:", arr_add)
print("Array after multiplying by 2:", arr_mul)

print("\n========== NUMPY BROADCASTING ==========\n")

# Create matrix
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# Create 1D array
B = np.array([1, 2, 3])

# Broadcasting
C = A + B

print("Matrix A:")
print(A)

print("\nArray B:")
print(B)

print("\nResult of A + B:")
print(C)