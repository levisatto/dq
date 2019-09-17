open_file = open('AppleStore.csv')
from csv import reader
read_file = reader(open_file)
apps_data = list(read_file)
apps_data = apps_data[1:]
content_ratings = {'4+': 0,'9+': 0, '12+': 0, '17+': 0}
for each in apps_data:
    c_rating = each[11]
    if c_rating in content_ratings:
        content_ratings[c_rating] += 1
print(content_ratings)
