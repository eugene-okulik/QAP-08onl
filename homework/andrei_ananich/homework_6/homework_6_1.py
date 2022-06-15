# Напишите функцию на вход которой подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
#
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

CHECK_STRING = "abeehhhhhccced"
count = {}
for s in CHECK_STRING:
    if s in count:
        count[s] += 1
    else:
        count[s] = 1

for key in count:
    if count[key] >= 1:
        print(key, count[key])
