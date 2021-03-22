name = input("What is your name?: ")
age = int(input("Please tell us your age?:  "))

if 18 <= age < 31:
    print("Well come aboard {}".format(name))
elif age >= 31:
    print("You are too old for this grandpa {}".format(name))
else:
    print("Step down! Punk!")
    