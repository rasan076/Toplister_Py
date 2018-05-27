import json
from classes.song import Song


def parse_songs_from_json(song_objects, path):
    with open(path) as f:
        data = json.load(f)
    songs = data["songs"]
    for song in songs:
        temp = Song(song["id"])
        temp.title = song["title"]
        if "artists" in song:
            if "main_artists" in song["artists"]:
                temp.main_artists = []
                temp.main_artists_countries = []
                for artist in song["artists"]["main_artists"]:
                    if "name" in artist:                    
                        temp.main_artists.append(artist["name"])
                        if "country" in artist:
                            temp.main_artists_countries.append(artist["country"])
                        else:
                            temp.main_artists_countries.append("")
            if "featuring" in song["artists"]:
                temp.featuring_artists = []
                temp.featuring_artists_countries = []
                for artist in song["artists"]["featuring"]:
                    if "name" in artist:                    
                        temp.featuring_artists.append(artist["name"])
                        if "country" in artist:
                            temp.featuring_artists_countries.append(artist["country"])
                        else:
                            temp.featuring_artists_countries.append("")
        if "release_year" in song:
            temp.year = song["release_year"]
        if "genre" in song:
            temp.genre = song["genre"]
        if "score" in song:
            temp.score = song["score"]
        if "comparisons" in song:
            temp.comparisons = song["comparisons"]
        song_objects.append(temp)


def write_songs_to_json(song_list, path):
    temp = {}
    temp["songs"] = []
    for song in song_list:
        temp_song = {}
        temp_song["id"] = song.id
        temp_song["title"] = song.title
        temp_song["artists"] = {}
        
        if len(song.main_artists) > 0:
            main_artist_list = []
            for artist_name in song.main_artists:
                artist_entry = {}
                artist_entry["name"] = artist_name
                ind = song.main_artists.index(artist_name)
                artist_entry["country"] = song.main_artists_countries[ind]
                main_artist_list.append(artist_entry)
            temp_song["artists"]["main_artists"] = main_artist_list
        
        if len(song.featuring_artists) > 0:
            feat_artist_list = []
            for artist_name in song.featuring_artists:
                artist_entry = {}
                artist_entry["name"] = artist_name
                ind = song.featuring_artists.index(artist_name)
                artist_entry["country"] = song.featuring_artists_countries[ind]
                feat_artist_list.append(artist_entry)
            temp_song["artists"]["featuring"] = feat_artist_list
        
        temp_song["release_year"] = song.year
        if song.genre != "":
            temp_song["genre"] = song.genre
        temp_song["score"] = song.score
        temp_song["comparisons"] = song.comparisons
        
        temp["songs"].append(temp_song)

    with open(path, "w") as outfile:
        json.dump(temp, outfile, sort_keys=False, indent=4)


song_objects = []
parse_songs_from_json(song_objects, "songs_example.json")
write_songs_to_json(song_objects, "test_output.json")