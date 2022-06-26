# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
#
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
#
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.

# Функция шифрования

PLAIN_TEXT = "Hello world77!"
DECODED_TEXT = "Khoor zruog00!"

def encode(text, key):
    encrypted = ""
    for letter in text:
        if letter.isupper(): #проверить, является ли символ прописным
            letter_index = ord(letter) - ord('A')
            # сдвиг текущего символа на позицию key
            letter_shifted = (letter_index + key) % 26 + ord('A')
            letter_new = chr(letter_shifted)
            encrypted += letter_new
        elif letter.islower():
            letter_index = ord(letter) - ord('a')
            letter_shifted = (letter_index + key) % 26 + ord('a')
            letter_new = chr(letter_shifted)
            encrypted += letter_new
        elif letter.isdigit():
            # если это число, сдвинуть его значение
            letter_new = (int(letter) + key) % 10
            encrypted += str(letter_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            encrypted += letter
    return encrypted

# Функция дешифрования
def decode(text, key):
    decrypted = ""
    for letter in text:
        if letter.isupper():
            letter_index = ord(letter) - ord('A')
            # сдвинуть текущий символ влево
            letter_og_pos = (letter_index - key) % 26 + ord('A')
            letter_og = chr(letter_og_pos)
            decrypted += letter_og
        elif letter.islower():
            letter_index = ord(letter) - ord('a')
            letter_og_pos = (letter_index - key) % 26 + ord('a')
            letter_og = chr(letter_og_pos)
            decrypted += letter_og
        elif letter.isdigit():
            letter_og = (int(letter) - key) % 10
            decrypted += str(letter_og)
        else:
            decrypted += letter
    return decrypted

print(encode(PLAIN_TEXT,3))
print(decode(DECODED_TEXT,3))
