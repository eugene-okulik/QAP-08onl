from math import sqrt


num1 = 10
num2 = 15


def get_triangle(side1, side2):
    hypo = round(sqrt((side1**2)+(side2**2)), 2)
    area = (side1*side2) / 2
    return f"Гипотенуза = {hypo} \nПлощадь = {area}"


print(get_triangle(num1, num2))
