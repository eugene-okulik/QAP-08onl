TEXT = ('Mauris fringilla odio sit amet pretium ultricies. '
        'Pellentesque habitant morbi tristique')


def symbols(text):
    lst = list()
    print(text[0:8])
    print(text[42:46])
    for i in range(len(text)):
        if i % 3 == 0:
            lst.append(text[i])
    print("".join(lst))


symbols(TEXT)
