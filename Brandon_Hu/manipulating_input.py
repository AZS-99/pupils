
"""
Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total. For example,
if the user enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5 as the gratuity and 11.5
as the total. Here is a sample run:
Enter the subtotal and a gratuity rate: 15.69, 15
The gratuity is 2.35 and the total is 18.04
"""
import math


def total(subtotal, gratuity_rate):
    rate = gratuity_rate / 100
    tip = subtotal * rate
    total = subtotal + tip
    return round(total, 2)


"""
Write a program that reads three edges for a triangle and computes the perimeter if the input is valid. Otherwise, 
display that the input is invalid. The input is valid if the sum of every pair of two edges is greater than the 
remaining edge. Here is a sample run:



The perimeter is 3
"""
def tri (edge1 ,edge2, edge3):
    if edge1 + edge3 < edge2 or edge3 + edge2 < edge1 or edge2 + edge1 < edge3:
        raise Exception("These values are not valid for a triangle")
    perimeter = edge1 + edge2 + edge3
    return perimeter


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
def divisible(integer):
    remainder_when_divided_by_5 = integer % 5
    divisible_by_5 = (remainder_when_divided_by_5 == 0)
    divisible_by_6 = (integer % 6 == 0)
    print("This is divisible by 5:", divisible_by_5)
    print("is", integer, "divisible by 5 and 6?", divisible_by_5 and divisible_by_6)
    print("is", integer, "divisible by 5 or 6?", divisible_by_5 or divisible_by_6)
    print("is", integer, "divisible by 5 or 6, but not both?", divisible_by_5 ^ divisible_by_6)


"""
Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature.
Your program should prompt the user to enter the amount of water in kilograms and the initial and final
temperatures of the water. The formula to compute the energy is
        Q = M * (finalTemperature – initialTemperature) * 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius, and energy Q is measured in joules.
Here is a sample run:

Enter the amount of water in kilograms: 55.5
Enter the initial temperature: 3.5
Enter the final temperature: 10.5
The energy needed is 1625484.0
"""
def warming_water(amount_of_water, initial_temperature, final_temperature):
    joules = amount_of_water * (final_temperature - initial_temperature) * 4184
    print("The energy needed is", joules)



"""
Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and
displays its area. The formula for computing the area of a triangle is

s = (side1 + side2 + side3)/2
area = sqrt(s(s - side1)(s - side2)(s - side3))

Sample Run:
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
The area of the triangle is 33.6
"""
def tri(x1, y1, x2, y2, x3, y3):
    n1 = abs(x1 - x2)
    n2 = abs(y1 - y2)
    side1 = math.sqrt(n1 ** 2 + n2 ** 2)

    n3 = abs(x2 - x3)
    n4 = abs(y2 - y3)
    side2 = math.sqrt(n3 ** 2 + n4 ** 2)

    n5 = abs(x1 - x3)
    n6 = abs(y1 - y3)
    side3 = math.sqrt(n5 ** 2 + n6 **2)

    s = (side1 + side2 + side3)/2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
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
def cramer(a, b, c, d, e, f):
    x = (e*d - b*f) / (a*d - b*c)
    y = (a*f - e*c) / (a*d - b*c)
    return x,y


"""
The two roots of a quadratic equation, for example, ax^2 + bx + c = 0, can be obtained using the following formula:
r1 = (-b + sqrt(b^2-4ac)) / 2a and r2 = (-b - sqrt(b^2-4ac)) / 2a
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
"""
def root(a, b, c):
    if b**2 - 4 * a * c >0:
        r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / 2 * a
        return r1, r2
    elif b**2 - 4 * a * c == 0:
        r = -b / (2 * a)
        return r, float('inf')
    else:
        return float("inf"), float('inf')


"""
(Financials: currency exchange) Write a program that prompts the user to enter the currency exchange rate between U.S. 
dollars and Chinese Renminbi (RMB). Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for 
vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to convert it to Chinese RMB or U.S. 
dollars, respectively. Here are some sample runs:

Enter the exchange rate from dollars to RMB: 6.81
Enter 0 to convert dollars to RMB and 1 vice versa: 0
Enter the dollar amount: 100
$100.0 is 681.0 yuan

Enter the exchange rate from dollars to RMB: 6.81
Enter 0 to convert dollars to RMB and 1 vice versa: 1
Enter the RMB amount: 10000
10000.0 yuan is $1468.43
"""
def currency_exchange(rate, money, conversion_num):
    if conversion_num == 0:
        return money * rate
    else:
        return round(money / rate, 2)



"""
Write a program that prompts the user to enter the month and year and displays the number of days in the month. For 
example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. If the 
user entered month 3 and year 2005, the program should display that March 2005 has 31 days.
"""
def months(month, years):
    lst_31 = [1, 3, 5, 7, 8, 10, 12]
    lst_30 = [4, 6, 9, 11]
    if month in lst_31:
        return 31
    elif month in lst_30:
        return 30
    else:
        if years % 4 == 0:
            return 29
        else:
            return 28


