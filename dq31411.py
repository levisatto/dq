content_ratings = {'4+': 4433, '12+': 1155, '9+': 987, '17+': 622}
total_number_of_apps = 7197
c_ratings_proportions = {}
c_ratings_percentages = {}
for each in content_ratings:
    proportion = content_ratings[each] / total_number_of_apps
    percentage = proportion * 100
    c_ratings_proportions[each] = proportion
    c_ratings_percentages[each] = percentage
print(c_ratings_percentages)
print(c_ratings_proportions)