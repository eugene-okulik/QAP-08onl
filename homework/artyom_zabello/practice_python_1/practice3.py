SOME_STRING = 'my name is name'


def add_name(string):
    string = string.split(" ")
    string[3] = 'Artyom'
    return print(*string)


add_name(SOME_STRING)
