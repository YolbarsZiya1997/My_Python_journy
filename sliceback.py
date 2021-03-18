from typing_extensions import IntVar


letters = 'abcdefghijklmnopqrstuvwxyz'
           
backwards = letters[25:0:-1]#-1]
print(backwards)
backwards = letters[26::-1]
print(backwards)
backwards = letters[25::-1]
print(backwards)
backwards = letters[::-1] #python idiom for printing in reverse order
print(backwards)

print(letters[16:13:-1])
print(letters[4::-1])
boom = letters[25:16:-1]
print(boom)

print(letters[-4:])
print(letters[-1:])
print(letters[:1])
print(letters[0])