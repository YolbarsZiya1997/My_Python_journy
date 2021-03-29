options = ["exit","Learn Python","Learn Java","Go swimming","Have dinner","Go to bed"]
print("Please choose your option from the list below:")
choices = "1. Learn Python\n2. Learn Java\n3. Go swimming\n4. Have dinner\n5. Go to bed\n0. exit"
print(choices)

while True:
    choice = int(input("Please enter you choice: "))
    if choice == 1:
        print("It is a good choice to learn Python.")
    elif choice == 2:
        print("Remember that Java is kind of a ugly language.")
    elif choice == 3:
        print("It is still cold at this time of the year man!")
    elif choice == 4:
        print("Let's have some roasted chicken,aye?")
    elif choice == 5:
        print("Good night!")
    
    else:
        print("Game over")
        break
    