# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры цветов.
# Собрать букет (букет-еще один класс)/(можно использовать аксессуары) с определением его стоимости
# Для букета создать метод, который определяет время его увядания
# по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).
# Узнать, есть ли цветок определенного типа в букете.


class Flower:
    def __init__(self, name=None, age=None, price=None, color=None):
        self.name = name
        self.age = age
        self.price = price
        self.color = color

    def high_price(self):
        return 'high' if self.price > 7 else 'cheap'

    def fresh_flower(self):
        return 'fresh' if self.age < 3 else 'not fresh'


class Rose(Flower):
    def __init__(self, name, age=None, price=None, color=None):
        super().__init__(name, age, price, color)
        self.name = name
        self.age = age
        self.price = price
        self.color = color


class Orchid(Flower):
    def __init__(self, name, age=None, price=None, color=None):
        super().__init__(name, age, price, color)
        self.name = name
        self.age = age
        self.price = price
        self.color = color


class Tulip(Flower):
    def __init__(self, name, age=None, price=None, color=None):
        super().__init__(name, age, price, color)
        self.name = name
        self.age = age
        self.price = price
        self.color = color


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, b_flower):
        self.flowers.append(b_flower)

    def full_number_flowers(self):
        return len(self.flowers)

    def full_price(self):
        price = 0
        for b_flower in self.flowers:
            price = price + b_flower.price
        return price

    def age_of_bouquet(self):
        age = 0
        for b_flower in self.flowers:
            age = age + b_flower.age
        return age // self.full_number_flowers()

    def find_price_flower(self, price):
        result = []
        for b_flower in self.flowers:
            if b_flower.price == price:
                result.append(b_flower.name)
                return result
        return 'There is no such price'

    def find_color_flower(self, color):
        result = []
        for b_flower in self.flowers:
            if b_flower.color == color:
                result.append(b_flower.color)
                return result
        return 'There is no such color'

    def find_flower_bouquet(self, name):
        for b_flower in self.flowers:
            if b_flower.name == name:
                return 'This is flower in bouquet'
            return 'There is not such flower in bouquet'


flower = Flower()
bouquet = Bouquet()
rose = Rose(name='Rose', age=4, price=5, color='Red')
orchid = Orchid(name='Orchid', age=10, price=12, color='White')
tulip = Tulip(name='Tulip', age=7, price=9, color='Yellow')

bouquet.add_flower(rose)
bouquet.add_flower(orchid)
bouquet.add_flower(tulip)

print(bouquet.flowers)
print(bouquet.age_of_bouquet())
print(bouquet.find_color_flower('Red'))
print(bouquet.find_price_flower(9))
print(bouquet.find_flower_bouquet('Yellow'))
print(bouquet.full_price())
print(bouquet.full_number_flowers())
