# Есть строка: test_string = "Hello world!",
# необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”


test_string = "Hello world!"
print(test_string.find("w"))
print(test_string.count("l"))
if test_string.startswith('Hello'):
    print('Yes, this string contains this word!')

if test_string.endswith('qwe'):
    print('Yes,this string end with qwe')
else:
    print('No, there are no such letters.')
