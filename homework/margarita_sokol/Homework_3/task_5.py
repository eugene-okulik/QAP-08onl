# Программa запрашивает у пользователя длину ребра куба.
# И находит объем кубa и площадь его боковой поверхности.

A = float(input('Введите длину ребра куба '))
V = A ** 3
S = A**2 * 4
print('Объем куба равен ' + str(V))
print('Площадь боковой поверхности куба равна ' + str(S))
