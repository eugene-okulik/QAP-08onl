# Напишите функцию на вход которой подается строка
# Например, "cccbba" результат работы программы - строка “c3b2a"

str1 = input("Input: ")

def count_letters(line):

    line += '\n'
    list01 = []
    str_length = len(line)
    res_string = ""

    counter = 1

    for i in range(0, str_length-1):
        if line[i] == line[i+1]:
            counter += 1
        else:
            list01.append({line[i]: counter})
            counter = 1
    #print(list01)

    for element in list01:
        for key, value in element.items():
            res_string += key
            if value > 1:
                res_string += str(value)

    return res_string

result = count_letters(str1)

print(f"Our result: {result}")
