class Chequing:
    FEE = 10
    def __init__(self, first_name, last_name, age, sin_number):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sin_number = sin_number
        self.balance = 0
        self.transactions = 0

    def __str__(self):
        return str(self.balance)

    def deposit(self, amount):
        if self.transactions < 30:
            if amount >= 0:
                self.balance += amount
                self.transactions += 1
            else:
                print("Error")
        else:
            if amount >= 0:
                if self.balance + amount >= Chequing.FEE:
                    self.balance += amount
                    self.balance -= Chequing.FEE
                    self.transactions += 1
                else:
                    print("YOUR BALANCE IS NOT ENOUGH!!!!!!")
            else:
                print("Error")

    def withdraw(self, amount):
        if self.transactions < 30:
            if amount >= 0:
                if self.balance < amount:
                    print("No enough money to withdraw")
                else:
                    self.balance -= amount
                    self.transactions += 1
            else:
                print("Error")
        else:
            if amount >= 0:
                if self.balance - amount - Chequing.FEE >= 0:
                    self.balance -= amount
                    self.balance -= Chequing.FEE
                else:
                    print("YOUR BALANCE IS NOT THAT MUCH!!!!")
            else:
                print("Error")
