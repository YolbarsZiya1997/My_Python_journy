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
    print(locations[loc])
    availble_exits = ", ".join(exits[loc].keys())
    
    if loc == 0:
        break
    
    direction = input("Available exits are " + availble_exits + " ").upper()
    if direction in exits[loc]:
        loc = exits[loc][direction]
    else:
        print("Yoo mate, you can't go there !")