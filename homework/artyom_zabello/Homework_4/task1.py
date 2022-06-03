TEXT = ('Etiam tincidunt neque erat, quis molestie enim'
        'imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
        'dignissim vitae libero')


def add_ing(text):
    text = text.replace(',', "").replace(".", "").split(" ")
    lst = list()
    for i in text:
        lst.append(i+"ing")
    return print(lst)


add_ing(TEXT)

