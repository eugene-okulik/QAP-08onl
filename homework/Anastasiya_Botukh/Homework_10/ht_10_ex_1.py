class Flowers:
    def __init__(self, freshness, color, price, name):
        self.freshness = freshness
        self.color = color
        self.price = price
        self.name = name

    def get_flowers(self):
        return [self.freshness, self.color, self.price, self.name]


class Tulips(Flowers):
    def __init__(self, freshness, color, price, name):
        super().__init__(freshness, color, price, name)


class Roses(Flowers):
    def __init__(self, freshness, color, price, name):
        super().__init__(freshness, color, price, name)


class Orchids(Flowers):
    def __init__(self, freshness, color, price, name):
        super().__init__(freshness, color, price, name)


class Chamomiles(Flowers):
    def __init__(self, freshness, color, price, name):
        super().__init__(freshness, color, price, name)


class Cornflowers(Flowers):
    def __init__(self, freshness, color, price, name):
        super().__init__(freshness, color, price, name)


class Bouquet:
    def __init__(self, flowers):
        self.flowers = flowers

    def bouquet_freshness(self):
        total_freshness = 0
        for flower in self.flowers:
            total_freshness = total_freshness + flower.freshness
        return total_freshness / len(self.flowers)

    def price_bouquet(self):
        total_price = 0
        for flower in self.flowers:
            total_price = total_price + flower.price
        return total_price

    def find_color(self, color):
        result = []
        for flower in self.flowers:
            if flower.color == color:
                result.append(flower.name)
        return result if len(result) > 0 else 'there is no such color'  # тернарный оператор

    def find_name(self, name):
        result = []
        for flower in self.flowers:
            if flower.name == name:
                result.append(flower.name)
        return result if len(result) > 0 else 'there is no such flower'

    def find_price(self, price):
        result = []
        for flower in self.flowers:
            if flower.price == price:
                result.append(flower.name)
        return result if len(result) > 0 else 'there is no such price'

    def find_freshness(self, freshness):
        result = []
        for flower in self.flowers:
            if flower.freshness == freshness:
                result.append(flower.name)
        return result if len(result) > 0 else 'there is no such freshness'


tulip = Tulips(7, 'pink', 5, 'Tulip')
rose = Roses(5, 'red', 10, 'Rose')
orchid = Orchids(10, 'white', 15, 'Orchid')
chamomile = Chamomiles(4, 'blue', 8, 'Chamomile')
cornflower = Cornflowers(13, 'purple', 7, 'Cornflower')
flowers1 = [tulip, rose, orchid, chamomile, cornflower]
flowers2 = [rose, orchid, cornflower]
flowers3 = [tulip, chamomile]
bouquet1 = Bouquet(flowers1)
bouquet2 = Bouquet(flowers2)
bouquet3 = Bouquet(flowers3)
print(bouquet1.find_freshness(10))
print(bouquet2.find_price(8))
print(bouquet1.find_color("blue"))
print(bouquet2.find_color('white'))
print(bouquet3.find_freshness(7))
print(bouquet1.price_bouquet())
print(bouquet3.bouquet_freshness())
print(bouquet2.price_bouquet())
