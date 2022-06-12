def calculator():
    """Simple calculator"""
    while True:
        res = int(input('''Введите номер пункта меню:\n
        1. Сложение\n
        2. Вычитание\n
        3. Умножение\n
        4. Деление\n'''))
        if res > 4 or res < 1:
            print("Не правильная операция, попробуйте еще раз")
        else:
            num1 = int(input("Введите первое число "))
            num2 = int(input("Введите второе число "))
            break
    if res == 1:
        print("Результат: ", num1+num2)
    elif res == 2:
        print("Результат: ", num1-num2)
    elif res == 3:
        print("Результат: ", num1*num2)
    elif res == 4:
        if num2 != 0:
            print(f"Результат: частное:{num1//num2} остаток: {num1%num2}")
        else:
            print("На ноль делить нельзя")


calculator()
