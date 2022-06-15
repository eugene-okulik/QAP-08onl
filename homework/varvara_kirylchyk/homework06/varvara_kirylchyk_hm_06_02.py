# Реализуйте программу, которая спрашивала у пользователя,
# какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат
# Не забудьте о проверке деления на 0.
#
# Пример
#
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

A = int(input('Выберите операцию: 1. Сложение 2. Вычитание 3. Умножение '
              '4. Деление -> Введите номер пункта меню: '))
B = int(input('Введите первое число: '))
C = int(input('Введите второе число: '))

def validate_zero (something):
    if something == 0:
        return False
    return True

if not validate_zero(C):
    raise Exception("Деление на ноль")
#Валидация деления на ноль

def my_sum (num1, num2):
    return sum (num1, num2)

def my_diff (num1, num2):
    return num1 - num2

def my_mult (num1, num2):
    return num1 * num2

def my_div (num1, num2):
    return num1 // num2, num1 % num2

def calculation(opcode, op1, op2):
    if opcode == 1:
        result = my_sum(op1,op2)
        print(f"Сумма: {result}")
    elif opcode == 2:
        result = my_diff(op1, op2)
        print(f"Разность: {result}")
    elif opcode == 3:
        result = my_mult(op1, op2)
        print(f"Произведение: {result}")
    elif opcode == 4:
        result = my_div(op1, op2)
        print(f"Деление - Частное: {result[0]} Остаток: {result[1]}")
    else:
        result = None

    return result

func_res = calculation (A, B, C)
print(func_res)
