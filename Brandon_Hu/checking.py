from Account import Account

class Cheqing(Account):
    FEE = 10
    MAX_TRANACTION = 30
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def withdraw(self, amount):
        if amount > 0:
            self.balance -= amount
            self.transactions_count += 1
            if self.transactions_count == Cheqing.MAX_TRANACTION:
                self.balance -= Cheqing.FEE


