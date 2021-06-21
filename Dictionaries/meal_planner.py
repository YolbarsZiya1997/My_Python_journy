from contents import pantry, recipes

def add_shopping_item(data: dict, item: str, amount: int) -> None:
    """Add a key and value couple called 'item' and 'amount' to the 'data' dict.

    Args:
        data (dict): the dictionary you wanna use
        item (str): the items that are being added to the list
        amount (int): amount of items
    """
    # if item in data:
    #     data[item] += amount
    # else:
    #     data[item] = amount
    data[item] = data.setdefault(item, 0) + amount
    # the setdefault() method returns the value if the key exists.
    # if not it assigns a new entry for the value and assign the default value to ,t
    #  in our case it is 0
    
    
# display_dict = {str(index + 1): meal for index, meal in enumerate(recipes)}
display_dict = {}
for index, key in enumerate(recipes):
    display_dict[str(index + 1)] = key

shopping_list = {}
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
        selected_item = display_dict[choice]
        print(f"You have selected {selected_item}")
        print("checking ingredients ...")
        ingredients = recipes[selected_item]
        print(ingredients)
        for food_item, required_quantity in ingredients.items():
            quantity_in_pantry = pantry.get(food_item, 0) # the use of get might seem a litte confusing, but it is just dict[key], and the 0 there is for default value
            if required_quantity <= quantity_in_pantry:
                print(f"\t{food_item} OK")
            else:
                quantity_to_buy = required_quantity - quantity_in_pantry
                print(f"\tYou need to buy {quantity_to_buy} of {food_item}")
                add_shopping_item(shopping_list, food_item, quantity_to_buy)
            # print(shopping_list) one more thing to remember is that; the datas are stored as key and value not a tuple

if shopping_list != {}:
    print("This will be your grocery list ")
for items, amounts in shopping_list.items():
    print(items, amounts)
    