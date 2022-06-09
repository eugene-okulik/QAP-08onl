NUM = 5

USNUM = int(input('Попробуйте угадать загаданную цифру. Введите любую цифру '))

while USNUM < NUM or USNUM > NUM:
    print("Попробуйте снова")
    USNUM = int(input('Попробуйте угадать загаданную цифру. Введите любую цифру '))
while USNUM == NUM:
    print("Поздравляю! Вы угадали!")
    break
