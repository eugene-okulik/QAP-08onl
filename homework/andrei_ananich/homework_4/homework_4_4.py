# Создайте такую программу:
# Программа хранит какую-либо цифру в переменной
# Программа просит пользователя угадать цифру. Пользователь вводит цифру
# Программа сравнивает цифру с той, что хранится в переменной
# Если цифры не равны, программа пишет “попробуйте снова” и снова просит пользователя угадать цифру
# Если пользователь угадывает цифру, программа пишет “Поздравляю! Вы угадали!” и завершается.
# Т.е. программа не завершается пока пользователь не угадает цифру.

SECRET_NUMBER = 7
NUMBER = int(input('Угадайте число. Введите цифру'))
while NUMBER != SECRET_NUMBER:
    NUMBER = int(input('попробуйте снова'))
if NUMBER == SECRET_NUMBER:
    print('Поздравляю! Вы угадали!')