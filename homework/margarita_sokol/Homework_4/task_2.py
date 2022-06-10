# Есть строка:

TEST_STRING = "Hello world!"

# необходимо: вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

LETTER_W = TEST_STRING.index('w')
print('Буква W находится на месте:', LETTER_W)

NUMBER_L = TEST_STRING.count('l')
print('Количество букв l равно:', NUMBER_L)

SUBSTRING1 = TEST_STRING.startswith('Hello')
print('Строка начинается с подстроки Hello:', SUBSTRING1)

SUBSTRING2 = TEST_STRING.endswith('qwe')
print('Строка начинается с подстроки qwe:', SUBSTRING2)
