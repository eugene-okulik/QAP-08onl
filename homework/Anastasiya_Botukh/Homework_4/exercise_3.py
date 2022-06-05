# cоздайте переменную с текстом “Mauris fringilla
# odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”.
# извлеките из нее следующие срезы:
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем

text = 'Mauris fringilla odio sit amet pretium ' \
       'ultricies.Pellentesque habitant morbi tristique'

my_list = text[:8]
print(my_list)

my_list_2 = text[40:44]
print(my_list_2)

print(text[3::3])
