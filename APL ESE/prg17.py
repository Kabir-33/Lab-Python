# 17 program for demonstrating any 5 functions of dictionary

my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# 1. Get the value associated with a key
age = my_dict.get('age')
print("Age:", age)

# 2. Add a new key-value pair
my_dict['job'] = 'Engineer'
print("After adding job:", my_dict)

# 3. Remove a key-value pair
removed_item = my_dict.pop('city')
print("After removing city:", my_dict)
print("Removed item:", removed_item)

# 4. Get all keys in the dictionary
keys = my_dict.keys()
print("Keys:", keys)

# 5. Get all values in the dictionary
values = my_dict.values()
print("Values:", values)
