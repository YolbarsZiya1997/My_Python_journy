from nested_data import albums

SONGS_LIST_INDEX = 3
SONG_TITLE_INDEX = 1
while True:
# unpacking in one step
    print("Please choose your album(invalid choice exits): ")
    for index,(title, artist, year, songs) in enumerate(albums):   # the enumerate functiong gives error withou the parenthethesies
        print("{}: {}".format(index + 1, title))
    choice = int(input())
    while True:
        if 1 <= choice <= len(albums):
            songs_list = albums[choice - 1][SONGS_LIST_INDEX]
            break
        else: 
            print("Your choice is out of range, please choose carefully")
            choice = int(input())
    print("PLease choose your song: ")
    for index, (track_number, song) in enumerate(songs_list):
        print("{}: {}".format(index + 1, song))
    
    song_choice = int(input())
    while True:
        if 1 <= song_choice <= len(songs_list):
            title = songs_list[song_choice -1][SONG_TITLE_INDEX]
            break       
        else:
            print("Your choice is out of range, please choose carefully")
            song_choice = int(input())
        
    print("Playing {}".format(title))
    print("=" * 40)
    break
    
        

# unpacking in two steps
    # for index, value in enumerate(albums):
    #     title, artists, year, songs = value
    #     print(index,title,artists,year,songs)
    # break
    