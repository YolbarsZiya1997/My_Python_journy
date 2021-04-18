# for index, character in enumerate("abcdefgh"):
#     print(index, character)

for t in enumerate("abcdefgh"):
    index, character = t
    print(index, character) # this line is for the purpose of unpacking tuple
    
    
# index, character = (0,'a')
# print(index)
# print(character)