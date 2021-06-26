# print("Please choose your option from the list below: ")
# choices = "1. Learn Python\n2. Learn Java\n3. Go swimming\n4. Have dinner\n5. Go to bed\n0. exit"
# print(choices)
# choice = "-"
# while True:
#     # choice = input()
#     if choice == "0":
#         print("Game over")
#         break
#     elif choice in "12345":
#         print("You chose {}".format(choice))
#     else:
#         print("Please choose your option from the list below")
#         print("1:\tLearn Python")
#         print("2:\tLearn Java")
#         print("3:\tGo swimming")
#         print("4:\tHave dinner")
#         print("5:\tGo to bed")
#         print("0:\tExit")
    
#     choice = input()
    
choice = "-"
while choice != "0":
    # choice = input()
    if choice in set('12345'):
        print("You chose {}".format(choice))
    else:
        print("Please choose your option from the list below")
        print("1:\tLearn Python")
        print("2:\tLearn Java")
        print("3:\tGo swimming")
        print("4:\tHave dinner")
        print("5:\tGo to bed")
        print("0:\tExit")
    
    choice = input()
    
else:
    print("Game Over")