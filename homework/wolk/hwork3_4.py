
per1 = float (input ("Введите катет 1: "))
per2 = float (input ("Введите катет 2: "))

gipo = per1**2 + per2**2
plo = (per1 * per2) / 2

print("Гипотенуза = ", gipo ** .5)
print("Площадь треугольника: %.2f" % plo)