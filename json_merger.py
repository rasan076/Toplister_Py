from classes.song import Song
from json_parser import parse_songs_from_json
from json_parser import write_songs_to_json

output_file = "songlists/big_songlist.json"
input_files = [
    "songlists/1965-1969.json",
    "songlists/1970-1974.json",
    "songlists/1975-1979.json",
    "songlists/1980-1984.json",
    "songlists/1985-1989.json",
    "songlists/1990-1994.json",
    "songlists/1995-1999.json",
    "songlists/2000-2004.json",
    "songlists/2005-2009.json",
    "songlists/2010-2014.json",
    "songlists/2015-2019.json"]
song_list = []

for file in input_files:
    parse_songs_from_json(song_list, file)
    print("Reading " + file)

write_songs_to_json(song_list, output_file)
print("Sucessfully saved to " + output_file)