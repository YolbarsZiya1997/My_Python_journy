# print("Pleat enter three numbers: ")
# input_1 = int(input())
# input_2 = int(input())
# input_3 = int(input())

# result = input_1 + input_2 - input_3
# print(result)

# Using the split method

num = input("PLease enter three numbers: ")
numbers = num.split(",")
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print("Answer is = {}".format(numbers[0]+numbers[1]-numbers[2]))


    

