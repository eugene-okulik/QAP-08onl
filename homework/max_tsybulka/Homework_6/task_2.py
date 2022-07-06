# Реализуйте программу, которая спрашивала у пользователя,
# какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат
# Не забудьте о проверке деления на 0.
#
# Пример
# Выберите операцию:
#     1. Сложение
#     2. Вычитание
#     3. Умножение
#     4. Деление
# Введите номер пункта меню:
# 4
# Введите первое число:
# 10
# Введите второе число:
# 3
# Частное: 3, Остаток: 3
# Можете сделать все в одной функции, можете разделить на разные.

def calculator():
    while True:
        start = int(input('''Введите номер пункта меню:\n start
        1. Сложение\n
        2. Вычитание\n
        3. Умножение\n
        4. Деление\n
Ввод: '''))
        if start > 4 or start < 1:
            print("Не правильная операция, попробуйте еще раз")
        else:
            A = int(input("Введите первое число: "))
            B = int(input("Введите второе число: "))
            break
    if start == 1:
        print("Результат: ", A + B)
    elif start == 2:
        print("Результат: ", A - B)
    elif start == 3:
        print("Результат: ", A * B)
    elif start == 4:
        if B != 0:
            print(f"Результат: ", A / B)
        else:
            print("На ноль делить нельзя!")

calculator()

# Пример без создания функции и более короткое решение

# X = int(input('''Введите номер пункта меню:\n
#         1. Сложение\n
#         2. Вычитание\n
#         3. Умножение\n
#         4. Деление\n
# Ввод: '''))
#
# A = int(input("Введите первое число: "))
# B = int(input("Введите второе число: "))
#
# if X == 1:
#     print(A + B)
# elif X == 2:
#     print(A - B)
# elif X == 3:
#     print(A * B)
# elif X == 4:
#     if B:
#         print(A / B)
#     else:
#         print("На ноль делить нельзя!")
