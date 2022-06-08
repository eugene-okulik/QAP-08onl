# Есть строка: test_string = "Hello world!",
# необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

TEST_STRING = "Hello world!"
print(TEST_STRING.find("w"))
print(TEST_STRING.count("l"))
if TEST_STRING.startswith('Hello'):
    print('Yes, this string contains this word!')
else:
    print('Sorry, no this word')
if TEST_STRING.endswith('qwe'):
    print('Yes,this string end with qwe')
else:
    print('No, there are no such letters.')
