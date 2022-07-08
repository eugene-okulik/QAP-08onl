class Flowers:
    def __init__(self, name, colour, stem_length, price=None):
        self.name = name
        self.colour = colour
        self.stem_length = stem_length
        self.price = price

    def get_price(self):
        return f'Price: {self.price}$'

    def get_stem_lenght(self):
        return f'{self.name} the length is: {self.stem_length}'


class Roses(Flowers):
    def __init__(self, name, colour, stem_length, price):
        super().__init__(name, colour, stem_length, price)


class Chrysanthemum(Flowers):
    def __init__(self, name, colour, stem_length, price):
        super().__init__(name, colour, stem_length, price)


class Alstroemeria(Flowers):
    def __init__(self, name, colour, stem_length, price):
        super().__init__(name, colour, stem_length, price)


class Bouquet:
    def __init__(self):
        self.bouquet = []

    def make_bouquet(self, flower):
        self.bouquet.append(flower)

    def bouquet_price(self):
        result = 0
        for flower in self.bouquet:
            result += flower.price
        return f'{result}$'

    def get_colour(self, colour):
        result = []
        for flower in self.bouquet:
            if flower.colour == colour:
                result.append(flower.name)
                result = ''.join(result)
        return result

    def get_length(self, stem_length):
        result = []
        for flower in self.bouquet:
            if flower.stem_length == stem_length:
                result.append(flower.name)
                result = ''.join(result)
        return result


roses = Roses('Rose red', 'red', 25, 5)
chrysanthemum = Chrysanthemum('Chrysanthemum', 'White', 20, 3)
alstroemeria = Alstroemeria('Alstroemeria', 'green', 29, 1)
a = Bouquet()
a.make_bouquet(roses)
a.make_bouquet(chrysanthemum)
a.make_bouquet(alstroemeria)
print(a.get_colour('red'))
print(a.get_length(20))
print(a.bouquet_price())
print(roses.get_stem_lenght())
print(roses.get_price())
