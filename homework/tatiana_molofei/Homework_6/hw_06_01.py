# Напишите функцию на вход которой подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
#
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

STRING = input()
NEW_DICT = {}

for i in STRING:
    if i not in NEW_DICT:
        NEW_DICT[i] = 1
    else:
        NEW_DICT[i] += 1

NEW_STRING = []
for key, item in NEW_DICT.items():
    NEW_STRING.append("{}{}".format(key.capitalize(), item))
RESULT = "".join(NEW_STRING)
print(RESULT)
