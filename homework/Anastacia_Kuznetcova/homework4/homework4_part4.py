# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной.
# Программа просит пользователя угадать цифру. Пользователь вводит цифру.
# Программа сравнивает цифру с той, что хранится в переменной.
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру.
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.
NUM = 9
GUESS = -1
while GUESS != NUM:
    GUESS = int(input("Угадайте число! "))
    if GUESS > NUM:
        print("Попробуйте снова")
    elif GUESS < NUM:
        print("Попробуйте снова")
    else:
        print("Поздравляю! Вы угадали!")