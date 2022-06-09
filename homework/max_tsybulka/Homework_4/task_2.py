# Есть строка: test_string = "Hello world!",
# необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

HW = "Hello world!"

print(HW.index('w'))
print(HW.count('l'))
print(HW.startswith('Hello'))
print(HW.endswith('qwe'))
