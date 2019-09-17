def ascii(string):
    n = 0
    English = True
    for each in string:
        if ord(each) > 127:
            n = n + 1
        if n > 3:
            English = False

    return English
print(ascii('Instagram'))

print(ascii('爱奇艺PPS -《欢乐颂2》电视剧热播'))

print(ascii('Docs To Go™ Free Office Suite'))

print(ascii('Instachat 😜'))