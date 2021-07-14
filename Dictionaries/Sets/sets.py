# farm_animals = {"sheep", "cow", "hen"}
# print(farm_animals)

# for animal in farm_animals:
#     print(animal)
    
# print("*" * 40)

# wild_animals = set(["lion", "tiger", "panther", "elephant", "hare"])
# print(wild_animals)

# for animals in wild_animals:
#     print(animals)
    
# farm_animals.add("horese")
# wild_animals.add("horese")
# print(farm_animals)
# print(wild_animals)

# adding to a set

# empty_set = set()
# print(empty_set)
# empty_set.add("this is some funny stuff")
# print(empty_set)

# empty_set2 = {}
# print(empty_set2)
# # empty_set2.add("who") # would give error

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)

# union of sets

# even = set(range(0, 40, 2))
# print(even)
# print(len(even))

# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print(len(squares))

# print(even.union(squares)) # the union does not contain duplicates
# print(len(even.union(squares)))
# print("-" * 80)

# intersection of sets

# print(even.intersection(squares))
# print(even & squares)
# print(squares.intersection(even))
# print(squares & even)

# set differene

# even = set(range(0, 40, 2))
# print(sorted(even))
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(sorted(squares))
# print()
# print("Even minus squares")
# print(sorted(even.difference(squares)))
# print(sorted(even - squares))
# print()
# print("Squares minus even")
# print(sorted(squares.difference(even)))
# print(sorted(squares - even))

# print("=" * 40)
# print(sorted(even))
# print(squares)
# even.difference_update(squares) # does not return a new set, instead it updates it staying still
# print(sorted(even))

# even = set(range(0, 40, 2))
# print(even)
# squares_tuple = (4, 6, 9, 16, 25)
# squares = set(squares_tuple)
# print(squares)
# print()
# print("symmetric even minus squares")
# print(sorted(even.symmetric_difference(squares)))
# print()
# print("symmetric squares minus even")
# print(sorted(squares.symmetric_difference(even)))

# removing an item from a set

# squares.discard(4)
# squares.remove(16)
# squares.discard(8)
# print(squares)
#squares.remove(8) # will give an error if the item removed is not in the set
# safer solution for that would be 
# if 8 in squares:
#     squares.remove(8)
# # or 
# try:
#     squares.remove(8)
# except KeyError:
#     print("The item 8 is not a member of the set")

even = set(range(0, 40, 2))
print(even)
squares_tuple = (4, 6, 16)
squares = set(squares_tuple)
print(squares)

if squares.issubset(even):
    print("squares is a subset of even")
    
if even.issuperset(squares):
    print("even is a superset of squares")