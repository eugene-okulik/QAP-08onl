TEXT = ('Mauris fringilla odio sit amet pretium ultricies. '
        'Pellentesque habitant morbi tristique')


def symbols(text):
    lst = []
    print(text[0:8])
    print(text[round((len(text)/2)-2):round((len(text)/2)+2)])
    for i in text:
        if text.index(i) % 3 == 0:
            lst.append(i)
    print("".join(lst))


symbols(TEXT)
