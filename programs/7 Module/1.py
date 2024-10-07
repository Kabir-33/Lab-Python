import os 
with open('Sample.txt','w') as file:
    file.write("This is a File")

os.remove('Sample.txt')
print("File 'Sample.txt' deleted")

# we can also write like this also 
# os.unlink('Sample.txt')