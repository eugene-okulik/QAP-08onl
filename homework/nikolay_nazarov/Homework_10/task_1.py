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


class Verbena(Flower):
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get("name"),
            lifetime=kwargs.get("lifetime"),
            color=kwargs.get("color"),
            length=kwargs.get("length"),
            price=kwargs.get("price")
        )


class Peony(Flower):
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

    def add_flower(self, flower_):
        self.components.append(flower_)

    def full_amount(self):
        return len(self.components)

    def full_price(self):
        res = 0
        for flower_ in self.components:
            res = res + flower_.price
        return res

    def lifetime_of_bouquet(self):
        res = 0
        for flower_ in self.components:
            res = res + flower_.lifetime
        return res // self.full_amount()

    def find_flower_by_color(self, color):
        res = []
        for flower_ in self.components:
            if flower_.color == color:
                res.append(flower_.name)
                return res
        return "Такого цвета нет"

    def find_price_of_flower(self, price):
        res = []
        for flower_ in self.components:
            if flower_.price == price:
                res.append(flower_.name)
                return res
        return "Нет цветка такой стоимости"

    def find_flower_in_bouquet(self, name):
        for flower_ in self.components:
            if flower_.name == name:
                return "Этот цветок есть в букете"
            return "Нет такого цветка в букете"

    def find_flower_by_length(self, length):
        res = []
        for flower_ in self.components:
            if flower_.length == length:
                res.append(flower_.name)
                return res
        return "Нет цветка c такой длинной стебля в букете"


flower = Flower()
bouquet = Bouquet()
rose = Rose(name="Rose", lifetime=50, length=40, color="Blue", price=200)
verbena = Verbena(name="Verbena", lifetime=25, length=50, color="Red", price=150)
peony = Peony(name="Peony", lifetime=15, length=30, color="Orange", price=100)
bouquet.add_flower(rose)
bouquet.add_flower(verbena)
bouquet.add_flower(peony)
print(bouquet.components)
print(bouquet.lifetime_of_bouquet())
print(bouquet.find_flower_by_color("Red"))
print(bouquet.find_price_of_flower(200))
print(bouquet.find_flower_in_bouquet("Rose"))
print(bouquet.full_price())
print(bouquet.full_amount())
print(bouquet.find_flower_by_length(30))
