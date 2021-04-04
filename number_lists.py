empty_list = []

even = [2,4,6,8]
odd = [1,3,5,7,9]

numbers = even + odd
print(numbers)

sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

digits = list("432985617")
print(digits)

# more_numbers = list(numbers)
# more_numbers = numbers[:]
more_numbers = numbers.copy()
print(more_numbers)
print(numbers is more_numbers) # would return true if the two items are refering to the same list
print(numbers == more_numbers) # would return true if the lists contains the same items in the same order

