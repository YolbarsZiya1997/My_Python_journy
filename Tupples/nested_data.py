albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"), 
         (2, "Devil's Food"), 
         (3, "The Black Widow"), 
         (4, "Some Folks"), 
         (5, "Only Women Bleed"),
     ]
    ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"), 
         (2, "Rock Steady"), 
         (3, "Ready for Love"), 
         (4, "Don't Let Me Down"), 
         (5, "Bad Company"), 
         (6, "The Way I Choose"), 
         (7, "Movin' On"), 
         (8, "Seagull"), 
     ]
    ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"), 
         (2, "Keeping a Rendezvous"), 
         (3, "Reaper of the Glory"), 
         (4, "She Used Me Up"), 
     ]
    ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

for name, artist, year, songs in albums:
    print("Albums: {}, Artist: {}, Year: {}, Songs: {}"
          .format(name,artist,year,songs))
    
print()

# album = albums[3]
# print(album)

# songs = album[3]
# print(songs)

# song = songs[2]
# print(song)
# print(song[1])

mayhem = albums[3][3][2][1]
print(mayhem)
print(albums[3])
print()
print(albums[3][3])
print()
print(albums[3][3][2])
print()
print(albums[3][3][2][1])

# for the challenge

print(albums[1][3][5][1])
print(albums[2][2])
print(albums[3][3][3][0])
print(albums[2][3][1])