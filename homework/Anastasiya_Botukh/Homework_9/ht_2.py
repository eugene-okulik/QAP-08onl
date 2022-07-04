class Investment:
    def __init__(self, amount, term):
        self.amount = amount
        self.term = term


class Bank:
    def __init__(self):
        pass

    @staticmethod
    def deposit(invest):
        monthly_percent = 10 / 12
        months = invest.term * 12
        total_amount = invest.amount
        while months > 0:
            total_amount = total_amount + (total_amount / 100 * monthly_percent)
            months = months - 1
            # print(total_amount)
        return total_amount


investment = Investment(2000, 5)
bank = Bank()
print(bank.deposit(investment))
