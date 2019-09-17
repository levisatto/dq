open_file = open('AppleStore.csv')
from csv import reader
read_file = reader(open_file)
app_list = list(read_file)
app_data = app_list[1:]
games_rating = []
for each in app_data:
    rating = float(each[8])
    genre = each[12]
    if genre == 'Games':
        games_rating.append(rating)
avg_game_rating = sum(games_rating) / len(games_rating)
print(avg_game_rating)