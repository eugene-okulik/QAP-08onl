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
_first_num = int(input('Введите первое число: '))
_second_num = int(input('Введите второе число: '))

def calculator(_first_num, _second_num):
    if OPERATION_SELECTION == 1:
        print(f'Результат суммы чисел: {(_first_num + _second_num)}')
    elif OPERATION_SELECTION == 2:
        print(f'Результат разности чисел: {(_first_num - _second_num)}')
    elif OPERATION_SELECTION == 3:
        print(f'Результат произведения чисел: {_first_num * _second_num}')
    elif OPERATION_SELECTION == 4:
        if _second_num == 0:
            print('Деление на ноль невозможно!!!')
        else:
            print(f'Частное от деления: {int(_first_num // _second_num)}, '
                  f'остаток от деления: {int(_first_num % _second_num)}')


calculator(_first_num, _second_num)
