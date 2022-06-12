# Создайте переменную с текстом “Mauris fringilla odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”. извлеките из нее следующие срезы:
#
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем


TEXT = 'Mauris fringilla odio sit amet pretium ultricies. ' \
    'Pellentesque habitant morbi tristique'
print(TEXT[:9])
A = len(TEXT)
B = int(A) / 2
print(round(B))
print(TEXT[int(B)-1:int(B)+3])
print(TEXT[3::3])
