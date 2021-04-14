menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","bacon","spam","spam",],
]

# for meal in menu:
#     for index,item in enumerate(meal):
#         if item == "spam":
#             del meal[index]    
#     print(meal)

for meal in menu:
    for index in range(len(meal)-1,-1,-1):
        if meal[index]== "spam":
            del meal[index]
    print(meal)

# for meal in menu:
#     for item in meal:
#         if item != "spam":
#             print(item)
#     print()
        
            
                
                
            
            
    