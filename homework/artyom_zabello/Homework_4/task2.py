TEST = "Hello world!"


def words(text):
    res1 = text.index("w")
    res2 = text.count("l")
    res3 = text.startswith("Hello")
    res4 = text.endswith("qwe")
    if res3 is True:
        stroka = "Строка начинается с Hello"
    else:
        stroka = "Строка не начинается с Hello"
    if res4 is True:
        stroka2 = "Строка заканчивается подстрокой - qwe"
    else:
        stroka2 = "Строка не заканчивается подстрокой - qwe"

    return print(f"Индекс буквы w = {res1} \nКоличество букв l = {res2} \n"
                 f"{stroka} \n{stroka2}")


words(TEST)

