'''def open_dataset(file_name='AppleStore.csv'):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    return data


apps_data = open_dataset()
print(apps_data)'''


# INITIAL CODE
def open_dataset(file_name='AppleStore.csv', header=True):
    opened_file = open(file_name)
    from csv import reader
    read_file = reader(opened_file)
    data = list(read_file)

    if header:
        return data[0], data[1:]
    else:
        return data


all_data = open_dataset(header=True)
for e in all_data:
    print(e)