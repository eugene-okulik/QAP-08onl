# Создайте переменную с текстом “Mauris fringilla odio sit amet pretium ultricies.
# Pellentesque habitant morbi tristique”.
# извлеките из нее следующие срезы:
# - первые восемь символов
# - четыре символа из центра строки
# - символы с индексами кратными трем

TEXT = "Mauris fringilla odio sit amet pretium ultricies. " \
            "Pellentesque habitant morbi tristique"

print(TEXT[:8])
print(TEXT[int((len(TEXT)-1)/2-2):int((len(TEXT)-1)/2+2)])
print(TEXT[3::3])
