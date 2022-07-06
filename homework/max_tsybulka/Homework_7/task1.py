while True:
    number = int(input('Введите длину сдвига: '))
    str = input('Введите текст: ')
    alphabet = 'abcdefghijklmnopqrstuvwxyz' \
               'ABCDEFGHIJKLMNOPQRSTUVWXYZ'\
               'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'\
               'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    res = []
    ln = len(alphabet)
    n = '.\/[]{}()=-.,;:\'"1234567890~!`@#$%^&*<>?|=+_- '
    for l in str:
        if not l in n:
            res.append(alphabet[(alphabet.find(l)+number)%ln])
        else:
            res.append(l)
    print('Вывод: ' + ''.join(res))
