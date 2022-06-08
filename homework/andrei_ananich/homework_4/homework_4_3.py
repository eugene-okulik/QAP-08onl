# Создайте переменную с текстом
# “Mauris fringilla odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”.
# извлеките из нее следующие срезы:
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем

A = 'Mauris fringilla odio sit amet pretium ultricies.\
Pellentesque habitant morbi tristique'
print(A[0:8])

LEN_STRING = int(len(A) / 2)
print(A[LEN_STRING:LEN_STRING+4])
print(A[3::3])
