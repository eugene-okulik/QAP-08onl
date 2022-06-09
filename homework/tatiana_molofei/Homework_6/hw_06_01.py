# Напишите функцию на вход которой подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
#
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

STRING = "ccbbbbcbbaaacccbabab"


def user_string():
    print(f'"{STRING}" == "c{STRING.count("c")}b{STRING.count("b")}a{STRING.count("a")}"')


user_string()
