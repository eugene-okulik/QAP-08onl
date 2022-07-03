class Flower:

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.lifetime = kwargs.get("lifetime")
        self.color = kwargs.get("color")
        self.length = kwargs.get("length")
        self.price = kwargs.get("price")

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


class Rose(Flower):
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get("name"),
            lifetime=kwargs.get("lifetime"),
            color=kwargs.get("color"),
            length=kwargs.get("length"),
            price=kwargs.get("price")
        )


class Gladiolus(Flower):
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get("name"),
            lifetime=kwargs.get("lifetime"),
            color=kwargs.get("color"),
            length=kwargs.get("length"),
            price=kwargs.get("price")
        )


class Iris(Flower):
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get("name"),
            lifetime=kwargs.get("lifetime"),
            color=kwargs.get("color"),
            length=kwargs.get("length"),
            price=kwargs.get("price")
        )


class Bouquet:
    def __init__(self):
        self.components = []

    def add_flower(self, _):
        self.components.append(_)

    def full_amount(self):
        return len(self.components)

    def full_price(self):
        res = 0
        for _ in self.components:
            res = res + _.price
        return res

    def lifetime_of_bouquet(self):
        res = 0
        for _ in self.components:
            res = res + _.lifetime
        return res // self.full_amount()

    def find_flower_by_color(self, color):
        res = []
        for _ in self.components:
            if _.color == color:
                res.append(_.name)
                return res
        return "Такого цвета нет"

    def find_price_of_flower(self, price):
        res = []
        for _ in self.components:
            if _.price == price:
                res.append(_.name)
                return res
        return "Нет цветка такой стоимости"

    def find_flower_in_bouquet(self, name):
        for i in self.components:
            if i.name == name:
                return "Этот цветок есть в букете"
            return "Нет такого цветка в букете"

    def find_flower_by_length(self, length):
        res = []
        for _ in self.components:
            if _.length == length:
                res.append(_.name)
                return res
        return "Нет цветка c такой длинной стебля в букете"


flower = Flower()
bouquet = Bouquet()
rose = Rose(name="Rose", lifetime=20, length=45, color="White", price=30)
gladiolus = Gladiolus(name="Gladiolus", lifetime=25, length=50, color="Red", price=15)
iris = Iris(name="Iris", lifetime=15, length=30, color="Orange", price=25)
bouquet.add_flower(rose)
bouquet.add_flower(gladiolus)
bouquet.add_flower(iris)
# rose.set_price(200) # сеттер изменения цены
# print(rose.price)
# iris.set_color("Yellow")
# print(iris.color) # сеттер изменения цвета
print(bouquet.components)
print(bouquet.lifetime_of_bouquet())
print(bouquet.find_flower_by_color("Red"))
print(bouquet.find_price_of_flower(30))
print(bouquet.find_flower_in_bouquet("Rose"))
print(bouquet.full_price())
print(bouquet.full_amount())
print(bouquet.find_flower_by_length(30))
