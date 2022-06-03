# Создайте переменную с текстом “Mauris fringilla odio sit amet pretium ultricies. Pellentesque habitant morbi
# tristique”. извлеките из нее следующие срезы:
#     первые восемь символов
#     четыре символа из центра строки
#     символы с индексами кратными трем

my_string = 'Mauris fringilla odio sit amet pretium ultricies. Pellentesque ' \
            'habitant morbi tristique'

print(my_string[:8])

len_str = int(len(my_string) / 2)
print(my_string[len_str:len_str+4])

print(my_string[3::3])
