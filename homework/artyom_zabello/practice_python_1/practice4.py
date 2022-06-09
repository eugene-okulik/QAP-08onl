SOME_STRING = 'Ivanov Ivan'


def reversed_value(text):
    text = list(text.split(" "))
    text.reverse()
    return print(*text)


reversed_value(SOME_STRING)
