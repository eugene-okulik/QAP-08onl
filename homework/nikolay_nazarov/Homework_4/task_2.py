# Есть строка: test_string = "Hello world!",
# необходимо:
# вывести на экран на каком месте находится буква w
# кол-во букв “l”
# Проверить начинается ли строка с подстроки: “Hello”
# Проверить заканчивается ли строка подстрокой: “qwe”

TEST_STRING = "Hello world!"
W_POSITION = TEST_STRING.find("w") + 1
print(f"Буква \"w\" находится на {W_POSITION} позиции")
L_COUNT = TEST_STRING.count("l")
print(f"Количество букв \"l\" в слове \"Hello world!\" равно {L_COUNT} ")
if TEST_STRING.startswith("Hello"):
    print("Строка начинается со слова \"Hello\"")
else:
    print("Строка не начинается со слова \"Hello\"")
if TEST_STRING.endswith("qwe"):
    print("Строка заканчивается на \"qwe\"")
else:
    print("Строка не заканчивается на \"qwe\"")
