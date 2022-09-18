class Flowers:
    def __init__(self, name=None, colour=None, lifetime=None, price=None):
        self.name = name
        self.colour = colour
        self.lifetime = lifetime
        self.price = price

    def fl_fresh(self):
        return ' не свежий' if self.lifetime < 2 else ' свежий'

    def fl_price(self):
        return ' не дорогой' if self.price < 350 else ' дорогой'


class UnusualFlowers(Flowers):
    def __init__(self, name, colour=None, lifetime=None, price=None):
        super().__init__(name, colour, lifetime, price)


class RegularFlowers(Flowers):
    def __init__(self, name, colour=None, lifetime=None, price=None):
        super().__init__(name, colour, lifetime, price)


class Bouquet:
    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def bq_price(self):
        full_price = 0
        for flower in self.flowers:
            full_price += flower.price
        return full_price

    def life_expectancy(self):
        life_exp = 0
        for flower in self.flowers:
            life_exp = (life_exp + flower.lifetime) / len(self.flowers)
        return life_exp

    def get_colour(self, colour):
        flower_colour = []
        for flower in self.flowers:
            if flower.colour == colour:
                flower_colour.append(flower.name)
        return flower_colour

    def bq_fresh(self):
        life_bq_exp = 0
        for flower in self.flowers:
            life_bq_exp = (life_bq_exp + flower.lifetime) / len(self.flowers)
        return 'Букет цветов не свежий' if life_bq_exp < 1 else 'Букет цветов свежий'


flower1 = UnusualFlowers('Крокус', 'синий', 4, 70)
flower2 = UnusualFlowers('Георгины', 'белый', 5, 150)
flower3 = UnusualFlowers('Нарцисс', 'желтый', 10, 200)
flower4 = UnusualFlowers('Герань', 'красный', 7, 500)
flower5 = UnusualFlowers('Ирис', 'голубой', 6, 500)
flower6 = RegularFlowers('Роза', 'красный', 4, 400)
flower7 = RegularFlowers('Лилия', 'оранжевый', 5, 255)
flower8 = RegularFlowers('Петуния', 'фиолетовый', 8, 250)
flower9 = RegularFlowers('Альстромерия', 'розовый', 8, 280)
flower10 = RegularFlowers('Пионы', 'фиолетовый', 5, 300)
bouquet1 = Bouquet()
bouquet1.add_flower(flower1)
bouquet1.add_flower(flower7)
bouquet1.add_flower(flower5)
bouquet1.add_flower(flower4)
bouquet1.add_flower(flower3)
bouquet1.add_flower(flower2)
print(f'Полная стоимость букета {bouquet1.bq_price()} тугриков')
print()
print(f'Средняя продолжительность жизни букета {round(bouquet1.life_expectancy(), 1)} дней')
print(bouquet1.get_colour('Оранжевый'))
print(f'Цветок {flower7.name} {flower7.fl_fresh()} {flower7.fl_price()}')
print(f'Цветок {flower5.name} {flower5.fl_fresh()} {flower5.fl_price()}')
print(f'Цветок {flower4.name} {flower4.fl_fresh()} {flower4.fl_price()}')
print(f'Цветок {flower1.name} {flower1.fl_fresh()} {flower1.fl_price()}')
print(f'Цветок {flower3.name} {flower3.fl_fresh()} {flower3.fl_price()}')
print(f'Цветок {flower2.name} {flower2.fl_fresh()} {flower2.fl_price()}')
print(bouquet1.bq_fresh())
