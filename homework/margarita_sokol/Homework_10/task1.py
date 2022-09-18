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
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.hours = kwargs.get('hours')
        self.color = kwargs.get('color')
        self.length = kwargs.get('length')
        self.price = kwargs.get('price')

    def set_color(self, color):
        self.color = color

    def set_price(self, price):
        self.price = price


class Peonies(Flower):
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get('name'),
            hours=kwargs.get('hours'),
            color=kwargs.get('color'),
            length=kwargs.get('length'),
            price=kwargs.get('price')
        )


class Tulips(Flower):
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get('name'),
            hours=kwargs.get('hours'),
            color=kwargs.get('color'),
            length=kwargs.get('length'),
            price=kwargs.get('price')
        )


class Freesia(Flower):
    def __init__(self, **kwargs):
        super().__init__(
            name=kwargs.get('name'),
            hours=kwargs.get('hours'),
            color=kwargs.get('color'),
            length=kwargs.get('length'),
            price=kwargs.get('price')
        )


class Bouquet:
    def __init__(self):
        self.includes = []

    def add_flower(self, flower_):
        self.includes.append(flower_)

    def price(self):
        return len(self.includes)

    def total_price(self):
        start = 0
        for flower_ in self.includes:
            start += flower_.price
        return start

    def bouquet_lifespan(self):
        start = 0
        for flower_ in self.includes:
            start += flower_.hours
        return start // self.price()

    def search_by_color(self, color):
        start = []
        for flower_ in self.includes:
            if flower_.color == color:
                start.append(flower_.name)
                return start
        return f'{color} flower missing'

    def search_by_length(self, length):
        start = []
        for flower_ in self.includes:
            if flower_.length == length:
                start.append(flower_.name)
                return start
        return f'Missing flower with length {length}'

    def search_by_price(self, price):
        start = []
        for flower_ in self.includes:
            if flower_.price == price:
                start.append(flower_.name)
                return start
        return f'Missing flower with cost {price}'

    def search_by_flower(self, name):
        for flower_ in self.includes:
            if flower_.name == name:
                return f'{name} is present in this bouquet'
        return f'Missing {name} in the bouquet'

flower = Flower()
bouquet = Bouquet()
peonies = Peonies(name='Peony', hours=12, length=40, color='white', price=710)
tulips = Tulips(name='Tulip', hours=40, length=20, color='yellow', price=450)
freesia = Freesia(name='Freesia', hours=10, length=12, color='violet', price=670)
bouquet.add_flower(peonies)
bouquet.add_flower(tulips)
bouquet.add_flower(freesia)
print(bouquet.includes)
print(bouquet.bouquet_lifespan())
print(bouquet.search_by_color('white'))
print(bouquet.search_by_price(670))
print(bouquet.search_by_flower('Tulip'))
print(bouquet.price())
print(bouquet.total_price())
print(bouquet.search_by_length(12))
