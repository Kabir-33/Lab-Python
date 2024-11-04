import numpy as np

# Create a 4D array
array_4d = np.array([
    [[[1, 2], [3, 4]], [[5, 6], [7, 8]]],
    [[[9, 10], [11, 12]], [[13, 14], [15, 16]]]
])

print(array_4d)

# Accessing elements
print("Element at (0, 0, 0, 0):", array_4d[0, 0, 0, 0])
print("Element at (1, 1, 1, 1):", array_4d[1, 1, 1, 1])

# Get the shape of the 4D array
print("Shape of the 4D array:", array_4d.shape)

# Modify an element
array_4d[0, 0, 0, 0] = 99
print("\nModified array:")
print(array_4d)
