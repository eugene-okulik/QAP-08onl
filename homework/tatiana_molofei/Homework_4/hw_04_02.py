# Есть строка: test_string = "Hello world!", необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

TEST_STRING = "Hello world!"

print(TEST_STRING.index('w'))
print(TEST_STRING.count('l'))
print(TEST_STRING.startswith('Hello'))
print(TEST_STRING.endswith('qwe'))
