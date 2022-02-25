
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
■ A get method for returning the stock name.
■ A get method for returning the stock symbol.
■ Get and set methods for getting/setting the stock’s previous price.
■ Get and set methods for getting/setting the stock’s current price.
■ A method named getChangePercent() that returns the percentage changed
from previousClosingPrice to currentPrice.
"""
import math


class Stock:
    def __init__(self, symbol, name, previousClosingPrice, currentPrice):
        self.symbol = symbol
        self.name = name
        self.previousClosingPrice = previousClosingPrice
        self.currentPrice = currentPrice

    def getChangePercent(self):
        percentage = round((((self.currentPrice - self.previousClosingPrice) / self.previousClosingPrice) * 100), 1)


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
    def __init__(self, id, balance, annualInterestRate):
        self.id = id
        self.balance = balance
        self.annualInterestRate = annualInterestRate

    def getMonthlyInterestRate(self):
        monthly_interest_rate = self.annualInterestRate / 12
        return monthly_interest_rate

    def getMonthlyInterest(self):
        monthly_interest = self.balance * self.getMonthlyInterestRate()
        return monthly_interest

    def withdraw(self, amount):
        self.balance = self.balance - amount

    def deposit(self, amount):
        self.balance = self.balance + amount


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
    def __init__(self, speed, power, radius, color):
        self.speed = speed
        self.power = power
        self.radius = radius
        self.color = color

"""
(Geometry: n-sided regular polygon) An n-sided regular polygon’s sides all have the same length and all of its angles 
have the same degree (i.e., the polygon is both equilateral and equiangular). Design a class named RegularPolygon 
that contains:
■ A private int data field named n that defines the number of sides in the polygon.
■ A private float data field named side that stores the length of the side.
■ A private float data field named x that defines the x-coordinate of the center of
the polygon with default value 0.
■ A private float data field named y that defines the y-coordinate of the center of the polygon with default value 0.
■ A constructor that creates a regular polygon with the specified n (default 3), side (default 1), x (default 0), and 
y (default 0).
■ The method getPerimeter() that returns the perimeter of the polygon.
■ The method getArea() that returns the area of the polygon. The formula for
computing the area of a regular polygon is Area = (n x s^2) / 4 x tan(π/n) 

Write a test program that creates three RegularPolygon objects, created using RegularPolygon(), 
using RegularPolygon(6, 4) and RegularPolygon(10, 4, 5.6, 7.8). For each object, display its perimeter and area.
"""
class RegularPolygon:

    def __init__(self, n, side, x=0, y=0):
        self.n = n
        self.side = side
        self.x = x
        self.y = y

    def getPerimeter(self):
        perimeter = self.n * self.side
        return round(perimeter, 2)

    def getArea(self):
        area = (self.n * self.side ** 2) / 4 * math.tan(math.pi / self.n)
        return round(area, 2)


"""
(Algebra: quadratic equations) Design a class named QuadraticEquation for a quadratic equation ax2 + bx + x = 0. The 
class contains:
■ The private data fields a, b, and c that represent three coefficients.
■ A constructor for the arguments for a, b, and c.
■ A method named getDiscriminant() that returns the discriminant, which is b^2 - 4ac.
■ The methods named getRoot1() and getRoot2() for returning the two roots
of the equation using these formulas:

r1 =(-b+ sqrt(b^2-4ac)) / 2a and r2 = (-b-sqrt(b^2-4ac)) / 2a

These methods are useful only if the discriminant is non-negative. Let these methods return 0 if the discriminant is 
negative.
Implement the class. Write a test program that prompts the user to enter values for a, b, and c and displays the result 
based on the discriminant. If the discriminant is positive, display the two roots. If the discriminant is 0, display the 
one root. Otherwise, display “The equation has no roots.” 

Sample Run 1:
Enter a, b, c: 1.0, 3, 1
The roots are -0.381966 and -2.61803

Sample Run 2:
Enter a, b, c: 1, 2.0, 1
The root is -1

Sample Run 3:
Enter a, b, c: 1, 2, 3
The equation has no real roots
"""
class QuadraticEquation:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def getDiscriminant(self):
        return self.b ** 2 - 4 * self.a * self.c

    def getRoot1(self):
        return round(((-self.b + math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / 2 * self.a), 6)

    def getRoot2(self):
        return round(((-self.b - math.sqrt(self.b ** 2 - 4 * self.a * self.c)) / 2 * self.a), 6)


"""
(Algebra: 2 * 2 linear equations) Design a class named LinearEquation for a 2 * 2 system of linear equations:

ax + by = e
cx + dy = f

x = (ed - bf) / (ad - bc)
y = (af - ec) / (ad - bc)


The class contains:
■ The private data fields a, b, c, d, e, and f with get methods.
■ A constructor with the arguments for a, b, c, d, e, and f.
■ A method named isSolvable() that returns true if ad - bc is not 0.
■ The methods getX() and getY() that return the solution for the equation.
Implement the class. Write a test program that prompts the user to enter a, b, c, d, e, and f and displays the result. 
If ad - bc is 0, report that “The equation has no solution.”

Sample Run 1:
Enter a, b, c, d, e, f: 9.0, 4.0, 3.0, -5.0, -6.0, -21.0
x is -2.0 and y is 3.0

Sample Run 2:
Enter a, b, c, d, e, f: 1.0, 2.0, 2.0, 4.0, 4.0, 5.0
The equation has no solution
"""
class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f

    def isSolvable(self):
        if (self.a * self.d - self.b * self.c) == 0:
            return False
        else:
            return True

    "x = (ed - bf) / (ad - bc) y = (af - ec) / (ad - bc)"
    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.b - self.b * self.c)

