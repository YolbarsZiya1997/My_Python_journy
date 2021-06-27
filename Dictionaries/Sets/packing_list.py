travel_mode = {"1": "car", "2": "plane"}

items = {
    "can opener",
    "fuel",
    "jumper",
    "knife",
    "matches",
    "razor blades",
    "razor",
    "scissors",
    "shampoo",
    "shaving cream",
    "shirts (3)",
    "shorts",
    "sleeping bag(s)",
    "soap",
    "socks (3 pairs)",
    "stove",
    "tent",
    "mug",
    "toothbrush",
    "toothpaste",
    "towel",
    "underwear (3 pairs)",
    "water carrier",
}

restricted_items = {
    "catapult",
    "fuel",
    "gun",
    "knife",
    "razor blades",
    "scissors",
    "shampoo",
}

print("Please choose your way of travel")
for key, value in travel_mode.items():
    print(f"{key} - {value}")
    
mode = "-"
while mode not in travel_mode:
    mode = input("> ")
    
if mode == "2":
    for restricted_item in restricted_items:
        items.discard(restricted_item)
        # using remove would cause an error here
    
# print the packing list 
print("You need to pack: ")
for item in sorted(items):
    print(item)
    