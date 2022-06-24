# Напишите программу:
# Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции). Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию calc
# и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

first_1 = int(input("Enter first number: "))
second_2 = int(input("Enter second number: "))


def decorator(func):
    def wrapper(first, second, operation):
        if first < 0 or second < 0:
            operation = "*"
        if first == second:
            operation = "+"
        if first > second:
            operation = "-"
        if first < second:
            operation = "/"
        return func(first, second, operation)

    return wrapper


@decorator
def calc(first, second, operation):
    if operation == "*":
        print(first * second)
    if operation == "+":
        print(first + second)
    if operation == "-":
        print(first - second)
    if operation == "/":
        print(first / second)

calc(first_1, second_2, decorator)
