# Создайте текстовую переменную “my name is name”.
# Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
NAME = 'my name is name'
STR = NAME.split(" ")
STR[3] = 'Sergey'
MY_NAME = " ".join(STR)
print(MY_NAME)
