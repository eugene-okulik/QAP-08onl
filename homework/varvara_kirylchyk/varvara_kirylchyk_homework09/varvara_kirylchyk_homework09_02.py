# # Банковский вклад
#
# Создайте класс инвестиция, который содержит необходимые поля и методы,
# например сумма инвестиции и ее срок, расчет доходности.

# Пользователь делает инвестицию в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации - это означает,
# что проценты прибавляются к сумме инвестиции ежемесячно).

# Написать класс Bank, который в качестве свойства принимает инвестицию,
# внутри класса Bank метод deposit который возвращает сумму,
# которая будет на счету пользователя (расчитывается исходя из инвестиции).

class Investments:
    def __init__(self, amount, rate, time):
        self._amount = amount
        self.rate = rate
        self._time = time

    @property
    def time(self):
        return self._time

    @property
    def amount(self):
        return self._amount

class Bank:
    def __init__(self):
        pass

    @staticmethod
    def deposit(num):
        simple_interest = (num.amount * num.time * num.rate) / 100
        profit = num.amount + simple_interest
        return profit

    @staticmethod
    def public_method():
        pass

Invest = Investments(10000, 10, 5)
print(Bank.deposit(Invest))
