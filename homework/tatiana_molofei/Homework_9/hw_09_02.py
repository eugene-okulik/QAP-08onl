# Создайте класс инвестиция, который содержит необходимые поля и методы,
# например сумма инвестиции и ее срок, расчет доходности.
# Пользователь делает инвестицию в размере N рублей сроком на R лет под
# 10% годовых (инвестиция с возможностью ежемесячной капитализации - это
# означает, что проценты прибавляются к сумме инвестиции ежемесячно).
# Написать класс Bank, который в качестве свойства принимает инвестицию,
# внутри класса Bank метод deposit который возвращает сумму, которая будет
# на счету пользователя (расчитывается исходя из инвестиции).

class Invest:
    def __init__(self, percent, summ, term):
        self.percent = percent
        self._summ = summ
        self._term = term

    @property
    def summ(self):
        return self._summ

    @property
    def term(self):
        return self._term


class Bank:
    def __init__(self):
        pass

    @staticmethod
    def deposit(user_dep):
        i = 1
        term_month = user_dep.term * 12
        amount_percent = 0
        deposit_amount = user_dep.summ + amount_percent
        while i in range(0, term_month + 1):
            amount_percent = deposit_amount * user_dep.percent / 100 / 12
            deposit_amount += amount_percent
            # print(i, deposit_amount)
            i += 1

        return deposit_amount


user_invest = Invest(10, 1000, 2)

print(f'Your deposit will be {Bank.deposit(user_invest)}')
