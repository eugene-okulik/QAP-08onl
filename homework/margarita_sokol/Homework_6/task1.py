# Напишите функцию на вход которой подается строка, например,
# "cccbba" результат работы программы - строка “c3b2a".

TEXT = 'cccbba'
def stringcount(string):
    enumerator = 0
    string += ' '
    result = ''
    for let in range(len(string) - 1):
        enumerator += 1
        letter = string[let]
        if string[let] != string[let + 1]:
            result += letter
            if enumerator > 1:
                result += str(enumerator)
            enumerator = 0
    return result


print(stringcount(TEXT))
