# Есть строка: test_string = "Hello world!",
# необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

MY_STRING = 'Hello world!'
print(MY_STRING.find('w'))
print(MY_STRING.count('l'))
print(MY_STRING.startswith('Hello'))
print(MY_STRING.endswith('qwe'))
