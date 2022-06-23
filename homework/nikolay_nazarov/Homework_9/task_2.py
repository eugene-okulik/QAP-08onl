# Создайте класс инвестиция, который содержит необходимые поля и методы,
# например сумма инвестиции и ее срок, расчет доходности.
# Пользователь делает инвестицию в размере N рублей сроком на R лет под 10% годовых
# (инвестиция с возможностью ежемесячной капитализации -
# это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, метод deposit принимает аргументы N и R, и возвращает сумму,
# которая будет на счету пользователя.

class Investments:
    def __init__(self, inv_sum, inv_time):
        self.inv_sum = inv_sum
        self.inv_time = inv_time


class Bank:
    @staticmethod
    def deposit(class_object):
        profit = class_object.inv_sum * (1 + 0.1 / 12) ** (class_object.inv_time * 12)
        return profit


inv1 = Investments(700000, 5)
print(Bank.deposit(inv1))
