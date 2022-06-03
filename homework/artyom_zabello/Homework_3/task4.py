from math import sqrt


NUM1 = 10
NUM2 = 15


def get_triangle(side1, side2):
    hypo = round(sqrt((side1**2)+(side2**2)), 2)
    area = (side1*side2) / 2
    return f"Гипотенуза = {hypo} \nПлощадь = {area}"


print(get_triangle(NUM1, NUM2))
