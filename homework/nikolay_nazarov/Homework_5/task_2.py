# Напишите программу. Есть 2 переменные salary и bonus. Salary - integer, bonus - boolean.
# Если bonus - true, salary должна быть умножена на 10. Если false - нет

SALARY = 1000
BONUS = False

if BONUS:
    print(f"{SALARY}, {BONUS} == '${SALARY * 10}'")
else:
    print(f"{SALARY}, {BONUS} == '${SALARY}'")
