"""Представлены 4 функции для использования калькулятора"""
# Реализуйте программу, которая спрашивала у пользователя, какую операцию он хочет
# произвести над числами, а затем запрашивает два числа и выводит результат
# Не забудьте о проверке деления на 0.


def multiplication(num1, num2):
    """Данная функция выполняет операцию умножения"""
    return num1 * num2


def addition(num1, num2):
    """Данная функция выполняет операцию сложения"""
    return num1 + num2


def subtraction(num1, num2):
    """Данная функция выполняет операцию вычитания"""
    return num1 - num2


def divide(num1, num2):
    """Данная функция выполняет операцию деления"""
    return num1 // num2


print("Выберите операцию 1 - Деление, 2 - Умножение, 3 - Сложение, 4 - Вычитание")
operation = int(input("Введите операцию 1 2 3 4: "))
value1 = int(input("Введите первое число: "))
value2 = int(input("Введите второе число: "))

if operation == 1:
    if value2 == 0:
        print("Деление на ноль запрещено")
    else:
        print(f'Частное чисел равно {divide(value1, value2)} остаток равен {value1 % value2}')

elif operation == 2:
    print(f'Произведение чисел равно {multiplication(value1, value2)}')

elif operation == 3:
    print(f'Сумма чисел равна {addition(value1, value2)}')
elif operation == 4:
    print(f' Разность чисел равна {subtraction(value1, value2)}')
else:
    print('Операция была введена неверно')
