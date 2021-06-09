numbers = {
    1: 'one',
    3: 'three',
    5: 'five',
    7: 'seven',
    9: 'nine',
}
 
print("I can count odd numbers in order")
for key in numbers:
    print(numbers[key])
 
numbers[8] = 'eight'
numbers[2] = 'two'
numbers[6] = 'six'
numbers[4] = 'four'
 
print()
print("I can count to 9 in order")
for key in numbers:
    print(numbers[key])
 
# If your code relies on the keys being sorted, sort them first
print()