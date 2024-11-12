file = open('E:\Python\PY lab\programs\18 File Handling','r')

for each in file:
    print(each)

print(file.read())    

with open('file1.txt' ) as file:
    data = file.read()

print(data)

