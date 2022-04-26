name = input("Please enter your name: ")
age = int(input("How old are you,{0}? ".format(name)))
print(type(age))

if age >= 18:
    print("You are old enough to vote")
    print("Please put an X in the box")
else:
    print("You need some milk :D, come back in {} years mate".format(18-age))



if age < 18:
    print("You need some milk :D, come back in {} years mate".format(18-age))
elif age == 900:
    print("Sorry, Yoda, you die in Return of the Jedi :D")
else:
    print("You are old enough to vote")
    print("Please put an X in the box")
    


