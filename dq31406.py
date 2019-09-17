'''idade = ['4+', '4+', '4+', '9+', '9+', '12+', '17+']
contidade = {}
for each in idade:
    if each in contidade:
        contidade[each] += 1
    else:
        contidade[each] = 1
print(contidade)
'''
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
content_ratings = {}
for each in apps_data[1:]:
    c_ratings = each[11]
    if c_ratings in content_ratings:
        content_ratings[c_ratings] += 1
    else:
        content_ratings[c_ratings] = 1
print(content_ratings)