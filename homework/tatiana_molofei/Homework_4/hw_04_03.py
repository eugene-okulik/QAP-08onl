# Создайте переменную с текстом “Mauris fringilla odio sit amet
# pretium ultricies. Pellentesque habitant morbi
# tristique”. извлеките из нее следующие срезы:
#     первые восемь символов
#     четыре символа из центра строки
#     символы с индексами кратными трем

MY_STRING = 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque ' \
            'habitant morbi tristique'

print(MY_STRING[:8])

LEN_STR = int(len(MY_STRING) / 2)
print(MY_STRING[LEN_STR:LEN_STR+4])

print(MY_STRING[3::3])
