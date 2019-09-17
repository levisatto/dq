open_file = open('AppleStore.csv')
from csv import reader
read_file = reader(open_file)
apps_data = list(read_file)


def freq_table(index):
    table = {}
    for each in apps_data[1:]:
        value = each[index]
        if value in table:
            table[value] += 1
        else:
            table[value] = 1
    return table
price = freq_table(12)

print(price)