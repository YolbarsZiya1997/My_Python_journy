"""My version"""
# import random

# highest = 10
# answer = random.randint(1,highest)

# print(answer)
# print("Please enter a number between 1 and {}: ".format(highest))
# guess = int(input())

# if guess == answer:
#     print("Yaraysen, birinci qetimde muwapıqıyet kazandıng")
    
# while guess != answer:
#     if guess <= answer:
#         print("Chongraq bir san kir")
#     else:
#         print("Kichikrek bir san kir")
#     guess = int(input())
#     if guess == answer:
#         print("Barikallah, nowettiki wezipege atlan!")
#     elif guess == 0:
#         print("Berip süt emip kel!")
#         break

"""The lecturers version"""

import random

highest = 10
answer = random.randint(1,highest)
print(answer)
guess = 0 # initializer for the while-loop
print("Please enter a number between 1 and {}".format(highest))

while guess != answer:
    guess = int(input())
    if guess == answer:
        print("You have got it, Rambo")
    
    elif guess == 0:
        print("He needs some milk folk, Game Over!")
        break
    
    else:
        if guess > answer:
            print("Slow down, Soldier")
        else:
            print("Go higher boii")
    

