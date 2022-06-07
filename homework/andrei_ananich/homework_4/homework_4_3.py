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
print(len(A)/2)
print(A[43:47])
print(A[3::3])
