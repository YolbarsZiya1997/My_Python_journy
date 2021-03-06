# myList = ["a", "b", "c", "d"]
# letters = "abcdefghijklmnopqrstuvwxyz"
# numbers = "123456789"


# newString = ""
# Cumbersome way of doing it 
# for c in myList:
#     newString += c + ", "
    
# for c in myList:
#     newString = " mississippi ".join(numbers)
# print(newString)
# ***** The Basic Adventure Game ******

locations = {
    0: "You are sitting in front of a computer learning Python",
    1: "You are standing at the end of a road before a small brick building",
    2: "You are at the top of a hill",
    3: "You are inside a building, a well house for a small stream",
    4: "You are in a valley beside a stream",
    5: "You are in the forest",    
}

exits = [
    {"Q": 0},
    {"W": 2, "E": 3, "S": 4, "N": 5, "Q": 0},
    {"N": 5, "E": 1, "Q": 0},
    {"W": 1, "Q": 0,},
    {"W": 2, "N": 1, "Q": 0},
    {"W": 2, "S": 1, "Q": 0}    
]

loc = 1
while True:
    available_exits = ", ".join(exits[loc].keys())

    print(locations[loc])
    
    if loc == 0:
        break
    
    directions = input("Availabel exits are " + available_exits + " ").upper()
    print()
    if directions in exits[loc]:
        loc = exits[loc][directions]
    else:
        print("You cannot go in that direction")
        