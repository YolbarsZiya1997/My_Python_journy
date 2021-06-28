# Modify the program so that the exits is a dictionary rather than a list,
# with the keys being the numbers of the locaitons and the values being 
# dictionaries holding the exits (as they do at present). No change should
# be needed to the actual code.

# Once that is working, creat another dictionary that contains words that
# players may use. These words will be the keys, and their values will be
# a single letter that the program can use to determine which way to go



locations = {
        0: "You are sitting in front of a computer learning Python",
        1: "You are standing at the end of a road before a small brick building",
        2: "You are at the top of a hill",
        3: "You are inside a building, a well house for a small stream",
        4: "You are in a valley beside a stream",
        5: "You are in the forest",    
}

exits = {
        0: {"Q": 0},
        1: {"W": 2, "E": 3, "S": 4, "N": 5, "Q": 0},
        2: {"N": 5, "E": 1, "Q": 0},
        3: {"W": 1, "Q": 0,},
        4: {"W": 2, "N": 1, "Q": 0},
        5: {"W": 2, "S": 1, "Q": 0},    
}
words = {
        "WEST": "W",
        "EAST": "E",
        "NORTH": "N",
        "SOUTH": "S",
        "QUIT": "Q"
}


loc = 1
while True:
    print(locations[loc])
    availble_exits = ", ".join(exits[loc].keys())
    
    if loc == 0:
        break
    
    direction = input("Available exits are " + availble_exits + " ").upper()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    elif direction in words.keys():
        direction = words[direction]
        loc = exits[loc][direction]
    else:
        print("Yoo mate, you can't go there !")