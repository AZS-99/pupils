#Children Class
from Account import Account

class Chequing(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            self.transactions += 1

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount









