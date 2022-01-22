"""
Assume a runner runs 14 kilometers in 45 minutes and 30 seconds. Write a program that displays the average speed in
miles per hour. (Note that 1 mile is 1.6 kilometers.)
Round to the nearest 3 decimal places
"""
import math
def speed (kilometers, mins):
    miles = kilometers / 1.6
    hours = mins / 60
    totalspeed = miles / hours
    return round(totalspeed, 3)


"""
The US Census Bureau projects population based on the following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for the next five years. Assume the current population is 312032486 
and one year has 365 days. Hint: in Python, you can use integer division operator // to perform division. The result is 
an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
"""
def pop (currentpop):
    yearseconds = 365 * 24 * 60 * 60
    births = yearseconds * 5 // 7
    deaths = yearseconds * 5 // 13
    immigrants = yearseconds * 5 // 45
    currentpop += births
    currentpop -= deaths
    currentpop += immigrants
    return currentpop


"""
Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result. 
The formula for the conversion is as follows:
      fahrenheit = (9 / 5) * celsius + 32

Sample Run:
Enter a degree in Celsius: 43 

Sample output:
43 Celsius is 109.4 Fahrenheit

"""
def converttemp (cel):

    fahr = (9 / 5) * cel + 32
    return fahr


"""
Write a program that reads three edges for a triangle and computes the perimeter if the input is valid. Otherwise, 
display that the input is invalid. The input is valid if the sum of every pair of two edges is greater than the 
remaining edge. Here is a sample run:

Enter three edges: 1, 1, 1
The perimeter is 3
"""


def triangles (edge1, edge2, edge3):
    if edge1 > edge2 + edge3 or edge2 > edge1 + edge3 or edge3 > edge1 + edge2:
        raise Exception("The values you entered are not valid")
    per = edge1 + edge2 + edge3
    return per


"""
Write a program that prompts the user to enter an integer and checks whether the number is divisible by both 5 and 6, 
divisible by 5 or 6, or just one of them (but not both).

sample run 1:

Enter an integer: 10
Is 10 divisible by 5 and 6? False
Is 10 divisible by 5 or 6? True
Is 10 divisible by 5 or 6, but not both? True

sample run 2:

Enter an integer: 30
Is 30 divisible by 5 and 6? True
Is 30 divisible by 5 or 6? True
Is 30 divisible by 5 or 6, but not both? False
"""
def divrules (num):
    div5 = False
    div6 = False
    if num % 5 == 0:
        div5 = True
    if num % 6 == 0:
        div6 = True
    print("Is", num, "divisible by 5 and 6?", True if div6 and div5 else False)
    print("Is", num, "divisible by 5 or 6?", True if div6 or div5 else False)
    print("Is", num, "divisible by 5 or 6, but not both?", True if div6 ^ div5 else False)


"""
Write a program that prompts the user to enter the minutes (e.g., 1 billion), and displays the number of years and days
for the minutes. For simplicity, assume a year has 365 days. Here is a sample run:

Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days
"""
def timeconvert (mins):
    days = mins // (24 * 60)
    years = days // 365
    days = days % 365
    return days, years


"""
Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and 
displays its area. The formula for computing the area of a triangle is

s = (side1 + side2 + side3)/2
area = sqrt(s(s - side1)(s - side2)(s - side3))

Sample Run:
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
The area of the triangle is 33.6
"""
def trianglearea (x1, y1, x2, y2, x3, y3):
    side1 = math.sqrt(abs(x1 - x2)**2 + abs(y1 - y2)**2)
    side2 = math.sqrt(abs(x2 - x3)**2 + abs(y2 - y3)**2)
    side3 = math.sqrt(abs(x3 - x1)**2 + abs(y3 - y1)**2)
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s*(s - side1)*(s - side2)*(s - side3))
    return round(area, 1)


"""
Write a program that reads in an investment amount, the annual interest rate, and the number of years, and displays the 
future investment value using the following formula:
futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)^numberOfMonths
For example, if you enter the amount 1000, an annual interest rate of 4.25%, and the number of years as 1, the future 
investment value is 1043.33. Here is a sample run:

Enter investment amount: 1000
Enter annual interest rate: 4.25
Enter number of years: 1
Accumulated value is 1043.33
"""
def investmentpredictor (amt, interest, years):
    monthlyinterest = (interest/100) / 12
    months = years * 12
    futureInvestmentValue = amt * (1 + monthlyinterest)**months
    return round(futureInvestmentValue, 2)

"""
Suppose you save $100 each month into a savings account with an annual interest rate of 5%. Therefore, the monthly 
interest rate is 0.05/12 = 0.00417. After the first month, the value in the account becomes
          100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
          (100 + 100.417) * (1 + 0.00417) = 201.252
After the third month, the value in the account becomes
          (100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
Write a program that prompts the user to enter a monthly saving amount and displays the account value after the sixth 
month. Here is a sample run of the program:
Enter the monthly saving amount: 100
After the sixth month, the account value is 608.81
"""
def compoundinterest (amt, months):
    rate = 1 + 0.00417
    for i in range (months):
        amt += 100 if i > 0 else 0
        amt *= rate

        print("Amount on month", i, "is", amt)
    return round(amt, 2)


"""
The two roots of a quadratic equation, for example, ax^2 + bx + c = 0, can be obtained using the following formula:
r1=(-b + sqrt(b^2-4ac)) / 2a and r2=(-b - sqrt(b^2-4ac)) / 2a
b^2 - 4ac is called the discriminant of the quadratic equation. If it is positive, the equation has two real roots. If 
it is zero, the equation has one root. If it is negative, the equation has no real roots.
Write a program that prompts the user to enter values for a, b, and c and displays the result based on the discriminant. 
If the discriminant is positive, display two roots. If the discriminant is 0, display one root. Otherwise, display The 
equation has no real roots. Here are some sample runs.

Sample Run 1: 
Enter a, b, c: 1.0, 3, 1
The roots are -0.381966 and -2.61803

Sample Run 2:
Enter a, b, c: 1, 2.0, 1
The root is -1

Sample Run 3:
Enter a, b, c: 1, 2, 3
The equation has no real roots
"I'm trying to connnect through PyCharm"

"""
def quadratics (a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("The equation has no real roots")
    elif discriminant == 0:
        print("The root is", str(-b / (2 * a)))
    else:
        r1 = -b + math.sqrt(discriminant) / (2 * a)
        r2 = -b - math.sqrt(discriminant) / (2 * a)
        print("The roots are" + str(r1) + "and", str(r2))



"""
You can use Cramer’s rule to solve the following 2 * 2 system of linear equation:
ax + by = e
cx + dy = f

x = (ed - bf) / (ad - bc)
y = (af - ec) / (ad - bc)

Write a program that prompts the user to enter a, b, c, d, e, and f and display the result. If (ad – bc) is 0, report 
that The equation has no solution.

Sample Run 1:
Enter a, b, c, d, e, f: 9.0, 4.0, 3.0, -5.0, -6.0, -21.0
x is -2.0 and y is 3.0

Sample Run 2:
Enter a, b, c, d, e, f: 1.0, 2.0, 2.0, 4.0, 4.0, 5.0
The equation has no solution
"""
def cramer (a, b, c, d, e, f):
    denominator = (a * d) - (b * c)
    if denominator == 0:
        return float("inf"), float("inf")
    else:
        x = (e * d - b * f) / denominator
        y = (a*f - e*c) / denominator
        return x, y
