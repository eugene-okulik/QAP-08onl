# Напишите программу. Есть 2 переменные salary и bonus. Salary - integer, bonus - boolean.
# Если bonus - true, salary должна быть умножена на 10. Если false - нет
# Примеры результатов:
# 10000, True == '$100000'
# 25000, True == '$250000'
# 10000, False == '$10000'
# 60000, False == '$60000'
# 2, True == '$20'
# 78, False == '$78'
# 67890, True == '$678900'

A = 78
B = True
if B is True:
    print(A * 10)
B = False
if B is False:
    print(A)
