# 19 program for demonstrating any 5 functions of tuple

my_tuple = (1, 2, 3, 4, 5, 3)

# 1. Access an element by index
element = my_tuple[2]
print("Element at index 2:", element)

# 2. Count occurrences of an element
count = my_tuple.count(3)
print("Count of element 3:", count)

# 3. Find the index of an element
index = my_tuple.index(4)
print("Index of element 4:", index)

# 4. Check if an element exists in the tuple
exists = 5 in my_tuple
print("Does 5 exist in the tuple?", exists)

# 5. Get the length of the tuple
length = len(my_tuple)
print("Length of the tuple:", length)

# 6. Concatenate two tuples
new_tuple = my_tuple + (6, 7, 8)
print("Concatenated tuple:", new_tuple)

# 7. Slice the tuple
slice_tuple = my_tuple[1:4]
print("Sliced tuple (from index 1 to 3):", slice_tuple)
