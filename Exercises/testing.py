import math
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
total = 0
for index, (items, prices) in enumerate(goods):
    total += prices
print(total)
    