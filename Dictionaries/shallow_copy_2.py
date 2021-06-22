import copy


lion_list = ["scary", "big", "cat"]
elephant_list = ["big", "grey", "wrinkled"]
teddy_list = ["cuddly", "stuffed"]


animals = {
    "lion": lion_list,
    "elephant": elephant_list,
    "teddy": teddy_list,
}
# Perform a shallow copy
# Both lists will have the same id
# things = animals.copy()

# Perform a deep copy
things = copy.deepcopy(animals)

# they have different ids
print(id(things["teddy"]), things["teddy"])
print(id(animals["teddy"]), animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])



# manually copying
# things = {
#     "lion": lion_list,
#     "elephant": elephant_list,
#     "teddy": teddy_list,
# }
# thus you can understand the one line code more percise

# print(things["teddy"])
# print(animals["teddy"])

# print()

# things["teddy"].append("toy")
# it's obvious that they are all referring to the same list
# teddy_list.append("toy")
# animals["teddy"].append("added via 'animals'")
# things["teddy"].append("added via 'things'")
# print(things["teddy"])
# print(animals["teddy"])
# print(teddy_list)
