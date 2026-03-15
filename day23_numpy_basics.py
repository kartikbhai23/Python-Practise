# Day 23: NumPy arrays
# basic operations on ndarrays (super fast math vectors)

import numpy as np

# creating vectors
arr1 = np.array([1, 2, 3, 4, 5])
print("1D Vector:", arr1)
print("Type:", type(arr1))
print("Dimensions:", arr1.shape)

# 2D grid matrix
arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print("2D Matrix:\n", arr2d)
print("Dimensions:", arr2d.ndim)

# fast vectorized math
print("Vector + 10:", arr1 + 10)
print("Vector ^ 2:", arr1 ** 2)

# coordinates indexing
print("Item index 2:", arr1[2])
print("Row 0, Col 1 index:", arr2d[0, 1])

# exercise 1: 3x3 zeros array
zeros_arr = np.zeros((3, 3))
print("Zeros:\n", zeros_arr)

# exercise 2: arange with increments
range_arr = np.arange(10, 51, 5)
print("Range:", range_arr)

# challenge: calc mean/stddev on random data
np.random.seed(42)
random_data = np.random.randint(1, 100, size=10)
print("Data:", random_data)
print("Mean:", np.mean(random_data))
print("Std Deviation:", np.std(random_data))
print("Sum:", np.sum(random_data))
