
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
import math, time


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

    def getX(self):
        return (self.e * self.d - self.b * self.f) / (self.a * self.d - self.b * self.c)


    def getY(self):
        return (self.a * self.f - self.e * self.c) / (self.a * self.d - self.b * self.c)


"""
(Stopwatch) Design a class named StopWatch. The class contains:
■ The private data fields startTime and endTime.
■ A constructor that initializes startTime with the current time.
■ A method named start() that resets the startTime to the current time.
■ A method named stop() that sets the endTime to the current time.
■ A method named getElapsedTime() that returns the elapsed time for the
stop watch in milliseconds.
Implement the class. Write a test program that measures the execution time of adding numbers from 1 to 1,000,000.
"""
class StopWatch:
    def __init__(self):
        self.startTime = time.time()
        self.stopTime = float('inf')

    def start(self):
        self.startTime = time.time()

    def stop(self):
        self.stopTime = time.time()

    def getElapsedTime(self):
        return self.stopTime - self.startTime


"""
(Geometry: intersection) Suppose two line segments intersect. The two endpoints for the first line segment are (x1, y1)
and (x2, y2) and for the second line segment are (x3, y3) and (x4, y4). Write a program that prompts the user to enter 
these four endpoints and displays the intersecting point. (Hint: Use the LinearEquation class)
 
Enter the endpoints of the first line segment: 2.0, 2.0, 0, 0
Enter the endpoints of the second line segment: 0, 2.0, 2.0, 0
The intersecting point is: (1.0, 1.0)
"""
class LinearEquation:
    def geometry_intersection(self):
        pass



"""
(The Point class) Design a class named Point to represent a point with x- and y-coordinates. The class contains:
■ Two private data fields x and y that represent the coordinates with get methods.
■ A constructor that constructs a point with specified coordinates with default
point (0, 0).
■ A method named distance that returns the distance from this point to another
point of the Point type.
■ A method named isNearBy(p1) that returns true if point p1 is close to this
point. Two points are close if their distance is less than 5.
■ Implement the __str__ method to return a string in the form (x,y).
Implement the class. Write a test program that prompts the user to enter 
two points, displays the distance between them, and indicates whether they are near each other. Here are sample runs:

Enter two points x1, y1, x2, y2: 2.1, 2.3, 19.1, 19.2
The distance between the two points is 23.97
The two points are not near each other

Enter two points x1, y1, x2, y2: 2.1, 2.3, 2.3, 4.2
The distance between the two points is 1.91
The two points are near each other
"""
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})" .format(self.x, self.y)

    def distance(self, other):
        return math.sqrt(((self.x - other.x) ** 2) + ((self.y - other.y) ** 2))

    def isNearBy(self, p1):
        return self.distance(p1) <= 5


"""
(Geometry: The Circle2D class) Define the Circle2D class that contains:
■ Two private float data fields named x and y that specify the center of the circle with get/set methods.
■ A private data field radius 
■ A constructor that creates a circle with the specified x, y, and radius. The
default values are all 0.
■ A method getArea() that returns the area of the circle.
■ A method getPerimeter() that returns the perimeter of the circle.
■ A method containsPoint(x, y) that returns True if the specified point (x,y) is inside this circle.
■ A method contains(circle2D) that returns True if the specified circle is
inside this circle 
■ A method overlaps(circle2D) that returns True if the specified circle
overlaps with this circle.
■ Implement the __contains__(another) method that returns True if this circle is contained in another circle

■ Implement the __cmp__, __lt__, __le__, __eq__, __ne__, __gt__, __ge__ methods that compare two circles based on 
their radius.

Sample Run: 
Enter x1, y1, radius1: 5, 5.5, 10
Enter x2, y2, radius2: 9, 1.3, 10
Area for c1 is 314.1592653589793
Perimeter for c1 is 62.83185307179586
Area for c2 is 314.1592653589793
Perimeter for c2 is 62.83185307179586
c1 contains the center of c2? True
c1 contains c2? False
c1 overlaps c2? True
"""
class Circle2D:
    def __init__(self, x,  y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def getArea(self):
        return math.pi * self.radius ** 2

    def getPerimeter(self):
        return 2 * self.radius * math.pi

    def containsPoint(self, x2, y2):
        return ((x2 - self.x) ** 2) + ((y2 - self.y) ** 2) <= self.radius ** 2

    def __contains__(self, other):
        difference_btw_centres = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return difference_btw_centres + other.radius <= self.radius

    def overlaps(self, other):
        difference_btw_centres = math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)
        return self.radius + other.radius > difference_btw_centres



"""
(Geometry: The Rectangle2D class) Define the Rectangle2D class that contains:
■ Two float data fields named x and y that specify the center of the rectangle with get/set methods. (Assume that the 
rectangle sides are parallel to x- or y- axes.)
■ The data fields width and height
■ A constructor that creates a rectangle with the specified x, y, width, and
height with default values 0.
■ A method get_area() that returns the area of the rectangle.
■ A method get_perimeter() that returns the perimeter of the rectangle.
■ A method contains_point(x, y) that returns True if the specified point (x,y) is inside this rectangle 
■ A method overlaps(Rectangle2D) that returns True if the specified
rectangle overlaps with this rectangle 
■ Implement the __contains__(other) method that returns True if this rectangle is contained in another rectangle.
■ Implement the __cmp__, __lt__, __le__, __eq__, __ne__, __gt__, __ge__ methods that compare two rectangles based on 
their areas.


Implement the class. Write a test programme that prompts the user to enter two rectangles with center x-, y-coordinates, 
width, and height, creates two Rectangle2D objects r1 and r2, displays their areas and perimeters, and displays the 
result of r1.contains_point(r2.x, r2.y), r1.contains(r2), and r1.overlaps(r2). Here is a sample run:

Enter x1, y1, width1, height1: 9, 1.3, 10, 35.3
Enter x2, y2, width2, height2: 1.3, 4.3, 4, 5.3
Area for r1 is 353.0
Perimeter for r1 is 90.6
Area for r2 is 21.2
Perimeter for r2 is 18.6
r1 contains the center of r2? False
r1 contains r2? False
r1 overlaps r2? False
"""
class Rectangle2D:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __contains__(self, other):
        diff_of_x = abs(other.x - self.x)
        diff_of_y = abs(other.y - self.y)
        return diff_of_x + 0.5 * other.width <= 0.5 * self.width and diff_of_y + 0.5 * other.height <= 0.5 * self.height

    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __ne__(self, other):
        return self.get_area() != other.get_area()

    def __gt__(self, other):
        return self.get_area() > other.get_area()

    def __ge__(self, other):
        return self.get_area() >= other.get_area()

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def contain_point(self, x, y):
        return abs(x - self.x) <= (self.width / 2) and abs(y - self.y) <= (self.height / 2)

    def overlaps(self, other):
        return abs(other.x - self.x) < 0.5 * (self.width + other.width) and abs(other.y - self.y) < 0.5 * (self.height + other.height)

















