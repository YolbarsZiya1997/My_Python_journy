# t = ("a", "b", "c")
# print(t)
# name = "Ziya"
# age = 10

# print((name,age,"Python",2020)) # Tupple version

welcome = "Welcome to my Nightmare", "Alice Cooper", 1975
bad = "Bad Company", "Bad Company", 1974
budgie = "Nightflight", "Budgie", 1981
imelda = "More Mayhem", "Emilda May", 2011
metallica = "Ride the Lightning", "Metallica", 1984

# print((metallica))
# print(metallica[0],metallica[2])
# # metallica[0] = "Master of Puppets" #Tupples are immutable
# metallica_2 = list(metallica)
# print(metallica_2)

# metallica_2[0] = "Feth el jihan"
# print(metallica_2)

title, artist, year = metallica
print(title,artist,year)

table = ("Coffee table", 200, 100, 75, 34.50)
print(table[1]*table[2])

name, length, width, height, price = table
print(length*width)
# I mean the purpose of the programm above is to make the code more readable
