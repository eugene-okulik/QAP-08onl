# Шифр Цезаря — один из древнейших шифров.
# При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
#
# Напишите две функции - encode и decode принимающие,
# как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.

_my_word = input('Enter your message: ').lower()
shift = int(input('Enter shift length: '))
ALPHABET = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
def encode(_my_word):
    result = ''
    for i in _my_word:
        if i in ALPHABET:
            position_now = ALPHABET.find(i)
            new_position = position_now + shift
            result += ALPHABET[new_position]
        else:
            result += i
    return result


print(encode(_my_word))


_my_word2 = input('Enter your message: ').lower()
shift2 = int(input('Enter shift length: '))
def decode(_my_word2):
    result2 = ''
    for i in _my_word2:
        if i in ALPHABET:
            position_now = ALPHABET.find(i)
            new_position = position_now - shift2
            result2 += ALPHABET[new_position]
        else:
            result2 += i
    return result2


print(decode(_my_word2))
