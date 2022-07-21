# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры цветов.
# Собрать букет (букет - еще один класс) (можно использовать аксессуары)
# с определением его стоимости.
# Для букета создать метод,
# который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни)
# (и это тоже метод).
# Узнать, есть ли цветок определенного типа в букете.


class Flowers:
    def __init__(self, color, freshness, name, price):
        self.color = color
        self.freshness = freshness
        self.name = name
        self.price = price

    def set_color(self, color):
        self.color = color

    def set_freshness(self, freshness):
        self.freshness = freshness

    def set_name(self, name):
        self.name = name

    def set_price(self, price):
        self.price = price


class Roses(Flowers):
    def __init__(self, color=None, freshness=None, name=None, price=None):
        super().__init__(color, freshness, name, price)


class Tulips(Flowers):
    def __init__(self, color=None, freshness=None, name=None, price=None):
        super().__init__(color, freshness, name, price)


class Peonys(Flowers):
    def __init__(self, color=None, freshness=None, name=None, price=None):
        super().__init__(color, freshness, name, price)


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
        return result if len(result) > 0 else 'There is no such color'

    def find_freshness(self, freshness):
        result = []
        for flower in self.flowers:
            if flower.freshness == freshness:
                result.append(flower.name)
        return result if len(result) > 0 else 'There is no such freshness'

    def find_name(self, name):
        result = []
        for flower in self.flowers:
            if flower.name == name:
                result.append(flower.name)
        return result if len(result) > 0 else 'There is no such flower'

    def find_price(self, price):
        result = []
        for flower in self.flowers:
            if flower.price == price:
                result.append(flower.name)
        return result if len(result) > 0 else 'There is no such price'


tulip = Tulips('pink', 5, 'Tulip', 8)
rose = Roses('red', 10, 'Rose', 11)
peony = Peonys('blue', 7, 'Peonys', 6)
flowers1 = [tulip, rose, peony]
flowers2 = [rose, peony]
flowers3 = [tulip, peony]
bouquet1 = Bouquet(flowers1)
bouquet2 = Bouquet(flowers2)
bouquet3 = Bouquet(flowers3)
print(bouquet1.find_freshness(7))
print(bouquet2.find_price(8))
print(bouquet1.find_color("blue"))
print(bouquet2.find_color('white'))
print(bouquet3.find_freshness(7))
print(bouquet1.price_bouquet())
print(bouquet3.bouquet_freshness())
print(bouquet2.price_bouquet())
