# Реализуйте программу, которая спрашивала у пользователя,
# какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат.
# Не забудьте о проверке деления на 0.

OPERATION_SELECTION = int(input('Выберите операцию:\n'
      '1. Сложение\n'
      '2. Вычитание\n'
      '3. Умножение\n'
      '4. Деление\n'
      'и введите номер пункта меню: '))
NUM1 = int(input('Введите первое число: '))
NUM2 = int(input('Введите второе число: '))

def calculator(NUM1, NUM2):
    if OPERATION_SELECTION == 1:
        return f'Результат суммы чисел: {(NUM1 + NUM2)}'
    elif OPERATION_SELECTION == 2:
        return f'Результат разности чисел: {(NUM1 - NUM2)}'
    elif OPERATION_SELECTION == 3:
        return f'Результат произведения чисел: {NUM1 * NUM2}'
    elif OPERATION_SELECTION == 4:
        if NUM2 == 0:
            return 'Деление на ноль невозможно!!!'
        return f'Частное от деления: {int(NUM1 // NUM2)}, остаток от деления: {int(NUM1 % NUM2)}'
    else:
        return 'Выбрана несуществующая операция!'


print(calculator(NUM1, NUM2))
