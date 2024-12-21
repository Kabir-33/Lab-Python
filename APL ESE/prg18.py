# 18 program for demonstrating any 5 functions of string

my_string = "Hello, World!"

# 1. Find the length of the string
length = len(my_string)
print("Length of the string:", length)

# 2. Convert the string to uppercase
uppercase_string = my_string.upper()
print("Uppercase:", uppercase_string)

# 3. Replace a substring with another substring
replaced_string = my_string.replace("World", "Python")
print("Replaced string:", replaced_string)

# 4. Split the string into a list of substrings
split_string = my_string.split(", ")
print("Split string:", split_string)

# 5. Check if the string starts with a specific substring
starts_with_hello = my_string.startswith("Hello")
print("Starts with 'Hello':", starts_with_hello)
