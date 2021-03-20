answer = 5
print("Please guess number between 1 and 10: ")
guess = int(input())

if guess < answer :
    print("Please guess higher")
    guess = int(input())
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry you have failed")
elif guess > answer :
    print("Please guess lower")
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Mission failed, try again next time :D")
else:
    print("You got it first time ;D")