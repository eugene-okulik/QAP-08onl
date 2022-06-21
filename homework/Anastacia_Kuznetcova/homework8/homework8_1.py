"""Внизу решение задания"""


def calc(first, second, operation):
    """Функция которая делает одну из арифметических операций с переданными ей числами"""
    if operation == '+':
        print(first + second)
    elif operation == '-':
        print(first - second)
    elif operation == '/':
        print(first / second)
    elif operation == "*":
        print(first * second)


def decorator(func, first, second):
    """Функция которая декорирует функцию calc и управляет, тем какая операция будет произведена"""

    def wrapper():
        if first < 0 or second < 0:
            func(first, second, "*")

        if first == second and not first < 0 and not second < 0:
            func(first, second, "+")

        if first > second and not first < 0 and not second < 0:
            func(first, second, "-")

        if second > first and not first < 0 and not second < 0:
            func(first, second, "/")

    return wrapper


a = int(input("Введите первое число "))
b = int(input("Введите второе число "))

new_func = decorator(calc, a, b)

new_func()
