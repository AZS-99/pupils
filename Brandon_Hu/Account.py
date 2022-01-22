class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions_count = 0

    def withdraw(self, amount):
        raise NotImplementedError

    def deposit(self, amount):
        raise NotImplementedError


