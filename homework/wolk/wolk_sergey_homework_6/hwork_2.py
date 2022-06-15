answare = input("Калькулятор : on/off")
while answare != 'off':
    simvol = input('Введите знак + - * /')
    chislo = int(input('Введите 1 число'))
    chislo2 = int(input('Введите 2 число'))
    if simvol == '+':
        print("Ответ:", chislo + chislo2)
    elif simvol == '-':
        print("Ответ:", chislo - chislo2)
    elif simvol == '*':
        print("Ответ:", chislo * chislo2)
    elif simvol == '/':
        if chislo2 != 0:
            print("Ответ:", chislo / chislo2)
        else:
            print("Деление на ноль")
print("Пока.")
