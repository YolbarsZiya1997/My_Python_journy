menu = [
    ["egg", "bacon"],
    ["egg", "sausage", "bacon"],
    ["egg","spam"],
    ["egg","bacon","spam"],
    ["egg","bacon","sausage","spam"],
    ["spam","bacon","sausage","spam"],
    ["spam","sausage","spam","bacon","spam","tomato","spam"],
    ["spam","egg","spam","spam","bacon","spam"],
]

for meal in menu:
    if "spam" not in meal:
        # here the for-loop is searching through the list 
        # which each have their own sublists. And if "spam" is not
        # in it it will print the sublist out
        print(meal)
        for item in meal:
            # to print out the items in the sublists
            print(item)
    else:
        print("{0} has a spam score of {1}"
              .format(meal,meal.count("spam")))