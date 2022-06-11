# Напишите программу. Есть 2 переменные salary и bonus. Salary - integer, bonus - boolean.
# Если bonus - true, salary должна быть умножена на 10. Если false - нет.

SALARY = 10000
BONUS = False
if BONUS == True:
    print('$' + str(SALARY * 10))
elif BONUS == False:
    print('$' + str(SALARY))
