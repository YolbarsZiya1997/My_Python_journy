current_choice = "-"
computer_parts = [] # creat an empty list

while current_choice != "0":
    if current_choice in "123456":
        print("Adding {}".format(current_choice))
        if current_choice == "1":
            computer_parts.append("computer")
        elif current_choice == "2":
            computer_parts.append("monitor")
        elif current_choice == "3":
            computer_parts.append("keyboard")
        elif current_choice == "4":
            computer_parts.append("mouse")
        elif current_choice == "5":
            computer_parts.append("mouse mat")
        elif current_choice == "6":
            computer_parts.append("hdmi cable")    
    else:
        print("Please add options from the list below: ")
        print("1: computer \n2: monitor \n3: keyboard \n4: mouse\n5: mouse mat\n6: hdmi cable\n0: to finish")

    current_choice = input()
    
print(computer_parts)
