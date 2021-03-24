# s
    
number = input("PLease enter a series of numbers, using any separators you like: ")
separators="" #append characters to a empty string

for char in number:
    if not char.isnumeric():
        separators = separators + char
        
# print(separators)
values = "".join(char if char not in separators else "" for char in number).split()
print(sum([int(val) for val in values]))
# remember that this sums over an empty string (Does not give us the sum somehow)
values = "".join(char if char not in separators else " " for char in number).split()
print(sum([int(val) for val in values]))
# this one do gives us the sum of the variables though
