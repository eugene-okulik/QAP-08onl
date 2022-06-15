# Напишите функцию на вход которой подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

user_string = f'{input()} '


def count_letters(user_string):

    count_index = 1
    new_list = []
    new_string = ''

    for index in range(0, len(user_string) - 1):
        if user_string[index] == user_string[index + 1]:
            count_index += 1
        else:
            new_list.append({user_string[index]: count_index})
            count_index = 1

    for element in new_list:
        for key, value in element.items():
            new_string += key
            if value > 1:
                new_string += str(value)

    return new_string


RESULT = count_letters(user_string)

print(RESULT)
