# Шифр Цезаря — один из древнейших шифров. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.
#
# Примеры:
# hello world! -> khoor zruog!
# this is a test string -> ymnx nx f yjxy xywnsl
#
# Напишите две функции - encode и decode принимающие как параметр строку и число - сдвиг.
# Знаки препинания должны сохраниться.


CLEAR_TEXT = "hello world!"
DECODED_TEXT = "khoor zruog!"
# Функция шифрования
def encrypt(clear_text, key):
    encrypted = ""
    for letters in clear_text:
        if letters.isupper(): #проверить, является ли символ прописным
            letters_index = ord(letters) - ord('A')
            # сдвиг текущего символа на позицию key
            letters_shifted = (letters_index + key) % 26 + ord('A')
            letters_new = chr(letters_shifted)
            encrypted += letters_new
        elif letters.islower(): #проверка наличия символа в нижнем регистре
            # вычесть юникод 'a', чтобы получить индекс в диапазоне [0-25)
            letters_index = ord(letters) - ord('a')
            letters_shifted = (letters_index + key) % 26 + ord('a')
            letters_new = chr(letters_shifted)
            encrypted += letters_new
        elif letters.isdigit():
            # если это число, сдвинуть его фактическое значение
            letters_new = (int(letters) + key) % 10
            encrypted += str(letters_new)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            encrypted += letters
    return encrypted
# Функция дешифрования
def decrypt(ciphertext, key):
    decrypted = ""
    for letters in ciphertext:
        if letters.isupper():
            letters_index = ord(letters) - ord('A')
            # сдвигаем текущий символ влево, чтобы получить его исходное положение
            letters_og_pos = (letters_index - key) % 26 + ord('A')
            letters_og = chr(letters_og_pos)
            decrypted += letters_og
        elif letters.islower():
            letters_index = ord(letters) - ord('a')
            letters_og_pos = (letters_index - key) % 26 + ord('a')
            letters_og = chr(letters_og_pos)
            decrypted += letters_og
        elif letters.isdigit():
            # если это число, сдвиньте его фактическое значение
            letters_og = (int(letters) - key) % 10
            decrypted += str(letters_og)
        else:
            # если нет ни алфавита, ни числа, оставьте все как есть
            decrypted += letters
    return decrypted

print(encrypt(CLEAR_TEXT,3))
print(decrypt(DECODED_TEXT,3))
