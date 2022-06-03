# Создайте переменную с текстом “Mauris fringilla odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”.
# извлеките из нее следующие срезы:
# первые восемь символов
# четыре символа из центра строки
# символы с индексами кратными трем
TEXT_1 = "Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi tristique"
NO_8_SYMBOLS = (TEXT_1[:8])
print(NO_8_SYMBOLS)
print(TEXT_1[int((len(TEXT_1)-1)/2-2):int((len(TEXT_1)-1)/2+2)])
print(TEXT_1[4::4])
