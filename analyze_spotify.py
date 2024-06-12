import csv

with open("top_50_2023.csv", "r", encoding="utf8") as file:
    top_50_songs_list = list(csv.reader(file))
    top_50_songs_list.remove(top_50_songs_list[0])

print(top_50_songs_list[0])
