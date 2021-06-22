animals = {
    "lion": ["scary", "big", "cat"],
    "elephant": ["big", "grey", "wrinkled"],
    "teddy": ["cuddly", "stuffed"],
}

# I predict the out come would be toy
# things = animals # the things here is not a copy of the animal, they are the same dict
things = animals.copy() # the things is a copy of animal, which has its own values and keys

print(things["teddy"])
print(animals["teddy"])

print()

things["teddy"].append("toy")
print(things["teddy"])
print(animals["teddy"])
# the toy value is not independently appended to the things but instead it appended to both the things and animals
# Thus when the value is a mutable objec, the copy will be a shallow copy which doesn't creat a completely new list?
