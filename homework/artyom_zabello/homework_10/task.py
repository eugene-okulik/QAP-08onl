class Flower:
    def __init__(self, fresh, color, length, cost):
        self.fresh = fresh
        self.color = color
        self.length = length
        self.cost = cost

    def change_color(self, col):
        self.color = col

    def change_cost(self, cost):
        self.cost = cost


class Rose(Flower):
    def __init__(self, fresh=10, color='Red', length=15, cost=75):
        super().__init__(fresh, color, length, cost)
        self.fresh = fresh
        self.color = color
        self.length = length
        self.cost = cost
        self.name = 'Rose'


class Chamomile(Flower):
    def __init__(self, fresh=8, color='White', length=10, cost=40):
        super().__init__(fresh, color, length, cost)
        self.fresh = fresh
        self.color = color
        self.length = length
        self.cost = cost
        self.name = 'Chamomile'


class Peony(Flower):
    def __init__(self, fresh=6, color='Pink', length=18, cost=60):
        super().__init__(fresh, color, length, cost)
        self.fresh = fresh
        self.color = color
        self.length = length
        self.cost = cost
        self.name = 'Peony'


class Lily(Flower):
    def __init__(self, fresh=12, color='Green', length=25, cost=70):
        super().__init__(fresh, color, length, cost)
        self.fresh = fresh
        self.color = color
        self.length = length
        self.cost = cost
        self.name = 'Lily'


class Astra(Flower):
    def __init__(self, fresh=15, color='Yellow', length=17, cost=45):
        super().__init__(fresh, color, length, cost)
        self.fresh = fresh
        self.color = color
        self.length = length
        self.cost = cost
        self.name = 'Astra'


class Bouquet:
    def __init__(self):
        self.bouquet = []
        self.cost = []
        self.life = []
        self.color = []
        self.length = []

    @classmethod
    def check(cls, var):
        if len(var) > 0:
            return True
        return False

    def add(self, flo):
        """Method for adding flowers into bouquet"""
        self.bouquet.append(flo.name)
        self.cost.append(flo.cost)
        self.life.append(flo.fresh)
        self.color.append(flo.color)
        self.length.append(flo.length)

    def get_bouquet(self):
        """Method for getting info about your bouquet """
        if self.check(self.bouquet):
            return f"Your bouquet is consist of {', '.join(self.bouquet)} price is {sum(self.cost)}"
        return "Your bouquet has been not formed yet"

    def avg_life(self):
        """Average time to fade of your bouquet """
        if self.check(self.bouquet):
            return f'Average time to fade is {(sum(self.life)) / len(self.bouquet)} days'
        return "Your bouquet has been not formed yet"

    def sort_by_fresh(self):
        if self.check(self.bouquet):
            __res = dict(zip(self.bouquet, self.life))
            return list(reversed(sorted(__res.items(), key=lambda x: x[1])))
        return "Your bouquet has been not formed yet"

    def sort_by_color(self):
        if self.check(self.bouquet):
            __res = dict(zip(self.bouquet, self.color))
            return sorted(__res.items(), key=lambda x: x[1])
        return "Your bouquet has been not formed yet"

    def sort_by_length(self):
        if self.check(self.bouquet):
            __res = dict(zip(self.bouquet, self.length))
            return list(reversed(sorted(__res.items(), key=lambda x: x[1])))
        return "Your bouquet has been not formed yet"

    def sort_by_cost(self):
        if self.check(self.bouquet):
            __res = dict(zip(self.bouquet, self.cost))
            return list(reversed(sorted(__res.items(), key=lambda x: x[1])))
        return "Your bouquet has been not formed yet"

    def find_by_cost(self, cos):
        if self.check(self.bouquet):
            __res = dict(zip(self.bouquet, self.cost))
            __res1 = {flow: cost for flow, cost in __res.items() if cost >= cos}
            return __res1
        return "Your bouquet has been not formed yet"

    def find_by_type(self, flo):
        if flo in self.bouquet:
            return "Is present"
        return "Is absent"


flower1 = Rose()
flower1.change_cost(10)
flower2 = Lily()
flower3 = Astra()
flower4 = Peony()
flower5 = Chamomile()
bouquet1 = Bouquet()
bouquet1.add(flower1)
bouquet1.add(flower2)
bouquet1.add(flower3)
flower1.change_cost(10)
print(bouquet1.get_bouquet())
