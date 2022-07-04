# Напишите функцию на вход которой подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

USER_STR = input("Введи текст из примера ниже: \n-cccbba"
                 "\n-abeehhhhhccced\n-aaabbceedd\n-abcde\n-aaabbdefffff\n"
                "Ввод: ")


def count_letters(user_string):

    count = 1
    list = []
    string = ''

    for index in range(0, len(user_string) - 1):
        if user_string[index] == user_string[index + 1]:
            count += 1
        else:
            list.append({user_string[index]: count})
            count = 1

    for element in list:
        for key, value in element.items():
            string += key
            if value > 1:
                string += str(value)

    return string


RESULT = count_letters(USER_STR)

print(RESULT)

# Более элегантный способ решения заадчи

# s, r = input("Введи текст из примера ниже: \n-cccbba\n-abeehhhhhccced\n-aaabbceedd\n-abcde\n-aaabbdefffff\n"), ''
# while len(s): r += s[0] + str(len(s) - len(s.lstrip(s[0]))); s = s.lstrip(s[0])
# print(r)
