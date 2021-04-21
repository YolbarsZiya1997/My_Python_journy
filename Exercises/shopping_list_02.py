goods = [("potato", 4.00),
         ("green beans", 11.50),
         ("mushrooms", 7.50),
         ("chillies", 12.50),
         ("onion", 3.45),
         ("garlic", 18.00),
         ("chicken", 35.00),
         ("sausages", 12.75),
         ("secret sauce",7.00),
        ]
print("Please choose the grocery you want")
for index, (items,prices) in enumerate(goods):
    print("{}: {}".format(index+1,items))
check = []
ITEMS = 0
PRICES = 1
while True:
    choice = int(input())
    if 1 <= choice <= len(goods):
        if goods[choice-1] in check:
            print("Removing {} from the bill".format(goods[choice-1][ITEMS],goods[choice-1][PRICES]))
            check.remove(goods[choice-1])
        else:
            print("Adding {} to the bill, it's {}".format(goods[choice-1][ITEMS],goods[choice-1][PRICES]))
            check.append(goods[choice-1])
        print("Your list now consists {}".format(check))
        
    elif choice > len(goods):
        print("That goods is not available, try again later")
        print()
        for index, (items,prices) in enumerate(goods):
            print("{}: {}".format(index+1,items))
    else:
        print("Your bill is ready")
        total = 0
        for indexs, (item,price) in enumerate(check):
            total += price # same as total = total + price
        print("Totall is {} dollar".format(total))
        print(check)
        break
        
        


            
        
        
        