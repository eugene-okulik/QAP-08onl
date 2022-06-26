# Создайте класс инвестиция, который содержит необходимые поля и методы,
# например сумма инвестиции и ее срок, расчет доходности.
# Пользователь делает инвестицию в размере N рублей сроком на R лет
# под 10% годовых (инвестиция с возможностью ежемесячной капитализации -
# это означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, который в качестве свойства принимает инвестицию,
# внутри класса Bank метод deposit который возвращает сумму,
# которая будет на счету пользователя (расчитывается исходя из инвестиции).

class Investment:
    def __init__(self, amount, term, calculation):
        self.amount = amount
        self.term = term
        self.calculation = calculation

    def set_amount(self, amount):
        self.amount = amount

    def set_term(self, term):
        self.term = term

    def set_calculation(self, calculation):
        self.calculation = calculation


class Bank:
    investment = None
    def set_investment(self, investment):
        self.investment = investment

    def deposit(self):
        month = self.investment.term * 12
        every_month = self.investment.calculation / 12
        total = self.investment.amount
        for _ in range(month):
            total = total + (total / 100 * every_month)

        return total


x = Investment(35700, 15, 12)
bank = Bank()
bank.set_investment(x)
result = bank.deposit()

print(int(result))
