# Напишите функцию на вход которой подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

USER_STR = input("Введи текст из примера ниже: \n-cccbba\n-abeehhhhhccced\n-aaabbceedd\n-abcde\n-aaabbdefffff\n"
              "Ввод: ")


def count_letters(user_string):

    COUNT_INDEX = 1
    NEW_LIST = []
    NEW_STRING = ''

    for index in range(0, len(user_string) - 1):
        if user_string[index] == user_string[index + 1]:
            COUNT_INDEX += 1
        else:
            NEW_LIST.append({user_string[index]: COUNT_INDEX})
            COUNT_INDEX = 1

    for element in NEW_LIST:
        for key, value in element.items():
            NEW_STRING += key
            if value > 1:
                NEW_STRING += str(value)

    return NEW_STRING


RESULT = count_letters(USER_STR)

print(RESULT)


# Более элегантный способ решения заадчи

# s, r = input("Введи текст из примера ниже: \n-cccbba\n-abeehhhhhccced\n-aaabbceedd\n-abcde\n-aaabbdefffff\n"), ''
# while len(s): r += s[0] + str(len(s) - len(s.lstrip(s[0]))); s = s.lstrip(s[0])
# print(r)