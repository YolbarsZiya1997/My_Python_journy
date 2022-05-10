"""
with open('/home/ziya/Documents/My_Python_journy/Files&Exceptions/pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents.rstrip())
 """   
    
# Another way of doing this is that
"""
file_path = "/home/ziya/Documents/My_Python_journy/Files&Exceptions/pi_digits.txt"
with open(file_path) as file_object_1:
    contents_1 = file_object_1.read()
    print(contents_1.rstrip())
"""
    

# Reading the file line by line
file_name = "/home/ziya/Documents/My_Python_journy/Files&Exceptions/pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()
    
for line in lines:
    print(line.rstrip())