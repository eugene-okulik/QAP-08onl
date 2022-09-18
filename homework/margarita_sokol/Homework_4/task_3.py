# Создайте переменную с текстом:

TEXT = 'Mauris fringilla odio sit amet pretium ultricies.' \
       'Pellentesque habitant morbi tristique'

# извлеките из нее следующие срезы:
# 1) первые восемь символов
# 2) четыре символа из центра строки
# 3) символы с индексами кратными трем

EX1 = TEXT[0:8]
print(EX1)

EX2 = int(len(TEXT) // 2)
A = len(TEXT) % 2
print(TEXT[EX2 + A - 2:EX2 + A + 2])

EX3 = TEXT[3::3]
print(EX3)
