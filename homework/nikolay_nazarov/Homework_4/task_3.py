# Создайте переменную с текстом “Mauris fringilla odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”. извлеките из нее следующие срезы:
# - первые восемь символов
# - четыре символа из центра строки
# - символы с индексами кратными трем

SOME_TEXT = "Mauris fringilla odio sit amet pretium ultricies. " \
            "Pellentesque habitant morbi tristique"
print(SOME_TEXT[:8])
print(SOME_TEXT[int((len(SOME_TEXT)-1)/2-2):int((len(SOME_TEXT)-1)/2+2)])
print(SOME_TEXT[3::3])
