class Flower:
    def empty_public_method_1(self):  # добавила пустые методы чтобы пайлинт не ругался
        pass

    def empty_public_method_2(self):
        pass


class Rose(Flower):
    def __init__(self):
        self.flower_name = "Rose"
        self.color = "White"
        self.price = 450
        self.lifetime = 10
        self.stem_length = 75


class Gladiolus(Flower):

    def __init__(self):
        self.flower_name = "Gladiolus"
        self.color = "Pink"
        self.price = 100
        self.lifetime = 15
        self.stem_length = 80


class Iris(Flower):

    def __init__(self):
        self.flower_name = "Iris"
        self.color = "Orange"
        self.price = 250
        self.lifetime = 30
        self.stem_length = 60


class Bouquet:

    def __init__(self, *flowers):
        self.components = list(flowers)

    def full_amount(self):
        res = 0
        for _ in self.components:
            res = res + 1
        return res

    def full_price(self):
        res = 0
        for flower in self.components:
            res = res + flower.price
        return res

    def lifetime_of_bouquet(self):
        res = 0
        for flower in self.components:
            res = res + flower.lifetime
        return res // self.full_amount()

    def find_flower_by_color(self, color):
        for i in self.components:
            if i.color == color:
                return i.flower_name
        return "Такого цвета нет"

    def find_price_of_flower(self, price):
        for i in self.components:
            if i.price == price:
                return i.flower_name
        return "Нет цветка такой стоимости"

    def find_flower_in_bouquet(self, flower_name):
        for i in self.components:
            if i.flower_name == flower_name:
                return "Этот цветок есть в букете"
            return "Нет такого цветка в букете"

    def find_flower_by_stem_length(self, stem_length):
        for i in self.components:
            if i.stem_length == stem_length:
                return i.flower_name
        return "Нет цветка c такой длинной стебля в букете"


Flower = Flower()
Rose1 = Rose()
Gladiolus1 = Gladiolus()
Iris1 = Iris()
First_Bouquet = Bouquet(Rose1, Gladiolus1, Iris1)
print(First_Bouquet.components)
print(First_Bouquet.lifetime_of_bouquet())
print(First_Bouquet.find_flower_by_color("Orange"))
print(First_Bouquet.find_price_of_flower(450))
print(First_Bouquet.find_flower_in_bouquet("Rose"))
print(First_Bouquet.full_price())
print(First_Bouquet.full_amount())
print(First_Bouquet.find_flower_by_stem_length(60))
