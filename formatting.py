for i in range(1, 13):
    #right aligned
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i,i**2,i**3))
print()

for i in range(1, 13):
    print("No. {0:<2} squared is {1:<3} and cubed is {2:<4}".format(i,i**2,i**3))
    #left aligned
print()

for i in range(1, 13):
    print("No. {0:^2} squared is {1:^3} and cubed is {2:^4}".format(i,i**2,i**3))
    #center the fields

print()

print("Pi is approximately {0:12}".format(22/7)) #general formal for 12 decimals
# remember the 12 here is only for making space for the out put for the code 
# as you can see the output is 15 decimal, thus is what you want is only a 12 decimal output
# you can add a '.' ({0:.12}) infront of the index
print("Pi is approximately {0:<12f}".format(22/7))  #six digits after decimal point
# the f automatically make the output limited to 6 decimal
print("Pi is approximately {0:12.50f}".format(22/7)) #percision of field of 50
print("Pi is approximately {0:52.50f}".format(22/7)) #different field size
print("Pi is approximately {0:<72.50f}".format(22/7))
print("Pi is approximately {0:<72.56f}".format(22/7))

for i in range(1, 13):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:<4}".format(i,i**2,i**3))