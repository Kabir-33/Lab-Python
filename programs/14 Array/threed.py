import numpy as np
# 3D array
array_3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# O/p  : [[[ 1  2  3]
# [ 4  5  6]]

# [[ 7  8  9]
#  [10 11 12]]]

print(array_3d)
print("Element at (0, 0, 0):", array_3d[0, 1, 0])   # 4
print("Element at (1, 1, 2):", array_3d[1, 1, 2])   # 12


array_3d[0, 0, 0] = 25
print("\nModified array:")          # 1 is changed as 25 the whole remains same
print(array_3d)


print("\nIterating through 3D array:")
for matrix in array_3d:
    for row in matrix:
        for element in row:
            print(element, end=' ')
    print()
