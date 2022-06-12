STRING = input('enter different letters:')


def letter_count(user_str):
    count_let = 1
    result = ''
    for key, _ in enumerate(user_str):
        if key == len(user_str) - 1:
            if count_let == 1:
                result += user_str[key]
            else:
                result += user_str[key] + str(count_let)
            break
        if user_str[key] == user_str[key + 1]:
            count_let += 1
        else:
            if count_let == 1:
                result += user_str[key]
            else:
                result += user_str[key] + str(count_let)
            count_let = 1
    return result


print(letter_count(STRING))
