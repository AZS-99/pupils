# Parent Class
class Account:
    def __init__(self, balance):
        self.balance = balance
        self.transactions = 0

    def deposit(self, amount):
        raise NotImplementedError

    def withdraw(self, amount):
        raise NotImplementedError





