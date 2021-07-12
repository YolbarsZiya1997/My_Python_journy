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

namedExits = {
        1: {"2": 2, "3": 3, "4": 4, "5": 5},
        2: {"5": 5, "1": 1},
        3: {"1": 1},
        4: {"2": 2, "1": 1},
        5: {"2": 2, "1": 1},
}

vocabulary = {
        "WEST": "W",
        "EAST": "E",
        "NORTH": "N",
        "SOUTH": "S",
        "QUIT": "Q",
        "ROAD": "1",
        "HILL": "2",
        "BUILDING": "3",
        "VALLEY": "4",
        "FOREST": "5",
}

loc = 1
while True:
    print(locations[loc])
    available_exits = ", ".join(exits[loc].keys())
    
    if loc == 0:
        break
    else:
        allExits = exits[loc].copy() # main purpose of this dict is to contain all the existing exits
        allExits.update(namedExits[loc]) # while not disturbing the user interface
    
    direction = input("Available exits are " + available_exits + " ").upper()
    print()
    # Parse the user input in vocabulary
    if len(direction) > 1: # which we detect that the input is a word
        # for word in vocabulary:
        #     if word in direction:
        #         direction = vocabulary[word]
        words = direction.split()
        for word in words:
            if word in vocabulary:
                direction = vocabulary[word]
                break
        
    if direction in allExits:
        loc = allExits[direction]

    else:
        print("Yoo mate, you can't go there !")