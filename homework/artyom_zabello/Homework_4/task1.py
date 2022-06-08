TEXT = ('Etiam tincidunt neque erat, quis molestie enim'
        'imperdiet vel. Integer urna nisl, facilisis vitae semper at,'
        'dignissim vitae libero')


def add_ing(text):
    text = text.replace(',', "").replace(".", "").split(" ")
    lst = []
    for i in text:
        lst.append(i+"ing")
    return print(str(lst).replace("[", "").replace("]", "").
                 replace("'", "").replace(",", ""))


add_ing(TEXT)
