# 5. program to read the contents from a one file and write into another file


source_file_path = 'source.txt'  

destination_file_path = 'destination.txt'  

with open(source_file_path, 'r') as source_file:
    contents = source_file.read()

with open(destination_file_path, 'w') as destination_file:
    destination_file.write(contents)

print("Contents have been successfully copied from", source_file_path, "to", destination_file_path)
