numbers = set()

print(numbers, type(numbers))

# while len(numbers) < 4:
#     next_value = int(input("Please enter your next value: "))
#     numbers.add(next_value)
    
# print(numbers)

data = ["blue", "red", "blue", "green", "red", "blue", "white"]

# Create a set from the list to remove the duplicates
unique_data = sorted(set(data))
print(unique_data)

# Create a list of unique colours, keeping the order they appeared
unique_data = list(dict.fromkeys(data))
print(unique_data)