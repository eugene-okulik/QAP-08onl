# Цветочница
# Создать классы цветов: общий класс для всех цветов
# и классы для нескольких видов.
# Создать экземпляры цветов.
# Собрать букет (букет - еще один класс) (можно использовать аксессуары)
# с определением его стоимости.
# Для букета создать метод,
# который определяет время его увядания по среднему времени жизни
# всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров
# (свежесть/цвет/длина стебля/стоимость)(это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам
# (например, по среднему времени жизни) (и это тоже метод).
# Узнать, есть ли цветок определенного типа в букете.
# max age of rose is 5; fresh rose when current age <=20% of max age
# max age of peony is 10; fresh peony when current age <= 50% max age

import abc
from dataclasses import dataclass


@dataclass
class Plant(abc.ABC):
    name: str
    max_age: int
    current_age: int
    color: str
    length: int
    price: float
    petal_shape: str
    # thorns: bool

    # @abc.abstractmethod
    # def is_expensive(self):
    #     pass

    @abc.abstractmethod
    def is_fresh(self):
        pass


class Rose(Plant):
    def is_fresh(self):
        return self.current_age <= 0.2 * self.max_age

    def dummy(self):
        pass


class Peony(Plant):
    def is_fresh(self):
        return self.current_age <= 0.5 * self.max_age

    def dummy(self):
        pass


rose1 = Rose(name="Rose", max_age=5, current_age=1, color="red",
             length=10, price=100, petal_shape="round")
peony1 = Peony(name="Peony", max_age=10, current_age=8, color="white",
               length=20, price=80, petal_shape="")
print(rose1.is_fresh())
print(peony1.is_fresh())

rose2 = Rose(name="Rose", max_age=7, current_age=2, color="red",
             length=10, price=100, petal_shape="round")
peony2 = Peony(name="Peony", max_age=5, current_age=9, color="red",
               length=10, price=100, petal_shape="round")


class Bunch:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_amount(self):
        return len(self.flowers)

    def total_price(self):
        result = 0
        for flower in self.flowers:
            result = result + flower.price
        return result

    # Увядание по среднему времени жизни всех цветов в букете, в днях
    def average_age(self):
        return sum([f.current_age for f in self.flowers]) / len(self.flowers)

    # выборка цветов по цвету
    def get_color(self, color):
        return [f for f in self.flowers if f.color == color]

    @staticmethod
    def is_expensive_stat(price):
        return price > 10


Bunch = Bunch()

Bunch.add_flower(rose1)
Bunch.add_flower(rose2)
Bunch.add_flower(peony1)
Bunch.add_flower(peony2)

print(Bunch.total_amount())
print(Bunch.total_price())
print(Bunch.average_age())
print(Bunch.get_color("red"))
print(Bunch.is_expensive_stat(15))
print(rose1)
