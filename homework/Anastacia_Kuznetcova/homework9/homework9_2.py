"""Решение задания снизу"""


class Investment:
    """Создан класс инвестиции"""

    def __init__(self, amount, time, rate):
        self.amount = amount
        self.time = time
        self.rate = rate

    def set_amount(self, amount):
        """Добавлен setter суммы инвестиции"""
        self.amount = amount

    def set_time(self, time):
        """Добавлен setter срока"""
        self.time = time

    def set_rate(self, rate):
        """Добавлен setter процента"""
        self.rate = rate


class Bank:
    """Добавлен класс банка"""
    investment = None

    def set_investment(self, investment):
        """Добавлен setter инвестиции"""
        self.investment = investment

    def deposit(self):
        """Добавлен метод депозит"""
        month = self.investment.time * 12
        monthly = self.investment.rate / 12
        result = self.investment.amount
        for _ in range(month):
            result = result + (result / 100 * monthly)

        return result


i = Investment(10000, 10, 10)
bank = Bank()
bank.set_investment(i)
res = bank.deposit()

print(int(res))
