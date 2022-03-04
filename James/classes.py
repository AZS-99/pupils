"""
(The Stock class) Design a class named Stock to represent a company’s stock that contains:
■ A private string data field named symbol for the stock’s symbol.
■ A private string data field named name for the stock’s name.
■ A private float data field named previousClosingPrice that stores the stock
price for the previous day.
■ A private float data field named currentPrice that stores the stock price for
the current time.
■ A constructor that creates a stock with the specified symbol, name, previous
price, and current price.
■ A method named getChangePercent() that returns the percentage changed
from previousClosingPrice to currentPrice.
"""
class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice

    def getChangePercent(self):
        change = self.currentPrice - self.previousClosingPrice
        changepercent = (change/self.currentPrice) * 100
        return round(changepercent, 2)


"""
(The Account class) Design a class named Account that contains:
■ A private int data field named id for the account.
■ A private float data field named balance for the account.
■ A private float data field named annualInterestRate that stores the current
interest rate.
■ A constructor that creates an account with the specified id (default 0), initial
balance (default 100), and annual interest rate (default 0).
■ A method named getMonthlyInterestRate() that returns the monthly
interest rate.
■ A method named getMonthlyInterest() that returns the monthly interest.
■ A method named withdraw that withdraws a specified amount from the
account.
■ A method named deposit that deposits a specified amount to the account.
(Hint: The method getMonthlyInterest() is to return the monthly interest amount, not the interest rate. 
Use this formula to calculate the monthly interest: balance * monthlyInterestRate
            monthlyInterestRate is annualInterestRate / 12. 
Note that annualInterestRate is a percent (like 4.5%). You need to divide it by 100.)
Write a test program that creates an Account object with an account id of 1122, a balance of $20,000, and an annual 
interest rate of 4.5%. Use the withdraw method to withdraw $2,500, use the deposit method to deposit $3,000, and print 
the id, balance, monthly interest rate, and monthly interest.
"""
class Account:
    def __init__(self, id=0, balance=100, annualInterestRate=0):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        return self.annualInterestRate / 12

    def getMonthlyInterest(self):
        return self.balance * self.getMonthlyInterestRate()

    def withdraw(self, amt):
        self.balance -= amt

    def deposit(self, amt):
        self.balance += amt


"""
(The Fan class) Design a class named Fan to represent a fan. The class contains:
■ Three constants named SLOW, MEDIUM, and FAST with the values 1, 2, and 3 to denote the fan speed.
■ A private int data field named speed that specifies the speed of the fan.
■ A private bool data field named on that specifies whether the fan is on (the
default is False).
■ A private float data field named radius that specifies the radius of the fan.
■ A private string data field named color that specifies the color of the fan.
■ A constructor that creates a fan with the specified speed (default SLOW), radius
(default 5), color (default blue), and on (default False).
Write a test program that creates two Fan objects. For the first object, assign the maximum speed, radius 10, color 
yellow, and turn it on. Assign medium speed, radius 5, color blue, and turn it off for the second object. Display each 
object’s speed, radius, color, and on properties.
"""
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3
    def __init__(self, speed, radius=5, on=False, color="blue"):
        self.radius = radius
        self.on = on
        self.speed = Fan.SLOW
        self.color = color
