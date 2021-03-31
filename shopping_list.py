shopping_list = ["potato",
                 "green beans",
                 "mushrooms",
                 "chillies",
                 "onion",
                 "garlic",
                 "chicken",
                 "sausages",
                 "secret sauce"]
number_of_choices = []
for i in range(1,len(shopping_list)+1):
    number_of_choices.append(str(i))
print(number_of_choices)

current_choice = "-"
bill = []
while current_choice != "0":
    print("Adding {} to the bill".format(current_choice))
    if current_choice in number_of_choices:
        index = int(current_choice)-1
        chosen_goods = shopping_list[index]
        bill.append(chosen_goods)
        print("Added {}".format(chosen_goods))
    
    
    else:
        print("Please choose the goods you want from the list below")
        for number,goods in enumerate(shopping_list):
            print("{0}: {1}".format(number + 1,goods))
    current_choice = input()
            
print(bill)