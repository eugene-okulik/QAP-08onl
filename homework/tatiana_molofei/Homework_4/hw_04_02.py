# Есть строка: test_string = "Hello world!", необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

test_string = "Hello world!"

print(test_string.index('w'))
print(test_string.count('l'))
print(test_string.startswith('Hello'))
print(test_string.endswith('qwe'))
