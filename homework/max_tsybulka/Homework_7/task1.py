while True:
    NUMBER = int(input('Введите длину сдвига: '))
    STR = input('Введите текст: ')
    ALPHAVET = 'abcdefghijklmnopqrstuvwxyz' \
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
               'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'\
               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    res = []
    LN = len(ALPHAVET)
    N = '.[]{}()=-.,;:"1234567890~!`@#$%^&*<>?|=+_- '
    for l in STR:
        if not l in N:
            res.append(ALPHAVET[(ALPHAVET.find(l)+NUMBER)%LN])
        else:
            res.append(l)
    print('Вывод: ' + ''.join(res))
