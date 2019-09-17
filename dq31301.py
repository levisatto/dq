open_file = open('AppleStore.csv')
from csv import reader
read_file = reader(open_file)
apps_data = list(read_file)
totalFree = 0
totalPaid = 0
count_free = 0
count_paid = 0
for each in apps_data[1:]:
    if each[5] == '0':
        rating = float(each[8])
        totalFree = totalFree + rating
        count_free +=1
    if each[5] != '0':
        rating = float(each[8])
        totalPaid += rating
        count_paid += 1


avg_paid = totalPaid / count_paid
avg_free = totalFree / count_free


print(f'A nota média dos apps grátis é {avg_free:5.2f} em um total de {count_free} apps')
print(f'A nota média dos apps pagos é {avg_paid:5.2f} em um total de {count_paid} apps')