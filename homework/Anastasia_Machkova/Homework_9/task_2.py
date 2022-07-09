class Invest:
    def __init__(self, amount, term, rate):
        self._amount = amount
        self._term = term
        self._rate = rate

    @property
    def amount(self):
        return self._amount

    @property
    def term(self):
        return self._term

    @property
    def rate(self):
        return self._rate


class Bank:
    def __init__(self):
        pass

    @staticmethod
    def deposit(num):
        result = (num.amount * num.term * num.rate) / 100
        profit = num.amount + result
        return profit

    @staticmethod
    def public_method():
        pass

MyProfit = Invest(1500, 5, 3)
print(Bank.deposit(MyProfit))
