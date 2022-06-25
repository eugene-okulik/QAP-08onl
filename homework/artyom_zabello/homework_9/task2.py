class Investment:
    def __init__(self, amount, term):
        self._amount = amount
        self.term = float(term)

    @property
    def amount(self):
        return self._amount

    def invest(self):
        profit = self._amount / 100 * (10/12)
        return profit


class Bank:

    def public(self):
        pass

    @staticmethod
    def deposit(dep):
        """This method counts user's deposit according to investment.
            Accepts investment as input """
        result = dep.amount + (dep.invest()*(dep.term*12))
        return print(f"Your deposit will be {result} rubles")


inv1 = Investment(300, 1)
Bank.deposit(inv1)
