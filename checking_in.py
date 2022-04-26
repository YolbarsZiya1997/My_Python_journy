parrot = "Norwegian Blue"

letter = input("Enter a character: ")
# You can also write words 

if letter in parrot:
    print("{} is in {}".format(letter,parrot))
    # Remember that it is case sensitive
else:
    print("I don't need that letter")

range
