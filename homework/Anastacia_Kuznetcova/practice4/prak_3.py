# Создайте текстовую переменную “my name is name”. Напечатайте ее, но вместо 2ого
# “name” вставьте ваше имя
MY_NAME_IS = "my name is name"
my_list = MY_NAME_IS.split()
element_3 = my_list.pop(3)
my_list.insert(4, 'stassia92')
NO_DOTS = ' '.join(my_list)
print(NO_DOTS)
