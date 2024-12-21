# 15 program for demonstrating any 5 functions of Array

import array as arr

my_array = arr.array('i',[1, 2, 3, 4, 5])

my_array.append(6)
print("After appending 6:", my_array)

my_array.insert(2, 99)  # Insert 99 at index 2
print("After inserting 99 at index 2:", my_array)

my_array.remove(4)
print("After removing 4:", my_array)

popped_element = my_array.pop()
print("After popping an element:", my_array)
print("Popped element:", popped_element)

index_of_99 = my_array.index(99)
print("Index of 99:", index_of_99)
