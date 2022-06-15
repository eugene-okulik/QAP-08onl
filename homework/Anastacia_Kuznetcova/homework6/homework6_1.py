"""
Решение с помощью функции
"""


def convert(my_string):
    """Возвращает укороченную строку, где повторяющиеся символы записываются как a2, a, a4"""
    my_string += '.'
    answer = ''  # Final result
    line_len = 0  # длина последовательности

    for i in range(len(my_string) - 1):
        line_len += 1
        cur_letter = my_string[i]

        if my_string[i] != my_string[i + 1]:
            answer += cur_letter
            if line_len > 1:
                answer += str(line_len)
            line_len = 0

    return answer


print(convert(input('Enter string: ')))
