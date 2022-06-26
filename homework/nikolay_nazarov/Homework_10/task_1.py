class Flower:
    def empty_public_method_1(self):
        pass

    def empty_public_method_2(self):
        pass


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
        self.content = list(flowers)

    def lifetime_of_bouquet(self):
        result = 0
        for i in self.content:
            result += i.lifetime_hours
        result = round(result / len(self.content), 1)
        return result

    def sort_by_lifetime_hours(self):
        i = 0
        while i < len(self.content):
            try:
                if self.content[i].lifetime_hours < self.content[i + 1].lifetime_hours:
                    i += 1
                elif self.content[i].lifetime_hours == self.content[i + 1].lifetime_hours:
                    i += 1
                else:
                    temp = self.content[i]
                    self.content[i] = self.content[i + 1]
                    self.content[i + 1] = temp
                    i = 0
            except IndexError:
                break
        return self.content

    def find_flower_by_color(self, color):
        for i in self.content:
            if i.color == color:
                return i.flower_name
        return "Нет цветка в таким цветом"

    def is_where_flower_with_price(self, price):
        for i in self.content:
            if i.price == price:
                return i.flower_name
        return "Нет цветка с такой стоимостью"


Rose1 = Rose()
Verbena1 = Verbena()
Peony1 = Peony()
Bouquet1 = Bouquet(Rose1, Verbena1, Peony1)
print(Bouquet1.lifetime_of_bouquet())
print(Bouquet1.sort_by_lifetime_hours())
print(Bouquet1.content)
print(Bouquet1.find_flower_by_color("Red"))
print(Bouquet1.is_where_flower_with_price(100))
