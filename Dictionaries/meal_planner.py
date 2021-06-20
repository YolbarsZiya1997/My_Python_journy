from contents import pantry, recipes

# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key
    
while True:
    # Display a menu of the recipes we know how to cook
    print("Please choose your recipe")
    print("-------------------------")
    for key, value in display_dict.items():
        print(f"{key} - {value}")
        
    choice = input(": ")

    if choice == "0":
        break
        
    elif choice in display_dict:
        selected_items = display_dict[choice]
        print(f"You have selected {selected_items}")
        print("Checking ingredients...\nThey are: ")
        ingredients = recipes[selected_items]
        print(ingredients)
        for food_item in ingredients:
            if food_item in pantry:
                print(f"\t{food_item} OK")
            else:
                print(f"\tYou don't have a necessary ingredient: {food_item}")
                