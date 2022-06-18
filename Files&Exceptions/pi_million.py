file_name = '/home/ziya/Documents/py_crash_source/ehmatthes-pcc_2e-078318e/chapter_10/pi_million_digits.txt'

with open(file_name) as file_object:
    lines = file_object.readlines()
    
pi_string = ''
for line in lines:
    pi_string += line
    
print(f'{pi_string[:52]}...')
print(len(pi_string))

# is your birthday inside the first million digits of pi?
birthday = input("Enter you birthday: ")

if birthday in pi_string:
    print("Your birthday is in the first million digits of pi")
    
else:
    print("Your birthday is not in the first million digits of pi")