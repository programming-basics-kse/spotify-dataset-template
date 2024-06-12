import csv

with open("top_50_2023.csv", "r", encoding="utf8") as file:
    top_50_songs_list = list(csv.reader(file))
    top_50_songs_list.remove(top_50_songs_list[0])

print(top_50_songs_list[0])
#1 Average Danceability
DENCEABILITY = 5
danceability_list = [float(song[DENCEABILITY]) for song in top_50_songs_list]
average_danceability = sum(danceability_list) / len(danceability_list)
print(f"The average danceability is: {average_danceability}")

#2 Release Date Difference:
from datetime import datetime
ALBUM_RELEASE_DATE = 3
POPULARITY = -1
data_format = "%Y-%m-%d"
most_popular = top_50_songs_list[0]
least_popular = top_50_songs_list[0]
for song in top_50_songs_list:
    if song[POPULARITY] > most_popular[POPULARITY]:
        most_popular = song
    elif song[POPULARITY] < least_popular[POPULARITY]:
        least_popular = song

most_popular_release_date = datetime.strptime(most_popular[ALBUM_RELEASE_DATE], data_format)
least_popular_release_date = datetime.strptime(least_popular[ALBUM_RELEASE_DATE], data_format)
difference = (most_popular_release_date - least_popular_release_date).days
print(f"The difference in days between the release dates of the most and least popular tracks is {difference}")
#3 Top Three Genres:
GENRES = 4
genres_dict = {}
for song in top_50_songs_list:
    genres_list = eval(song[GENRES])
    for genre in genres_list:
        genres_dict[genre] = genres_dict.get(genre, 0) + 1
sorted_genres = sorted(genres_dict.items(), key=lambda x: x[1], reverse=True)
top_three_genres = [genre[0] for genre in sorted_genres[:3]]
print(f"The three genres that occur most frequently in the dataset are {', '.join(top_three_genres)}")
#4 Average Liveliness with Energy Criteria:
ENERGY = 7
LIVELINESS = 11
liveliness_for_energy_songs = [float(song[LIVELINESS]) for song in top_50_songs_list if float(song[ENERGY]) > 0.5]
if liveliness_for_energy_songs:
    average_liveliness = sum(liveliness_for_energy_songs) / len(liveliness_for_energy_songs)
    print(f"The average value of liveliness for tracks where energy is greater than 0.5 is {round(average_liveliness, 2)}")
#5 Recurring Artists and Song Titles:
ARTIST = 0
TRACK = 1
artist_songs_dict = {}
for song in top_50_songs_list:
    artist = song[ARTIST]
    track = song[TRACK]
    if artist in artist_songs_dict:
        artist_songs_dict[artist].append(track)
    else:
        artist_songs_dict[artist] = [track]
recurring_artists = {artist: songs for artist, songs in artist_songs_dict.items() if len(songs) > 1}
print("Recurring Artists and Song Titles:")
for artist, songs in recurring_artists.items():
    print(f"{artist}:")
    for track in songs:
        print(f"{track}")


