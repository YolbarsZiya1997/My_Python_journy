available_exits = ["north","south","east","west"]

chosen_exit = ""
while chosen_exit.casefold() not in available_exits:
    #  It seems like the casefold function generally are used in
    # statements, if not it will give error
    """Because the input direction is not in the available exits
    the while loop continues until it is false"""
    chosen_exit = input("Please choose a direction: ")
    if chosen_exit.casefold() == "quit":
        print("Game over")
        break
    
print("aren't you glad you got out of there")

