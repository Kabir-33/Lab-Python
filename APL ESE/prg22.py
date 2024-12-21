# 22 program for Creating a new package for addition and multiplication operation and use it in another program.

# main.py
# first create seperate folder 
# add now create basic function in it ... refer mymath folder

from mymath.operations import add, multiply

# Using the add function
result_add = add(2, 3)
print("Result of addition:", result_add)

# Using the multiply function
result_multiply = multiply(2, 3)
print("Result of multiplication:", result_multiply)
