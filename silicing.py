parrot = 'Norwegian Blue'
#         012345678
# print(parrot[0:6]) #Norweg

# last character we specify in the slicing is not included in the out put
# print(parrot[3:5])
# print(parrot[0:9])
# print(parrot[:9])
# print(parrot[10:14])
# print(parrot[10:])
# print(parrot[:6])
# print(parrot[6:])
# print(parrot[:6]+parrot[6:])
# print(parrot[:])

# silicing using negative indexes

# print(parrot[-4:-2])
# print(parrot[-4:12])
# print(parrot[:-6]+parrot[-6:])
# print(parrot[-12:-9])

#using steps
print(parrot[0:6:2])
print(parrot[0:6:3])

number='9,223;372:036 854,775;807'
seperators=number[1::4]
print(seperators)
values = "".join(char if char not in seperators else "" for char in number).split()
print([int(val) for val in values])
values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])