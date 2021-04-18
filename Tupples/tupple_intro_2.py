albums = [("Welcome to my Nightmare", "Alice Cooper", 1975),
         ("Bad Company", "Bad Company", 1974),
         ("Nightflight", "Budgie", 1981),
         ("More Mayhem", "Emilda May", 2011),
         ("Ride the Lightning", "Metallica", 1984),
         ]

new_song = ("Arghimaq attar", "Batırlar", 1100)
albums.append(new_song)
print(albums)
for album in albums:
    name, artist, year = album
    print("Album : {}, Artist: {}, Year: {}"
          .format(name,artist,year))
print()
# Other method 
for name, artist, year in albums:
    print("Album: {}, Artist: {}, Year: {}"
          .format(name,artist,year))
    