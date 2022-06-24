# Цветочница
#
# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры цветов.

# Собрать букет (букет - еще один класс) (можно использовать аксессуары)
# с определением его стоимости.

# Для букета создать метод,
# который определяет время его увядания по среднему времени жизни всех цветов в букете.
#
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)

# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).

# Узнать, есть ли цветок определенного типа в букете.

class Plant:
    def __init__(self, name=None, age=None, color=None, price=None):
        self.name = name
        self.age = age
        self.color = color
        # self.length = length
        self.price = price

    def is_expensive(self):
        return 'expensive' if self.price > 10 else 'cheap'

    def is_fresh(self):
        return 'fresh' if self.age < 5 else 'not fresh'

class Flower(Plant):
    def __init__(self, name, age=None, color=None, price=None):
        super().__init__(name, age, color, price)

class Flower2(Plant):
    def __init__(self, name, age=None, color=None, price=None):
        super().__init__(name, age, color, price)

class Bunch:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_amount(self):
        result = 0
        for _ in self.flowers:
            result = result + 1
        return result

    def total_price(self):
        result = 0
        for flower in self.flowers:
            result = result + flower.price
        return result

    # Увядание по среднему времени жизни всех цветов в букете, в днях
    def average_age(self):
        result = 0
        for flower in self.flowers:
            result = result + flower.age
            average = result // self.total_amount()
        return average

    # Сортировка по цвету
    def get_color(self, color):
        result = []
        for flower in self.flowers:
            if flower.color == color:
                result.append(flower.name)
        return result

    @staticmethod
    def is_expensive_stat(price):
        return 'expensive' if price > 10 else 'cheap'

Plant = Plant()
Bunch = Bunch()

Daisy = Flower("Daisy", 6, "pupple", 15)
Camomile = Flower2("Camomile", 6, "white", 5)
Rose = Flower("Rose", 5, "red", 5)

Bunch.add_flower(Daisy)
Bunch.add_flower(Camomile)
Bunch.add_flower(Rose)
# print(Bunch)

print(Bunch.total_amount())
print(Bunch.total_price())
print(Bunch.average_age())
print(Bunch.get_color("red"))
print(Bunch.is_expensive_stat(15))
print(Rose.is_expensive())
print(Flower2)
