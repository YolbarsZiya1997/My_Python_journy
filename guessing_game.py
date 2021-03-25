"""The infinite guessing game"""
import random

highest = 10
answer = random.randint(1,highest)
print(answer) # TODO: Remove after testing
print("Please guess number between 1 and {}: ".format(highest))
guess = int(input())
"""The infinite guess game :D"""   
if guess == answer:
    print("You have got the correct answer, boiiiii")
while guess != answer:
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    guess = int(input())
    if guess == answer:
        print("Good job Rambo")
    elif guess == 0:
        print("Game  over")
        break

# if guess != answer:
#     if guess < answer:
#         print("Please guess higher")
#     else:
#         print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it ")
#     else:
#         print("Sorry, you have not guessed correctly")
# else:
#     print("You got it first time!")
 
    
# Given challenge
# if guess == answer:
#     print("You have got it first time")
# else:
#     if guess > answer:
#         print("Please guess lower")
#     else:
#         print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Now you have got it")
#     else:
#         print("Go get some milk boiii")


# if guess < answer :
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Sorry you have failed")
# elif guess > answer :
#     print("Please guess lower")
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("Mission failed, try again next time :D")
# else:
#     print("You got it first time ;D")
    
 