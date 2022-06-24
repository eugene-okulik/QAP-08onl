# Напишите программу: Есть функция которая делает одну из арифметических
# операций с переданными ей числами (числа и операция передаются в
# аргументы функции). Функция выглядит примерно так:

# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc и управляет тем
# какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение
#
# first_num = int(input('Enter first number: '))
# second_num = int(input('Enter second number: '))


def decorator(func):
    def wrapper(first_num, second_num, operation):
        if first_num == second_num:
            operation = '+'
        if first_num > second_num:
            operation = '-'
        if first_num < second_num:
            operation = '/'
        if first_num < 0 or second_num < 0:
            operation = '*'
        return func(first_num, second_num, operation)

    return wrapper


@decorator
def calc(first_num, second_num, operation):
    if operation == '+':
        print(first_num + second_num)
    if operation == '-':
        print(first_num - second_num)
    if operation == '/':
        print(first_num / second_num)
    if operation == '*':
        print(first_num * second_num)


calc(int(input('Enter first number: ')), int(input('Enter second number: ')), decorator)
