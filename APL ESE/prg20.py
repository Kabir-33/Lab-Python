# 20 program for demonstrating any 5 functions of set

my_set = {1, 2, 3, 4, 5}

# 1. Add an element to the set
my_set.add(6)
print("After adding 6:", my_set)

# 2. Remove an element from the set
my_set.remove(3)
print("After removing 3:", my_set)

# 3. Check if an element exists in the set
exists = 4 in my_set
print("Does 4 exist in the set?", exists)

# 4. Get the length of the set
length = len(my_set)
print("Length of the set:", length)

# 5. Perform union with another set
another_set = {4, 5, 6, 7, 8}
union_set = my_set.union(another_set)
print("Union of sets:", union_set)

# 6. Perform intersection with another set
intersection_set = my_set.intersection(another_set)
print("Intersection of sets:", intersection_set)

# 7. Perform difference with another set
difference_set = my_set.difference(another_set)
print("Difference of sets:", difference_set)
