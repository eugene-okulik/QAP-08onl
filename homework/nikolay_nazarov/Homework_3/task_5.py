# Программа запрашивает у пользователя длину ребра куба.
# И находит объем куба и площадь его боковой поверхности

CUBE_EDGE = int(input("Введите длину ребра куба:\n"))
print("Объем куба равен:")
print(CUBE_EDGE**3)
print("Площадь боковой поверхности куба равен:")
print((CUBE_EDGE**2)*4)