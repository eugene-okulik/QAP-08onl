class Flowers:
    def __init__(self, name, color, price, expiration_date=None):
        self.name = name
        self.color = color
        self.price = price
        self._expiration_date = expiration_date

    def show_name(self, name):
        self.name = name

    def flower_color(self, color):
        self.color = color

    def get_price(self, price):
        self.price = price

    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value


class Tulip (Flowers):
    def __init__(self, name=None, color=None, price=None, expiration_date=None):
        super().__init__(name, color, price, expiration_date)


class Orchid (Flowers):
    def __init__(self, name=None, color=None, price=None, expiration_date=None):
        super().__init__(name, color, price, expiration_date)


class Pion(Flowers):
    def __init__(self, name=None, color=None, price=None, expiration_date=None):
        super().__init__(name, color, price, expiration_date)


class Lily(Flowers):
    def __init__(self, name=None, color=None, price=None, expiration_date=None):
        super().__init__(name, color, price, expiration_date)


class FlowerBouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def make_bouquet(self):
        result = "Tulip", "Orchid", "Pion", "Lily"
        self.flowers.append(result)
        return f"The bouquet consists of: {result}"

    def bouquet_price(self):
        result = 0
        for flower in self.flowers:
            result += flower.price
        return f"The price of bouquet: {result}"

    def bouquet_term_life(self):
        result = 0
        for flower in self.flowers:
            result += flower.expiration_date / 4
        return result

    def find_name(self, name):
        result = []
        for flower in self.flowers:
            if flower.name == name:
                result.append(flower.name)
        return result

    def find_color(self, color):
        result = []
        for flower in self.flowers:
            if flower.color == color:
                result.append(flower.name)
        return result


tulip = Tulip("Tulip", "Yellow", 20, 5)
orchid = Orchid("Orchid", "White", 100, 15)
pion = Pion("Pion", "Pink", 50, 10)
lily = Lily("Lily", "White", 25, 18)
flowers1 = [tulip, orchid, pion, lily]
bouquet = FlowerBouquet(flowers1)
print(bouquet.find_color("White"))
print(bouquet.find_name("Pion"))
print(bouquet.bouquet_price())
print(bouquet.make_bouquet())
print(bouquet.bouquet_term_life())
