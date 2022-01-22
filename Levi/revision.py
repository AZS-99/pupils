import math
"""
The US Census Bureau projects population based on the following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population in five years. Assume the current population is 312032486
and one year has 365 days. Hint: in Python, you can use integer division operator // to perform division. The result is
an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
"""
def population(people):
    seconds_per_yr = 365 * 24 * 60 * 60
    births = seconds_per_yr // 7
    deaths = seconds_per_yr // 13
    immigrants = seconds_per_yr // 45
    return people + 5 * (births - deaths + immigrants)


"""
Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result. 
The formula for the conversion is as follows:
      fahrenheit = (9 / 5) * celsius + 32

Sample Run:
Enter a degree in Celsius: 43 

Sample output:
43 Celsius is 109.4 Fahrenheit

"""
def c_to_f(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


"""
Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total. For example, 
if the user enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5 as the gratuity and 11.5 
as the total. Here is a sample run:
Enter the subtotal and a gratuity rate: 15.69, 15
The gratuity is 2.35 and the total is 18.04
"""

def a(subtotal, gratuity_rate,):
    gratuity = subtotal * gratuity_rate * (1 / 100)
    total = gratuity + subtotal
    return round(gratuity, 2), round(total, 2)


"""
Write a program that reads three edges for a triangle and computes the perimeter if the input is valid. Otherwise, 
display that the input is invalid. The input is valid if the sum of every pair of two edges is greater than the 
remaining edge. Here is a sample run:

Enter three edges: 1, 1, 1
The perimeter is 3
"""

def perimeter(first_edge, second_edge, third_edge):
    if first_edge + second_edge < third_edge or second_edge + third_edge < first_edge or third_edge + first_edge < second_edge:
        raise Exception("Not Valid")
    return first_edge + second_edge + third_edge


"""
Suppose you shop for rice and find it in two different sized packages. You would like to write a program to compare the 
costs of the packages. The program prompts the user to enter the weight and price of each package and then displays the 
one with the better price. 

Here is a sample run:
Enter weight and price for package 1: 50, 24.59
Enter weight and price for package 2: 25, 11.99
Package 1 has the better price.
"""

def better_deal(weight, price, weight2, price2):
    price_per_pound1 = weight / price
    price_per_pound2 = weight2 / price2
    if price_per_pound1 < price_per_pound2:
        return 1
    return 2

"""
Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and
displays its area. The formula for computing the area of a triangle is

s = (side1 + side2 + side3)/2
area = sqrt(s(s - side1)(s - side2)(s - side3))

Sample Run:
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
The area of the triangle is 33.6
"""

def triangle_area(x1, y1, x2, y2, x3, y3):
    side1 = math.sqrt(abs(x2 - x1)**2 + abs(y2 - y1)**2)
    side2 = math.sqrt(abs(x3 - x2)**2 + abs(y3 - y2)**2)
    side3 = math.sqrt(abs(x1 - x3)**2 + abs(y1 - y3)**2)
    s = (side1 + side2 + side3)/2
    area = math.sqrt(s * (s - side1)*(s - side2)*(s - side3))
    return round(area, 1)


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

def linear_equation(a, b, c, d, e, f):
    denominator = a * d - b * c
    if denominator == 0:
        return float('inf'), float('inf')
    x = (e * d - b * f) / denominator
    y = (a * f - e * c) / denominator
    return x, y


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

def divisibility(number):
    divisible_by_5 = True if number % 5 == 0 else False
    divisible_by_6 = True if number % 6 == 0 else False
    print("Is", number, "divisible by 5 and 6?", divisible_by_5 and divisible_by_6)
    print("Is", number, "divisible by 5 or 6?", divisible_by_5 or divisible_by_6)
    print("Is", number, "divisible by 5 or 6, but not both?", divisible_by_5 ^ divisible_by_6)


"""
Write a program that prompts the user to enter the minutes (e.g., 1 billion), and displays the number of years and days
for the minutes. For simplicity, assume a year has 365 days. Here is a sample run:

Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days
"""

def minutes(minutes):
    days = minutes / 1440
    years = days // 365
    days = days % 365
    return years, days


