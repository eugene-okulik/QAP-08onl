# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.

# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl

# Напишите две функции - encode и decode принимающие
# как параметр строку и число - сдвиг. Знаки препинания должны сохраниться.

alfabet = "abcdefghijklmnopqrstuvwxyz"
decoded_alfabet = [i for i in alfabet]
a = "hello world!"
offset = 3

def decode(string, offset):
    i = 0
    decoded_string = ""
    while i < len(string):

        print(string[i])
        i += 1


print(decode(a, offset))
