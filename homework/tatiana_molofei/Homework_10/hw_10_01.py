# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры цветов. Собрать букет (букет - еще один класс)
# (можно использовать аксессуары) с определением его стоимости.
# Для букета создать метод, который определяет время его увядания
# по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).
# Узнать, есть ли цветок определенного типа в букете.


class Flowers:
    def __init__(self, name, colour=None, length=None, lifetime=None, price=None):
        self.name = name
        self.colour = colour
        self.length = length
        self.lifetime = lifetime
        self.price = price

    def flower_freshness(self):
        return ' is not fresh' if self.lifetime < 3 else ' is fresh'

    def flower_price(self):
        return ' is cheap' if self.price < 150 else ' is expensive'


class ExoticFlowers(Flowers):
    def __init__(self, name, colour=None, length=None, lifetime=None, price=None):
        super().__init__(name, colour, length, lifetime, price)


class GardenFlowers(Flowers):
    def __init__(self, name, colour=None, length=None, lifetime=None, price=None):
        super().__init__(name, colour, length, lifetime, price)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def bouquet_price(self):
        full_price = 0
        for flower in self.flowers:
            full_price += flower.price
        return full_price

    def average_age(self):
        av_age = 0
        for flower in self.flowers:
            av_age = (av_age + flower.lifetime) / len(self.flowers)
        return av_age

    def get_colour(self, colour):
        flower_colour = []
        for flower in self.flowers:
            if flower.colour == colour:
                flower_colour.append(flower.name)
        return flower_colour

    def bouquet_freshness(self):
        av_bouquet_age = 0
        for flower in self.flowers:
            av_bouquet_age = (av_bouquet_age + flower.lifetime) / len(self.flowers)
        return 'Bouquet is not fresh' if av_bouquet_age < 5 else 'Bouquet is fresh'

    @staticmethod
    def flower_price(price):
        return ' is cheap' if price < 150 else ' is expensive'


flower1 = ExoticFlowers('Anthurium', 'red', 15, 5, 50)
flower2 = ExoticFlowers('Arabis', 'blue', 10, 10, 100)
flower3 = ExoticFlowers('Calla lily', 'rose', 10, 20, 400)
flower4 = ExoticFlowers('Amaranth', 'green', 15, 15, 250)
flower5 = ExoticFlowers('Aster', 'green', 15, 5, 50)

flower6 = GardenFlowers('Rose', 'red', 15, 5, 120)
flower7 = GardenFlowers('Zinnia', 'white', 15, 10, 150)
flower8 = GardenFlowers('Peony', 'white', 20, 15, 220)
flower9 = GardenFlowers('Tulip', 'red', 20, 2, 80)
flower10 = GardenFlowers('Ranunculus', 'yellow', 15, 5, 150)


bouquet1 = Bouquet()

bouquet1.add_flower(flower1)
bouquet1.add_flower(flower7)
bouquet1.add_flower(flower5)
bouquet1.add_flower(flower5)
bouquet1.add_flower(flower9)

print(f'The total price of a bouquet is {bouquet1.bouquet_price()} rubles')
print(f'The average life of a bouquet is {round(bouquet1.average_age(), 2)} days')
print(bouquet1.get_colour('red'))
print(f'Flower {flower9.name} {flower9.flower_freshness()}')
print(bouquet1.bouquet_freshness())
