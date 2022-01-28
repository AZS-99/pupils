"""
The US Census Bureau projects population based on the following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for the next five years. Assume the current population is 312032486
and one year has 365 days. Hint: in Python, you can use integer division operator // to perform division. The result is
an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
"""
import math


def arithimetic(population):
    seconds_per_year = 365 * 24 * 60 * 60
    births = seconds_per_year // 7
    deaths = seconds_per_year // 13
    immigrants = seconds_per_year // 45
    population += (births - deaths + immigrants) * 5
    return population


"""
Write a program that reads a number in feet, converts it to meters, and displays the result. One foot is 0.305 meters. 
Here is a sample run:
Enter a value for feet: 16.5
16.5 feet is 5.0325 meters
"""
def convert_to_meters(feet):
    meter = feet * 0.305
    return meter


"""
Write a program that converts pounds into kilograms. The program prompts the user to enter a value in pounds, 
converts it to kilograms, and displays the result. One pound is 0.454 kilograms. Here is a sample run:
Enter a value in pounds: 55.5
55.5 pounds is 25.197 kilograms
"""
def convert_to_kilograms(pounds):
    kilogram = pounds * 0.454
    return kilogram


"""
Assume a runner runs 14 kilometers in 45 minutes and 30 seconds. Write a program that displays the average speed in 
miles per hour. (Note that 1 mile is 1.6 kilometers.) 
Round to the nearest 3 decimal places
"""
def convert_to_mph(km, minutes):
    mile = km / 1.6
    hr = minutes / 60
    speed = mile / hr
    return round(speed, 3)


"""
Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result. 
The formula for the conversion is as follows:
      fahrenheit = (9 / 5) * celsius + 32

Sample Run:
Enter a degree in Celsius: 43 

Sample output:
43 Celsius is 109.4 Fahrenheit
"""
def convert_to_Fahrenheit(Celsius):
    Fahreneit = (9 / 5) * Celsius + 32
    return Fahreneit


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
def investment_amount(investmentamount, annualinterestrate, numberyears ):
    futureInvestmentValue = investmentamount * (1 + (annualinterestrate/100) / 12) ** (numberyears *12)
    return round(futureInvestmentValue, 2)



"""
Write a program that reads three edges for a triangle and computes the perimeter if the input is valid. Otherwise, 
display that the input is invalid. The input is valid if the sum of every pair of two edges is greater than the 
remaining edge. Here is a sample run:

Enter three edges: 1, 1, 1
The perimeter is 3
"""
def perimeter(e1, e2, e3):
    if e1 + e2 > e3 and e2 + e3 > e1 and e1 + e3 > e2:
        return e1 + e2 + e3
    else:
        raise Exception("The values you entered are not valid")


"""
Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total. For example, 
if the user enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5 as the gratuity and 11.5 
as the total. Here is a sample run:
Enter the subtotal and a gratuity rate: 15.69, 15
The gratuity is 2.35 and the total is 18.04
"""
def totalrate(subtotal, gratuity_rate):

    gratuity = subtotal * gratuity_rate/100
    total = subtotal + gratuity
    return round(gratuity, 2), round(total, 2)


"""
Write a program that prompts the user to enter three integers and displays them in ascending order.
Sample run:
Enter 3 numbers: 5, 4, 1
Arranged: [1, 4, 5]
"""
def arrangement(x1,x2,x3):
    lst = [x1, x2, x3]
    lst.sort()
    return lst


"""
Suppose you shop for rice and find it in two different sized packages. You would like to write a program to compare the 
costs of the packages. The program prompts the user to enter the weight and price of each package and then displays the 
one with the better price. 

Here is a sample run:
Enter weight and price for package 1: 50, 24.59
Enter weight and price for package 2: 25, 11.99
Package 1 has the better price.
"""
def compare(weight_1, price_1, weight_2, price_2):
    price_per_kilo_1 = price_1/weight_1
    price_per_kilo_2 = price_2/weight_2
    if price_per_kilo_1 < price_per_kilo_2:
        return price_per_kilo_1
    else:
        return price_per_kilo_2


"""
Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and
displays its area. The formula for computing the area of a triangle is

s = (side1 + side2 + side3)/2
area = sqrt(s(s - side1)(s - side2)(s - side3))

Sample Run:
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
The area of the triangle is 33.6
"""
def find_sides(x1, y1, x2, y2, x3, y3):
    height1 = y1-y2
    base1 = x1-x2
    side1 = math.sqrt(height1 ** 2 + base1 ** 2)

    height2 = y2-y3
    base2 = x2-x3
    side2 = math.sqrt(height2 ** 2 + base2 ** 2)

    height3 = y1-y3
    base3 = x1 - x3
    side3 = math.sqrt(height3 ** 2 + base3 ** 2)

    s = (side1 + side2 + side3)/2
    area = math.sqrt(s*(s - side1)*(s - side2)*(s - side3))
    return round(area, 1)
