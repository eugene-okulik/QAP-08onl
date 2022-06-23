class Investments:
    def __init__(self, inv_sum, inv_time):
        self.inv_sum = inv_sum
        self.inv_time = inv_time

    @staticmethod
    def some_public_method_1():
        pass

    @staticmethod
    def some_public_method_2():
        pass


class Bank:
    @staticmethod
    def deposit(class_object):
        profit = class_object.inv_sum * (1 + 0.1 / 12) ** (class_object.inv_time * 12)
        return profit

    @staticmethod
    def some_public_method_3():
        pass


inv1 = Investments(700000, 5)
print(Bank.deposit(inv1))
