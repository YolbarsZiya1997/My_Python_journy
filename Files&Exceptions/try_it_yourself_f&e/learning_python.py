with open("/home/ziya/Documents/My_Python_journy/Files&Exceptions/try_it_yourself_f&e/learning_python.txt") as file_object:
    contents = file_object.read()
    print(contents.rstrip())
    

# now I will use a more compact method

file_path = "/home/ziya/Documents/My_Python_journy/Files&Exceptions/try_it_yourself_f&e/learning_python.txt"
print("\n------------Looping over the file")
with open(file_path) as f:
    for lines in f:
        print(lines.rstrip())
        
print("\n------------Looping over the lines")
with open(file_path) as file_object_2:
    lines = file_object_2.readlines()
    
for line in lines:
    print(line.rstrip())