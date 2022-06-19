# Напишите программу: Есть функция которая делает одну и
# з арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции).
# Функция выглядит примерно так:
#
# def calc(first, second, operation):
#     if opertaion == '+':
#     .....
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор, который декорирует функцию
# calc и управляет тем какая операция будет произведена:
#
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

def my_dec(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res
    return wrapper

@my_dec
def calc(num1: int, num2: int):
    if num1 == num2:
        print(num1 + num2)

@my_dec
def calc2(num1: int, num2: int):
    if num1 > num2:
        print(num2 - num1)

@my_dec
def calc3(num1: int, num2: int):
    if num1 < num2:
        print(num1 / num2)

@my_dec
def calc4(num1: int, num2: int):
    if num1 < 0:
        print(num1 * num2)
    if num2 < 0:
        print(num1 * num2)

NUM1 = int(input("NUM1: "))
NUM2 = int(input("NUM2: "))

calc(NUM1, NUM2)
calc2(NUM1,NUM2)
calc3(NUM1,NUM2)
calc4(NUM1,NUM2)
