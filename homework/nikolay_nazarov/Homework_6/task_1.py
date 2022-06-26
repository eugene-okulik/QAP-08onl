# Напишите функцию на вход которой подается строка, например,
# "cccbba" результат работы программы - строка “c3b2a"
# Похожую задачу решал на степике https://stepik.org/lesson/3367/step/7?unit=950

STRING = "cccbbbba"


def string_refactor(some_string):
    """Возвращает укороченную строку, где повторяющиеся символы записываются как a2, a, a4"""
    i = 0
    count = 0
    string_modded = ""
    while i < len(some_string):
        if i == 0 and len(some_string) != 1:
            count += 1
        elif some_string[i] == some_string[i - 1] and i != len(some_string) - 1:
            count += 1
        elif some_string[i] != some_string[i - 1]:
            if count != 1:
                string_modded += some_string[i - 1] + str(count)
                count = 1
            else:
                string_modded += some_string[i - 1]
                count = 1
        i += 1
    if i == len(some_string) and some_string[i - 1] != some_string[i - 2]:
        count = 1
        string_modded += some_string[i - 1]
    elif i == len(some_string):
        count += 1
        string_modded += some_string[i - 1] + str(count)
    return string_modded


print(string_refactor(STRING))
