# 4. program to read the contents from a file and display on console

file_path="example.txt"

with open(file_path, 'r') as file:
    contents=file.read()

print(contents)