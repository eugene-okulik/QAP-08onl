while True:
    NUMBER = int(input('Введите длину сдвига: '))
    STR = input('Введите текст: ')
    ALPHAVET = 'abcdefghijklmnopqrstuvwxyz' \
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
               'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'\
               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    res = []
    ln = len(ALPHAVET)
    n = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in STR:
        if not l in n:
            res.append(ALPHAVET[(ALPHAVET.find(l)+NUMBER)%ln])
        else:
            res.append(l)
    print('Вывод: ' + ''.join(res))
