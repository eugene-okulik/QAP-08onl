# Программа запрашивает у пользователя длину ребра куба. И находит объем куба и площадь его
# боковой поверхности

cube_edge_length = int(input('Введите длину ребра куба '))
cube_volume = cube_edge_length ** 3
print(f'Объем куба равен {cube_volume}')

square_side_cube = cube_edge_length ** 2 * 6
print(f'Площадь боковой поверхности равна {square_side_cube}')
