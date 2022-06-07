#Есть строка: test_string = "Hello world!",
#Необходимо:
#1 вывести на экран на каком месте находится буква w
#2 кол-во букв “l”
#3 Проверить начинается ли строка с подстроки: “Hello”
#4 Проверить заканчивается ли строка подстрокой: “qwe”


TEST_STRING = "Hello world!"
print(TEST_STRING.find("w"))

COUNT = TEST_STRING.count('l')
print("The count of 'l' is ", COUNT)

if TEST_STRING.startswith ('Hello'):
    print('Yes, it starts with "Hello"')
if TEST_STRING.startswith ('qwe'):
    print('Yes, it starts with "qwe"')
else:
    print("No")
