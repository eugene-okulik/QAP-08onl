class Investments:
    def __init__(self, inv_sum, inv_time, deposit_percentage=10):
        self.inv_sum = inv_sum
        self.inv_time = inv_time
        self.deposit_percentage = deposit_percentage / 100

    def calculation_of_investment(self):
        profit = self.inv_sum * (1 + self.deposit_percentage / 12) ** (self.inv_time * 12)
        return profit

    def some_public_method_1(self):
        pass


class Bank:
    @staticmethod
    def deposit(inv_object):
        return inv_object.calculation_of_investment()

    def some_public_method_2(self):
        pass


inv1 = Investments(700000, 5)
print(Bank.deposit(inv1))
