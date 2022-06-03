NUM = 9


def guessing(number):
    res = int(input("Угадайте цифру: "))
    while res != number:
        res = int(input("Попробуйте снова: "))
    if res == number:
        print("Поздравляю! Вы угадали!")


guessing(NUM)
