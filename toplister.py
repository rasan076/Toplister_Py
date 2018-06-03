from classes.song import Song
from classes.comparer import Comparer
from json_parser import parse_songs_from_json
from json_parser import write_songs_to_json

inputFile = "songs_example.json"
outputFile = "test_output.json"


def getSongText(song):
    text = song.title
    text += " - by "
    for artist in song.main_artists:
        text += artist
        if song.main_artists.index(artist) == (len(song.main_artists) - 2):
            text += " and "
        elif song.main_artists.index(artist) < (len(song.main_artists) - 2):
            text += ", "
    if len(song.featuring_artists) > 0:
        for artist in song.featuring_artists:
            text += " feat. "
            text += artist
            if song.featuring_artists.index(artist) == (len(song.featuring_artists) - 2):
                text += " and "
            elif song.featuring_artists.index(artist) < (len(song.featuring_artists) - 2):
                text += ", "
    return text


def printQuestion(song1, song2):
    text1 = "1: "
    text2 = "2: "
    text1 += getSongText(song1)
    text2 += getSongText(song2)
    print("")
    print("Which song do you prefer?")
    print(text1)
    print(text2)


song_list = []

print("Hello and welcome to toplister.py")


parse_songs_from_json(song_list, inputFile)


comparer = Comparer(song_list)

while True:
    printQuestion(comparer.getFirstSong(), comparer.getSecondSong())
    try:
        choise = int(input("Write '1' or '2' to chose: "))
    except ValueError: 
        print("\nLeaving toplister.py")
        break
        
    retVal = comparer.selectWinner(choise)
    if retVal == 0:
        print("")
    else:
        print("ERROR: Illigal input, no scores changed, try again\n")



write_songs_to_json(song_list, outputFile)
print("Save sucessful")