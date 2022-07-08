class Investment:

    def __init__(self, money, term, percent, user_name=None):
        self.money = money
        self.term = term
        self.percent = percent
        self._user_name = user_name

    def profit(self):
        profit = self.money + (((self.money / 100) * self.percent)
                               / 12) * self.term
        return f'The amount at the end of the term will be: {profit}$'

    @property
    def user_name(self):
        return self._user_name


class Bank:
    def __init__(self, investment=None):
        self.investment = investment

    def deposit(self):
        return self.investment.profit()

    def user_name(self):
        return self.investment.user_name


bank = Bank()
invest1 = Investment(float(input('Enter the amount: ')),
                     int(input('Enter the term (months): ')),
                     int(input('At what percentage: ')),
                     input('Enter your name: '))
bank .investment = invest1
print(bank.user_name(), bank.deposit())
