age = 24.0
print("My age is {0} years".format(age))
# The .format() function seems to fit the data type into the string
# NO matter what the data type is

print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}"
        .format(31, "Jan","March","May","Jul","Aug","Oct","Dec"))

print("There are {0} days in Jan,March,May and etc".format(31))

print("Monthes have different days for example Jan: {2}, Feb: {0}, Mar: {2}, Apr: {1}, May: {2}, June: {1}, July: {2}, Aug: {2}, Sep: {1}, Oct: {2}, Nov: {1},Dec: {2}"
        .format(28,30,31))

print()

print("""Jan: {2}
Feb: {0}
Mar: {2}
Apr: {1}
May: {2}
Jun: {1} 
Jul: {2} 
Aug: {2} 
Sep: {1}
Oct: {2} 
Nov: {1}
Dec: {2}""".format(28,30,31))