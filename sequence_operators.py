#What is a sequence
#Because a sequence is ordered, we can use indexes to access individual 
# items in the sequence

#FOR EXAMPLE

computer_parts = ['computer', 'monitor','keyboard','mouse','mouse mat']
print(computer_parts[1])
print(computer_parts[1][0]) #double indexing(indexing the index itself)

string1= "he's "
string2= "probably "
string3= "pining "
string4= "for the "
string5= "fjords."

print(string1+string2+string3+string4+string5)
print("he's " "probably " "pining " "for the " "fjords")

print("Hello " * 5)
print("Hello " *(5+5))
print("Hello " *5 + "4")

today = "friday"
print("day" in today) #True
print("fri" in today) #True
print("thur" in today) #False
print("parrot" in "fjord") #False