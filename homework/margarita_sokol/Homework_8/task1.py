# Напишите программу: Есть функция которая делает одну из
# арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции).
# Программа спрашивает у пользователя 2 числа (вне функции).
# Создайте декоратор, который декорирует функцию calc
# и управляет тем какая операция будет произведена:
# 1) если числа равны, то функция calc вызывается
# с операцией сложения этих чисел
# 2) если первое больше второго, то происходит
# вычитание второго из певрого
# 3) если второе больше первого - деление первого на второе
# 4) если одно из чисел отрицательное - умножение.

_first = int(input('Enter first number: '))
_second = int(input('Enter second number: '))

def decarator(func):
    def wrapeer(_first, _second, operation):
        if _first == _second:
            operation = '+'
        if _first > _second:
            operation = '-'
        if _second > _first:
            operation = '/'
        if _first < 0 or _second < 0:
            operation = '*'
        return func(_first, _second, operation)

    return wrapeer


@decarator
def calc(_first, _second, operation):
    if operation == '+':
        print(_first + _second)
    if operation == '-':
        print(_second - _first)
    if operation == '/':
        print(_first / _second)
    if operation == '*':
        print(_first * _second)

calc(_first, _second, decarator)
