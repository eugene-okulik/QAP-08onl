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
    def rate():
        pass


Invest = Investments(5000, 25, 5)
print(Bank.deposit(Invest))
