farm_animals = {'cow', 'sheep', 'hen', 'goat', 'horse'}
print(farm_animals)

for animals in farm_animals:
    print(animals)

print()
print('Indexing a sequence')
animal_list = ["cow", 'sheep', 'hen', 'goat', 'horse']
goat = animal_list[3]
print(goat)

# print('Indexing a set is not possible')
# goat = farm_animals[3] # will return the error that set object is not subscriptable

more_animals = {'sheep', 'hen', 'horse', 'cow', 'goat'}
if farm_animals == more_animals:
    print('The sets are equal') # sets that have the same element are considered the same set
else:
    print('The sets are different')
    
    