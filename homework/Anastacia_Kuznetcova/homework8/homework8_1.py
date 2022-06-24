"""Внизу решение задания"""
a = int(input("Введите первое число "))
b = int(input("Введите второе число "))


def decorator(func):
    """Функция которая декорирует функцию calc и управляет, тем какая операция будет произведена"""

    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"

        elif first == second and not first < 0 and not second < 0:
            operation = "+"

        elif first > second and not first < 0 and not second < 0:
            operation = "-"

        elif second > first and not first < 0 and not second < 0:
            operation = "/"
        return func(first, second, operation)

    return wrapper


@decorator
def calc(first, second, operation):
    """Функция которая делает одну из арифметических операций с переданными ей числами"""
    solution = []
    if operation == '+':
        solution = (first + second)
    elif operation == '-':
        solution = (first - second)
    elif operation == '/':
        solution = (first / second)
    elif operation == "*":
        solution = (first * second)
    return solution


print(calc(a, b, '-'))
