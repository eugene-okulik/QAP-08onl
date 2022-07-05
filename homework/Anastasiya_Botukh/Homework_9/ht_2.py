class Investment:
    def __init__(self, amount, term, profitability_calculation):
        self.amount = amount
        self.term = term
        self.profitability_calculation = profitability_calculation


class Bank:
    def __init__(self):
        pass

    @staticmethod
    def deposit(invest):
        monthly_profitability_calculation = 10 / 12
        months = invest.term * 12
        total_amount = invest.amount
        while months > 0:
            total_amount = total_amount + (total_amount / 100 * monthly_profitability_calculation)
            months = months - 1
            # print(total_amount)
        return total_amount

    def public_method(self):
        pass


investment = Investment(2000, 5, 4)
bank = Bank()
print(bank.deposit(investment))
