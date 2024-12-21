# 16 program for demonstrating any 5 functions of list

my_list = [1, 2, 3, 4, 5, 1]

my_list.append(6)

my_list.insert(2, 99)  # Insert 99 at index 2
print("After inserting 99 at index 2:", my_list)

my_list.remove(4)
print("After removing 4:", my_list)

popped_element = my_list.pop()
print("After popping an element:", my_list)
print("Popped element:", popped_element)

index_of_99 = my_list.index(99)
print("Index of 99:", index_of_99)

counter=my_list.count(1)
print("How many times 1 occur :",counter,"times")