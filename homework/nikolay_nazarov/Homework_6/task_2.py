# Реализуйте программу, которая спрашивала у пользователя,
# какую операцию он хочет произвести над числами,
# а затем запрашивает два числа и выводит результат
# Не забудьте о проверке деления на 0.

def calculator(num_1, num_2, action):
    """Возвращает результат действия над двумя числами"""
    result = None
    if action == 1:
        result = f"Сумма: {num_1 + num_2}"
    if action == 2:
        result = f"Разность: {num_1 - num_2}"
    if action == 3:
        result = f"Произведение: {num_1 * num_2}"
    if action == 4:
        if num_2 != 0:
            if num_1 % num_2 == 0:
                result = f"Частное: {num_1 / num_2}"
            if num_1 % num_2 != 0:
                result = f"Частное: {num_1 // num_2}, Остаток: {num_1 % num_2}"
        if num_2 == 0:
            result = "На ноль делить нельзя"
    else:
        result = "Ошибка ввода"
    return result


operation = int(input("Выберите операцию:\n" +
                      "1. Сложение\n"
                      "2. Вычитание\n"
                      "3. Умножение\n"
                      "4. Деление\n"
                      "Введите номер пункта меню:\n"))

first_num = int(input("Введите первое число:\n"))
second_num = int(input("Введите второе число:\n"))

print(calculator(first_num, second_num, operation))
