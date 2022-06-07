# Создайте текстовую переменную “my name is name”.
# Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.

MSG = "my name is name"
LIST = MSG.split(" ")
LIST[3] = "Varvara"
FINAL_STRING = " ".join(LIST)
print(FINAL_STRING)
