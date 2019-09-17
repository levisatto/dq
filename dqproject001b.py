from csv import reader

###Apple Data Set
open_apple_file = open('AppleStore.csv')
read_apple_file = reader(open_apple_file)
apple_data = list(read_apple_file)
apple_data_header = apple_data[0] # header
apple_data = apple_data[1:]

###Google Data Set
open_google_file = open('googleplaystore.csv')
read_google_file = reader(open_google_file)
google_data = list(read_google_file)
google_data_header = google_data[0] # header
google_data = google_data[1:]

def explore_data(dataset, start, end, row_col=False):
    dataset_explore = dataset[start:end]
    for each in dataset_explore:
        print(each)
    if row_col:
        print(f'Products:', {len(dataset)})
        print(f'Columns:', {len(dataset[0])})



### explore_data(apple_data,0,5,True)

def remove_error(dataset):
    for each in dataset:
        correct = len(dataset[0])
        length = len(each)
        if length != correct:
            print(dataset.index(each))


remove_error(google_data)
# Remove rows with errors
del google_data[10472]

# Duplicates

def duplicate(datase, pos):
    duplicate_apps = []
    unique_apps = []
    for each in datase:
        title = each[pos]
        if title in unique_apps:
            duplicate_apps.append(title)
        else:
            unique_apps.append(title)
    print('Duplicate items: ', len(duplicate_apps))
    print('Unique Items', len(unique_apps))

duplicate(google_data, 0)
duplicate(apple_data, 2)

### The higher the number of reviews, the more recent the data should be.
### Rather than removing duplicates randomly, we'll only keep the row with
### the highest number of reviews

### GOOGLE
def reviews_max_list(dataset, namecol, revcol):
    reviews_max = {}
    for each in dataset:
        name = each[namecol]
        n_reviews = float(each[revcol])
        if name in reviews_max and reviews_max[name] < n_reviews:
            reviews_max[name] = n_reviews
        elif name not in reviews_max:
            reviews_max[name] = n_reviews
    return  reviews_max
lista_review_google = reviews_max_list(google_data, 0, 3)
lista_review_apple = reviews_max_list(apple_data, 2, 6)

print('Lista com mais reviews Apple: ', len(lista_review_apple))
print('Lista com mais reviews Google: ', len(lista_review_google))

android_clean = [] # new cleaned data set
already_added = [] # app names
for each in google_data: # explore data set
    name = each[0] # key
    n_reviews = float(each[3]) # value
    # if number of reviews equals the key/value of the dictionary add to list
    if n_reviews == lista_review_google[name] and name not in already_added:
        android_clean.append(each)
        already_added.append(name) # in case there is a review max repeated
print(len(android_clean))

apple_clean = [] # new cleaned data set
apple_already_added = [] # app names
for each in apple_data: # explore data set
    name = each[2] # key
    n_reviews = float(each[6]) # value
    # if number of reviews equals the key/value of the dictionary add to list
    if n_reviews == lista_review_apple[name] and name not in apple_already_added:
        apple_clean.append(each)
        apple_already_added.append(name) # in case there is a review max repeated
print(len(apple_clean))

# English Only
def is_english(string):
    non_english = 0
    for each in string:
        if ord(each) > 127:
            non_english +=1
    if non_english > 3:
        return False
    else:
        return True

# Apple English
english_apple_data = []
for each in apple_clean:
    string = each[2]
    if is_english(string):
        english_apple_data.append(each)
print('English Apple data', len(english_apple_data))

# Android English
english_android_data = []
for each in android_clean:
    string = each[0]
    if is_english(string):
        english_android_data.append(each)
print('English Android data', len(english_android_data))


free_android_apps = []
for each in english_android_data:
    price = each[7]
    if price == '0':
        free_android_apps.append(each)

free_apple_apps = []
for each in english_apple_data:
    price = each[5]
    if price == '0':
        free_apple_apps.append(each)

print(len(free_apple_apps))
print(len(free_android_apps))

# android genre 9

# apple genre 12

def genre_count(dataset, col):
    genre_list = {}
    tot = 0
    for each in dataset:
        genre = each[col]
        if genre in genre_list:
            genre_list[genre] += 1
        else:
            genre_list[genre] = 1
            tot += 1
    return genre_list, tot
popopo = genre_count(free_apple_apps,12)
print(popopo)