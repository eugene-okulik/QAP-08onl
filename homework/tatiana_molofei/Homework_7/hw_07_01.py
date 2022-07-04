# Шифр цезаря
# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ
# заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
# Напишите две функции - encode и decode принимающие как параметр строку
# и число - сдвиг. Знаки препинания должны сохраниться.
#

ALF_LOWER = 'abcdefghijklmnopqrstuvwxyz'
ALF_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

user_string = input()
user_step = int(input())


def encode(text, step):
    string_encoded = ''
    for i in text:
        if i in ALF_LOWER:
            i_index = ord(i) - ord('a')
            new_index = (i_index + step) % 26 + ord('a')
            string_encoded += chr(new_index)
        elif i in ALF_UPPER:
            i_index = ord(i) - ord('A')
            new_index = (i_index + step) % 26 + ord('A')
            string_encoded += chr(new_index)
        elif i.isdigit():
            string_encoded += str((int(i) + step) % 10)
        else:
            string_encoded += i
    return string_encoded


def decode(text, step):
    string_decoded = ''
    for i in text:
        if i in ALF_LOWER:
            i_index = ord(i) - ord('a')
            new_index = (i_index - step) % 26 + ord('a')
            string_decoded += chr(new_index)
        elif i in ALF_UPPER:
            i_index = ord(i) - ord('A')
            new_index = (i_index - step) % 26 + ord('A')
            string_decoded += chr(new_index)
        elif i.isdigit():
            string_decoded += str((int(i) - step) % 10)
        else:
            string_decoded += i
    return string_decoded


print(encode(user_string, user_step))
print(decode(user_string, user_step))
