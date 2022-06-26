# Напишите функцию на вход которой подается строка, например, "cccbba"
# результат работы программы - строка “c3b2a"
#
# Примеры для проверки работоспособности:
# "cccbba" == "c3b2a"
# "abeehhhhhccced" == "abe2h5c3ed"
# "aaabbceedd" == "a3b2ce2d2"
# "abcde" == "abcde"
# "aaabbdefffff" == "a3b2def5"

# count = {}
# for s in CHECK_STRING:
#     if s in count:
#         count[s] += 1
#     else:
#         count[s] = 1
#
# for key in count:
#     if count[key] >= 1:
#         print(key, count[key])

# CHECK_STRING = "abeehhhhhccced"

CHECK_STRING = "abeehhhhhccced"

def letter_count(check_str):
    count_let = 1
    result = ''
    for key, _ in enumerate(check_str):
        if key == len(check_str) - 1:
            if count_let == 1:
                result += check_str[key]
            else:
                result += check_str[key] + str(count_let)
            break
        if check_str[key] == check_str[key + 1]:
            count_let += 1
        else:
            if count_let == 1:
                result += check_str[key]
            else:
                result += check_str[key] + str(count_let)
            count_let = 1
    return result


print(letter_count(CHECK_STRING))
