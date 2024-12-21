# 6. program to display file available in current directory

import os
current_directory = os.getcwd()

files_and_directories = os.listdir(current_directory)

files = [f for f in files_and_directories if os.path.isfile(os.path.join(current_directory, f))]

print("Files in the current directory:")
for file in files:
    print(file)
