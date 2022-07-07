# Напишите программу:
# Есть функция которая делает одну из арифметических операций с переданными ей числами
# (числа и операция передаются в аргументы функции).
# Программа спрашивает у пользователя 2 числа (вне функции)
# Создайте декоратор,
# который декорирует функцию calc и управляет тем какая операция будет произведена:
# если числа равны, то функция calc вызывается с операцией сложения этих чисел
# если первое больше второго, то происходит вычитание второго из певрого
# если второе больше первого - деление первого на второе
# если одно из чисел отрицательное - умножение

number_1 = int(input("Введите первое число: "))
number_2 = int(input("Введите второе число: "))


def dec(func):
    """A dummy docstring"""
    def wrapper(one, two, operation):
        if one < 0 or two < 0:
            operation = "*"
        elif one == two:
            operation = "+"
        elif one > two:
            operation = "-"
        elif one < two:
            operation = "/"
        return func(one, two, operation)

    return wrapper


@dec
def calc(one, two, operation):
    """A dummy docstring"""
    if operation == "*":
        print(one * two)
    elif operation == "+":
        print(one + two)
    elif operation == "-":
        print(one - two)
    elif operation == "/":
        print(one / two)


calc(number_1, number_2, dec)
