NUMBER = 5
TEXT = int(input('Угадайте число. Введите цифру '))
while TEXT != NUMBER:
    TEXT = int(input('Попробуйте снова '))
if TEXT == NUMBER:
    print('Поздравляю! Вы угадали!')
