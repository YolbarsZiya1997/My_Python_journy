pangram = "The quick brown fox jumps over the lazy dog"

letters = sorted(pangram)
print(letters)

numbers = [2.3,4.5,8.7,9.2,3.1,1.6]
# The main difference between the line above and the line below is that 
# the upper one does not creat a new list while the one below creats a 
# new list of its own
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)
numbers.sort()
print(numbers)

missing_letter = sorted("The quick brown fox jumped over the lazy dog",
                        key=str.casefold)
print(missing_letter)

names = ["Graham",
         "John",
         "terry",
         "eric",
         "Terry",
         "michael"
         ]
names.sort(key=str.casefold)
print(names)
