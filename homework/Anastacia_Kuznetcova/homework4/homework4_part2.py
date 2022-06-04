# Есть строка: test_string = "Hello world!",
# необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”
TEST_STRING = "Hello world!"
FIND_W = TEST_STRING.find("w")
print(f"Индекс буквы 'w' = {FIND_W}")
STARTS_WITH_HELLO = TEST_STRING.startswith("Hello")
# return True
print(f"Проверка начинается ли строка с подстроки 'Hello = {STARTS_WITH_HELLO}")
print(f"Количество букв 'l' = {TEST_STRING.count('l')}")
ENDS_WITH_QWE = TEST_STRING.endswith("qwe")
# return True
print(f"Проверка заканчивается ли строка подстрокой 'qwe' = {ENDS_WITH_QWE}")