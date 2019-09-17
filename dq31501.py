opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(index):
    new_list = []
    for each in apps_data[1:]:
        item = each[index]
        new_list.append(item)
    return new_list
def frequency(lista):
    frequencia = {}
    for each in lista:
        if each in frequencia:
            frequencia[each] += 1
        else:
            frequencia[each] = 1
    return frequencia

genres = list(extract(12))
print(genres)
lista_frequencia = frequency(genres)
print(lista_frequencia)