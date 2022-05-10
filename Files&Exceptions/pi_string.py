file_name = "/home/ziya/Documents/My_Python_journy/Files&Exceptions/pi_digits.txt"

with open(file_name) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line.strip()       # different from the rstrip() it strips the spaces between
    
print(pi_string)
print(len(pi_string))