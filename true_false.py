# day = "Saturday"
# temperature = 30
# raining = True

# if (day == "Saturday" and temperature > 27) or not raining: 
#     #remember that or in line 5 could also be "and"
#     print("Go swimming")
# else:
#     print("Learn python")

if 0:
    print("True")
else:
    print("False")
    
name = input("Please enter your name: ")
# if name:
if name != "":
    print("Hello,{}".format(name))
    """ if we had type nothing in here, the empty string 
    will be evaluated as false an the code will go ahead and print out
    the else statement."""
else:
    print("Are you the man with no name")