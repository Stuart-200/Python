new_file = open("new_file.txt", 'x')
new_file.close()

import os
print("Checking if 'myfile.txt' exists")
if os.path.exists("myfile.txt"):
    os.remove('myfile.txt')
else:
    print("File does not exist")
    
my_file = open("new_file.txt", 'w')
my_file.write("Hello, World!")
my_file.close()