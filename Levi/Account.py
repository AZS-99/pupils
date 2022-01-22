class Account:
    def __init__(self, balance):
        self.balance = balance
        self.transactions = 0

    def __str__(self):
        return "{0} account with balance: {1}".format(type(self).__name__, self.balance)

    def withdraw(self, amount):
        raise NotImplementedError

    def deposit(self, amount):
        raise NotImplementedError


class Chequing(Account):
    FEE = 5
    MAX_TRANSACTIONS = 30
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if amount < self.balance:
            self.balance -= amount
            self.transactions += 1
            if self.transactions >= Chequing.MAX_TRANSACTIONS:
                self.balance -= Chequing.FEE
                self.transactions = 0
        else:
            raise Exception("Insufficent Funds")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions += 1
            if self.transactions >= Chequing.MAX_TRANSACTIONS:
                self.balance -= Chequing.FEE
                self.transactions = 0
        else:
            raise Exception("Amount cannot be Negative")


class Savings(Account):
    MAX_TRANSACTIONS = 5
    FEE = 100
    def __init__(self, balance):
        super().__init__(balance)


    def withdraw(self, amount):
        if 0 < amount < self.balance and self.transactions <= 5:
            self.balance -= amount
            self.transactions += 1
            self.balance -= Savings.FEE
        else:
            raise Exception("Exceeded 5 Transactions or Amount is Greater Than Balance")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise Exception("Amount cannot be Negative")