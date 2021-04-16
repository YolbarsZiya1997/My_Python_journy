panagram = """"The quick brown
fox jumps\t
over the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))
generated_list = ['9',' ',
                  '2','2','3',' '
                  '3','7','2',' '
                  '0','3','6',' '
                  '8','5','4',' '
                  '7','7','5',' '
                  '8','0','7']
values = "".join(generated_list)
print(values)
values_list = values.split() # splits up the string at the spaces
print(values_list) 

# Mini challenge
# My way
integer_list=[]
for numbercan in generated_list:
    if numbercan != ' ':
        integer_list.append(int(numbercan))
    
print(integer_list)
# lecture way
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
    
print(values_list)
# second one
numura_setka = []
for value in values_list:
    numura_setka.append(value)
    
print(numura_setka)