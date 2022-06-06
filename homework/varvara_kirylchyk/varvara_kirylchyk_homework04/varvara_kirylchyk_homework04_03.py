# Создайте переменную с текстом:
# “Mauris fringilla odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”.
# Извлеките из нее следующие срезы:
# 1) первые восемь символов
# 2) четыре символа из центра строки
# 3) символы с индексами кратными трем

MY_STRING = "Mauris fringilla odio sit amet pretium ultricies. " \
            "Pellentesque habitant morbi tristique"

COUNT = len(MY_STRING)

MY_STRING2 = MY_STRING[:8]
print(MY_STRING2)

MY_STRING3 = MY_STRING[80:84]
print(MY_STRING3)

for i in range (0, COUNT, 3):
    MY_STRING4 = MY_STRING[i]
    print(MY_STRING4)
