# cоздайте переменную с текстом “Mauris fringilla
# odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”.
# извлеките из нее следующие срезы:
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем

TEXT = 'Mauris fringilla odio sit amet pretium ' \
       'ultricies.Pellentesque habitant morbi tristique'

MY_LIST = TEXT[:8]
print(MY_LIST)

MY_LIST_2 = TEXT[40:44]
print(MY_LIST_2)

print(TEXT[3::3])
