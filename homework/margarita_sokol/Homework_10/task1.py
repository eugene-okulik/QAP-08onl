# Создать классы цветов:
# общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры цветов. Собрать букет (букет - еще один класс),
# (можно использовать аксессуары) с определением его стоимости.
# Для букета создать метод, который определяет время его увядания
# по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).
# Узнать, есть ли цветок определенного типа в букете.

class Flower:
    def empty_public_method_1(self):
        pass

    def empty_public_method_2(self):
        pass


class Peonies(Flower):
    def __init__(self):
        self.name = 'Peony'
        self.hours = 12
        self.color = 'white'
        self.length = 40
        self.price = 710


class Tulips(Flower):
    def __init__(self):
        self.name = 'Tulip'
        self.hours = 40
        self.color = 'yellow'
        self.length = 20
        self.price = 450


class Freesia(Flower):
    def __init__(self):
        self.name = 'Freesia'
        self.hours = 10
        self.color = 'violet'
        self.length = 12
        self.price = 670


class Bouquet:
    def __init__(self, *flowers):
        self.includes = list(flowers)

    def price(self):
        start = 0
        for _ in self.includes:
            start += 1
        return start

    def total_price(self):
        start = 0
        for floret in self.includes:
            start += floret.price
        return start

    def bouquet_lifespan(self):
        start = 0
        for floret in self.includes:
            start += floret.hours
        return start // self.price()

    def search_by_color(self, color):
        for floret in self.includes:
            if floret.color == color:
                return floret.name
        return f'{color} flower missing'

    def search_by_length(self, stem_length):
        for floret in self.includes:
            if floret.length == stem_length:
                return floret.name
        return f'Missing flower with length {stem_length}'

    def search_by_price(self, price):
        for floret in self.includes:
            if floret.price == price:
                return floret.name
        return f'Missing flower with cost {price}'

    def search_by_flower(self, name):
        for floret in self.includes:
            if floret.name == name:
                return f'{name} is present in this bouquet'
        return f'Missing {name} in the bouquet'


Peonies1 = Peonies()
Tulips1 = Tulips()
Freesia1 = Freesia()
Bouquet1 = Bouquet(Peonies1, Tulips1, Freesia1)
print(Bouquet1.total_price())
print(Bouquet1.bouquet_lifespan())
print(Bouquet1.search_by_color('white'))
print(Bouquet1.search_by_length(12))
print(Bouquet1.search_by_price(670))
print(Bouquet1.search_by_flower('Tulip'))
