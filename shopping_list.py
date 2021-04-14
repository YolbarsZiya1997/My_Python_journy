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
    if current_choice not in number_of_choices:       
        print("Please choose the goods you want from the list below")
    # print("Adding {} to the bill".format(shopping_list[int(current_choice)]))
    # print("Please choose the goods you want from the list below")
        for number,goods in enumerate(shopping_list):
            print("{0}: {1}".format(number + 1,goods))
    
    
    elif current_choice in number_of_choices:
        index = int(current_choice)
        chosen_goods = shopping_list[index]
        bill.append(chosen_goods)
        
    
    current_choice = input()
    if current_choice != "0":
        print("Adding {} to the bill".format(shopping_list[int(current_choice)]))
    
    
            
print(bill)

# One problem remain in this code when entering the current_choice 
# the indexing starts from 0 instead of one, although it is a minute bug
# but it is worth solving 