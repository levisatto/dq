file_open = open('AppleStore.csv')
from csv import reader
file_reader = reader(file_open)
app_data = list(file_reader)
ratings_free = []
ratings_paid = []
for each in app_data[1:]:
    if each[5] == '0':
        rating = float(each[8])
        ratings_free.append(rating)
    else:
        rating = float(each[8])
        ratings_paid.append(rating)

avg_rating_free = sum(ratings_free) /  len(ratings_free)
avg_rating_paid = sum(ratings_paid) /  len(ratings_paid)
print(f'A pontuação média dos apps grátis é de {avg_rating_free:5.2f} em um total de {len(ratings_free)}')
print(f'A pontuação média dos apps pagos é de {avg_rating_paid:5.2f} em um total de {len(ratings_paid)}')


