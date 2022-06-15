# Напишите функцию на вход которой подается строка, например,
# "cccbba" результат работы программы - строка “c3b2a".

TEXT = 'cccbba'
def stringcount(STRING):
    ENUMERATOR = 0
    STRING += ' '
    RESULT = ''
    for a in range(len(STRING) - 1):
        ENUMERATOR += 1
        LETTER = STRING[a]
        if STRING[a] != STRING[a + 1]:
            RESULT += LETTER
            if ENUMERATOR > 1:
                RESULT += str(ENUMERATOR)
            ENUMERATOR = 0
    return RESULT


print(stringcount(TEXT))
