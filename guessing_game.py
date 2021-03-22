answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())


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
 
"""The infinite guess game :D"""   
while guess != answer:
    if guess < answer:
        print("Please guess higher")
    elif guess > answer:
        print("Please guess lower")
    guess = int(input())
if guess == answer:
    print("You have got the correct answer, boiiiii")
    
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
    
 