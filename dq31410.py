content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
for each in content_ratings:
    content_ratings[each] /= total_number_of_apps
    content_ratings[each] *= 100

percentage_17_plus = content_ratings['17+']
percentage_15_allowed = 100 - percentage_17_plus

print(f'{percentage_17_plus:5.2f}%')
print(f'{percentage_15_allowed:5.2f}%')