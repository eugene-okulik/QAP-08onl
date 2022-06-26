# Создать классы цветов: общий класс для всех цветов и классы для нескольких видов.
# Создать экземпляры цветов. Собрать букет (букет - еще один класс)
# (можно использовать аксессуары) с определением его стоимости.
# Для букета создать метод, который определяет время его увядания по среднему времени жизни всех цветов в букете.
# Позволить сортировку цветов в букете на основе различных параметров (свежесть/цвет/длина стебля/стоимость)
# (это тоже методы)
# Реализовать поиск цветов в букете по каким-нибудь параметрам (например, по среднему времени жизни) (и это тоже метод).
# Узнать, есть ли цветок определенного типа в букете.

class Flower:
    def __init__(self, flower_name, color, price, lifetime_hours, stem_length):
        self.flower_name = flower_name
        self.color = color
        self.price = price
        self.lifetime_hours = lifetime_hours
        self.stem_length = stem_length


class Rose(Flower):
    def __init__(self):
        self.flower_name = "Rose"
        self.color = "Red"
        self.price = 500
        self.lifetime_hours = 40
        self.stem_length = 70


class Verbena(Flower):
    def __init__(self):
        self.flower_name = "Verbena"
        self.color = "Blue"
        self.price = 800
        self.lifetime_hours = 20
        self.stem_length = 30


class Peony(Flower):
    def __init__(self):
        self.flower_name = "Peony"
        self.color = "Yellow"
        self.price = 100
        self.lifetime_hours = 10
        self.stem_length = 50


class Bouquet:
    def __init__(self, *flowers):
        self.content = flowers

    def lifetime_of_bouquet(self):
        result = 0
        for i in self.content:
            result += i.lifetime_hours
        result = round(result / len(self.content), 1)
        return result

    def sort_by_lifetime_hours(self):
        i = 0
        while i < len(self.content):
            print(self.content[i].lifetime_hours)
            if self.content[i].lifetime_hours <


rose1 = Rose()
Verbena1 = Verbena()
Peony1 = Peony()
Bouquet1 = Bouquet(rose1, Verbena1, Peony1)
# print(Bouquet1.lifetime_of_bouquet())
print(Bouquet1.sort_by_lifetime_hours())
