# Создайте переменную с текстом
# извлеките из нее следующие срезы:
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем
LINE = 'Mauris fringilla odio sit amet pretium ultricies.Pellentesque habitant morbi tristique'
NO_8_SYMBOLS = (LINE[:8])
print(NO_8_SYMBOLS)
LEN = len(LINE)
HALF_LEN = LEN / 2
print(LINE[43:47])
print(LINE[3::3])
