open_file = open('AppleStore.csv')
from csv import reader
read_file = reader(open_file)
apps_data = list(read_file)
data_sizes = []
for each in apps_data[1:]:
    size = float(each[3])
    data_sizes.append(size)

max(data_sizes)
min(data_sizes)