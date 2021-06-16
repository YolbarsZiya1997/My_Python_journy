available_parts = {"1": "computer",
                   "2": "monitor",
                   "3": "keyboard",
                   "4": "mouse",
                   "5": "mouse mat",
                   "6": "hdmi cable",
                   "7": "dvd drive",
                   "8": "joy stick"
}

current_choice = None
while current_choice != "0":
    if current_choice in available_parts:
        chosen_part = available_parts[current_choice]
        print(f"Adding {chosen_part}")
    
    current_choice = input("> ")
    
else:
    print("The item you are looking for is not in stock")
    
    
