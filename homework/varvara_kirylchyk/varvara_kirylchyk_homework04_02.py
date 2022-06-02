#Есть строка: test_string = "Hello world!",
#Необходимо:
#-вывести на экран на каком месте находится буква w
#кол-во букв “l”
#Проверить начинается ли строка с подстроки: “Hello”
#Проверить заканчивается ли строка подстрокой: “qwe”


TEST_STRING = "Hello world!"
print (TEST_STRING.find("w"))

COUNT = TEST_STRING.count('l')
print("The count of 'l' is ", COUNT)

if TEST_STRING.startswith ('Hello'):
    print ('Yes, it starts with "Hello"')
elif TEST_STRING.startswith ('qwe'):
    print ('Yes, it starts with "qwe"')
else:
    print("No")
