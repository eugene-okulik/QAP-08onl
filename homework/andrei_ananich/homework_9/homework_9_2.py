# Создайте класс инвестиция, который содержит необходимые поля и методы,
# например сумма инвестиции и ее срок, расчет доходности.
# Пользователь делает инвестицию в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации - это означает,
# что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, который в качестве свойства принимает инвестицию,
# внутри класса Bank метод deposit который возвращает сумму,
# которая будет на счету пользователя (расчитывается исходя из инвестиции)


class Investments:
    def __init__(self, amount, time, rate):
        self._amount = amount
        self._time = time
        self._rate = rate

    @property
    def amount(self):
        return self._amount

    @property
    def time(self):
        return self._time

    @property
    def rate(self):
        return self._rate


class Bank:
    def __init__(self):
        pass

    @staticmethod
    def deposit(number):
        result = (number.amount * number.time * number.rate) / 100
        profit = number.amount + result
        return profit

    @staticmethod
    def rate():
        pass


MyProfit = Investments(100, 1, 12)
print(Bank.deposit(MyProfit))
