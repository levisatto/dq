# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)



avg_price = mean(apps_data, 5)
avg_rating = mean(apps_data, 8)
print(avg_rating)
print(avg_price)