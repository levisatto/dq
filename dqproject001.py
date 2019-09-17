def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]
    for row in dataset_slice:
        print(row)
        print('\n') # adds a new (empty) line after each row

    if rows_and_columns:
        print('Number of rows:', len(dataset))
        print('Number of columns:', len(dataset[0]))

from csv import reader

open_apple_file = open('AppleStore.csv')
read_apple_file = reader(open_apple_file)
apple_data = list(read_apple_file)
apple_header = apple_data[0]
apple_data = apple_data[1:]

open_google_file = open('googleplaystore.csv')
read_google_file = reader(open_google_file)
google_data = list(read_google_file)
google_header = google_data[0]
google_data = google_data[1:]


#Find errors

def find_list_error(list_name):
    for each in list_name:
        correct_length = len(list_name[0])
        length = len(each)
        if correct_length != length:
            print(list_name.index(each))


find_list_error(google_data)
del google_data[10472]
find_list_error(google_data)

# Duplicates
'''for each in google_data:
    name = each[0]
    if name == 'Facebook':
        print(each)'''

# Duplicate count

def duplicate_count(list_name, pos):
    duplicate_apps = []
    unique_apps = []
    for each in list_name:
        name = each[pos]
        if name in unique_apps:
            duplicate_apps.append(name)
        else:
            unique_apps.append(name)
    print('Number of duplicate apps: ', len(duplicate_apps))
    print('Number of unique apps: ', len(unique_apps))

duplicate_count(google_data, 0)
duplicate_count(apple_data, 2)

# Highest number of reviews ANDROID

reviews_max_android = {}

for each in google_data:
    name = each[0]
    n_reviews = float(each[3])
    if name in reviews_max_android and reviews_max_android[name] < n_reviews:
        reviews_max_android[name] = n_reviews
    elif name not in reviews_max_android:
        reviews_max_android[name] = n_reviews

#ANDROID CLEAN
android_clean = [] # cleaned and chose the highest reviews
android_added = [] # app names
for each in google_data: # explore data set
    name = each[0] # key
    n_reviews = float(each[3]) # value
    # if number of reviews equals the key/value of the dictionary add to list
    if n_reviews == reviews_max_android[name] and name not in android_added:
        android_clean.append(each)
        android_added.append(name) # in case there is a review max repeated
print(len(android_clean))

# Highest number of reviews APPLE

reviews_max_apple = {}

for each in apple_data:
    name = each[2]
    n_reviews = float(each[6])
    if name in reviews_max_apple and reviews_max_apple[name] < n_reviews:
        reviews_max_apple[name] = n_reviews
    elif name not in reviews_max_android:
        reviews_max_apple[name] = n_reviews

#APPLE CLEAN
apple_clean = [] # cleaned and chose the highest reviews
apple_added = []

for each in apple_data:
    name = each[2]
    n_reviews = float(each[6])
    if n_reviews == reviews_max_apple[name] and name not in apple_added:
        apple_clean.append(each)
        apple_added.append(name)

def ascii(string):
    n = 0
    English = True
    for each in string:
        if ord(each) > 127:
            n = n + 1
        if n > 3:
            English = False
    return English
apple_english = []
apple_non_english = []
google_english = []
google_non_english = []


'''for each in apple_clean:
    name = each[2]
    if ascii(name):
        apple_english.append(each)

for each in android_clean:
    name = each[0]
    if ascii(name):
        android_clean.append(each)
'''
print(android_clean[0])
print(apple_clean[0])