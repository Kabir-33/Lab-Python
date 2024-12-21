# 24 program for use of Numpy library

import numpy as np

# Create a NumPy array from a list
array_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", array_from_list)

# Create an array of zeros
zeros_array = np.zeros(5)
print("Array of zeros:", zeros_array)

# Create an array of ones
ones_array = np.ones(5)
print("Array of ones:", ones_array)

# Create an array with a range of values
range_array = np.arange(10)
print("Array with range of values:", range_array)

# Perform element-wise addition
array_sum = array_from_list + range_array[:5]
print("Sum of arrays:", array_sum)

# Perform element-wise multiplication
array_product = array_from_list * 2
print("Element-wise multiplication:", array_product)
