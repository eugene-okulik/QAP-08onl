NUM = 9


def guessing():
    res = int(input("Угадайте цифру: "))
    while res != NUM:
        res = int(input("Попробуйте снова: "))
    if res == NUM:
        print("Поздравляю! Вы угадали!")


guessing()
