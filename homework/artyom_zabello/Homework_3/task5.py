def cube_length(side):
    volume = (side**2)*6
    area = (side**2)*4
    return f"Объем куба = {volume} \nПлощадь его боковой поверхности = {area}"


print(cube_length(int(input())))
