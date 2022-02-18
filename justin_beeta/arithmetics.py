import math

"""
Write a program that displays the area and perimeter of a circle that has a radius of 5.5 using the following formulas:
area = radius * radius * pi
perimeter = 2 * radius * pi
Find the answer to the nearest 2 decimal places.
"""
def area_and_perimeter(radius):
    print(round(radius * radius * math.pi, 2))
    print(2 * radius * math.pi)



"""
Write a program that reads a number in feet, converts it to meters, and displays the result. One foot is 0.305 meters. 
Here is a sample run:
Enter a value for feet: 16.5
16.5 feet is 5.0325 meters
"""
def convert_to_meters(feet):
    meters = feet * 0.305
    return meters


"""
Assume a runner runs 14 kilometers in 45 minutes and 30 seconds. Write a program that displays the average speed in 
miles per hour. (Note that 1 mile is 1.6 kilometers.) 
Round to the nearest 3 decimal places
"""
def average_speed(kilometers, mins):
    miles = kilometers / 1.6
    hrs = mins / 60
    return round((miles / hrs), 3)


"""
The US Census Bureau projects population based on the following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for the next five years. Assume the current population is 312032486
and one year has 365 days. Hint: in Python, you can use integer division operator // to perform division. The result is 
an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
"""
def theuscensusbureauproject():
    seconds = 365 * 24 * 60 * 60
    births = seconds // 7
    death = seconds // 13
    immigrant = seconds // 45
    change_in_population = births + immigrant - death
    change_in_population_5 = change_in_population * 5
    return change_in_population_5 + 312032486


"""
Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result. 
The formula for the conversion is as follows:
                                fahrenheit = (9 / 5) * celsius + 32

Sample Run:
Enter a degree in Celsius: 43 

Sample output:
43 Celsius is 109.4 Fahrenheit


Sample Run 2:
Enter a degree in Celsius: 44
44 Celsius is 110 Fahrenheit
"""
def fahrenheit_question(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit


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
def water(M, finalTemperature, initialTemparaeture):
    Q = M * (finalTemperature - initialTemparaeture) * 4184
    return Q


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
def annual(investmentAmount, annualinterestrate, numberOfYears):
    monthlyInterestRate = annualinterestrate / 100 / 12
    numberOfMonths = numberOfYears * 12
    futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** numberOfMonths
    return futureInvestmentValue


"""
Write a program that reads three edges for a triangle and computes the perimeter if the input is valid. Otherwise, 
display that the input is invalid. The input is valid if the sum of every pair of two edges is greater than the 
remaining edge. Here is a sample run:

Enter three edges: 1, 1, 1
The perimeter is 3

Enter three edges: 1, 1, 3
The input is invalid
"""
def get_triangle_perimeter(edge1, edge2, edge3):
    if edge1 + edge2 <= edge3 or edge1 + edge3 <= edge2 or edge2 + edge3 <= edge1:
        print("invalid")
    else:
        print("The perimeter is", edge1 + edge2 + edge3)


"""
Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total. For example, 
if the user enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5 as the gratuity and 11.5 
as the total. Here is a sample run:
Enter the subtotal and a gratuity rate: 15.69, 15
The gratuity is 2.35 and the total is 18.04
"""
def gratuity(subtotal, gratuity_rate):
    gratuity = subtotal * (gratuity_rate / 100)
    the_total = subtotal + gratuity
    return round(gratuity, 2), round(the_total, 2)


"""
Write a program that prompts the user to enter three integers and displays them in ascending order.
Sample run:
Enter 3 numbers: 5, 4, 1
Arranged: [1, 4, 5]
"""
def ascending_order(num1, num2, num3):
    lst = [num1, num2, num3]
    lst.sort()
    return lst


"""
Suppose you shop for rice and find it in two different sized packages. You would like to write a program to compare the 
costs of the packages. The program prompts the user to enter the weight and price of each package and then displays the 
one with the better price. 

Here is a sample run:
Enter weight and price for package a: 50, 24.59
Enter weight and price for package b: 25, 12.99
Package 1 has the better price.
"""
def rice(weight1, price1, weight2, price2):















