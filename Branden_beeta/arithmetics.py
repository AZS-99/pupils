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


def us_population(population):
    birth = 365 * 24 * 60 * 60 // 7
    death = 365 * 24 * 60 * 60 // 13
    immig = 365 * 24 * 60 * 60 // 45
    population = population + 5 * (birth - death + immig)
    print(population)


"""
Write a program that reads a Celsius degree from the console and converts it to Fahrenheit and displays the result.
The formula for the conversion is as follows:
                                fahrenheit = (9 / 5) x celsius + 32

Sample Run:
Enter a degree in Celsius: 43

Sample output:
43 Celsius is 109.4 Fahrenheit

"""

def c_to_f(c):
    return c * 9 / 5 + 32


"""
Write a program that calculates the energy needed to heat water from an initial temperature to a final temperature.
Your program should prompt the user to enter the amount of water in kilograms and the initial and final
temperatures of the water. The formula to compute the energy is
                        Q = M x (finalTemperature – initialTemperature) x 4184
where M is the weight of water in kilograms, temperatures are in degrees Celsius, and energy Q is measured in joules.
Here is a sample run:

Enter the amount of water in kilograms: 55.5
Enter the initial temperature: 3.5
Enter the final temperature: 10.5
The energy needed is 1625484.0
"""
def cal_energy(M, initialTemp, finalTemp):
    return M * (finalTemp - initialTemp) * 4184



"""
Write a program that reads in an investment amount, the annual interest rate, and the number of years, and displays the
future investment value using the following formula:
            futureInvestmentValue = investmentAmount x (1 + monthlyInterestRate)^numberOfMonths
For example, if you enter the amount 1000, an annual interest rate of 4.25%, and the number of years as 1, the future
investment value is 1043.33. Here is a sample run:

Enter investment amount: 1000
Enter annual interest rate: 4.25
Enter number of years: 1
Accumulated value is 1043.33
"""
def future_inv(invest_amount, annual_interest_rate, year):
    months = year * 12
    monthly_interest_rate = annual_interest_rate / 12 / 100
    return invest_amount * (1 + monthly_interest_rate) ** months


"""
Write a program that reads three edges for a triangle and computes the perimeter if the input is valid. Otherwise, 
display that the input is invalid. The input is valid if the sum of every pair of two edges is greater than the 
remaining edge. Here is a sample run:

Enter three edges: 1, 1, 1
The perimeter is 3

Enter three edges: 2, 3, 6
The input is invalid
"""
def tri_perimeter(edge_1,edge_2,edge_3):
    if edge_1 + edge_2 > edge_3 and edge_1 + edge_3 > edge_2 and edge_2 +edge_3 > edge_1:
        print("The perimeter is", edge_1 + edge_2 + edge_3)
    else:
        print("The input is invalid")


"""
Write a program that reads the subtotal and the gratuity rate and computes the gratuity and total. For example, 
if the user enters 10 for the subtotal and 15% for the gratuity rate, the program displays 1.5 as the gratuity and 11.5 
as the total. Here is a sample run:
Enter the subtotal and a gratuity rate: 15.69, 15
The gratuity is 2.35 and the total is 18.04
"""
def gratuity(subtotal,rate):
    gratuity = subtotal * (rate / 100)
    total = gratuity + subtotal
    return gratuity, round(total, 2)


"""
Suppose you shop for rice and find it in two different sized packages. You would like to write a program to compare the 
costs of the packages. The program prompts the user to enter the weight and price of each package and then displays the 
one with the better price. 

Here is a sample run:
Enter weight and price for package 1: 50, 24.59
Enter weight and price for package 2: 25, 12.99
Package 1 has the better price.
"""
def better_price(weight1,price1,weight2,price2):
    # price_p_pound1 = price1 / weight1
    # price_per_pound2 = price2 / weight2
    # if price_per_pound1 > price_per_pound2:
    #     return 2
    # else:
    #     return 1
    pass


"""
Write a program that prompts the user to enter the three points (x1, y1), (x2, y2), and (x3, y3) of a triangle and
displays its area. The formula for computing the area of a triangle is

s = (side1 + side2 + side3)/2
area = √(s(s - side1)(s - side2)(s - side3))

Sample Run:
Enter three points for a triangle: 1.5, -3.4, 4.6, 5, 9.5, -3.4
The area of the triangle is 33.6
"""
def cal_tri_area(x1,y1,x2,y2,x3,y3):
    side1 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    side2 = math.sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    side3 = math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    s = (math.sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2) + side2 + side1) / 2
    return math.sqrt(s * (s - side1) * (s - side2) * (s - side3))


"""
If you know the balance and the annual percentage interest rate, you can compute the interest on the next monthly 
payment using the following formula:
         interest = balance * (annualInterestRate / 1200)
Write a program that reads the balance and the annual percentage interest rate and displays the interest for the next 
month. Here is a sample run:
Enter balance and interest rate (e.g., 3 for 3%): 1000, 3.5 
The interest is 2.91667
"""
def interest(balance,rate):
    return balance * rate / 1200


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
def whether(number):
    rem1 = number % 5
    rem2 = number % 6
    five_xor_six = False
    if rem1 == 0 and rem2 == 0:
        five_and_six = True
    else:
        five_and_six = False
    if rem1 == 0 or rem2 ==0:
        five_or_six = True
        if rem1 != 0 or rem2 != 0:
            five_xor_six = True
    else:
        five_or_six = False

    return five_and_six, five_or_six, five_xor_six


"""
Write a program that prompts the user to enter the minutes (e.g., 1 billion), and displays the number of years and days
for the minutes. For simplicity, assume a year has 365 days. Here is a sample run:

Enter the number of minutes: 1000000000
1000000000 minutes is approximately 1902 years and 214 days
"""
def min_2_years_and_days(minutes):
    years = minutes // (60 * 24 * 365)
    remainder = minutes % (60 * 24 * 365)
    days = remainder // (24 * 60)
    return years, days


"""
Write a program that reads an unspecified number of integers, determines how many positive and negative values have been 
read, and computes the total and average of the input values (not counting zeros). Your program ends with the input 0. 
Display the average as a floating-point number. Here is a sample run:

Enter an integer, the input ends if it is 0: 1
Enter an integer, the input ends if it is 0: 2
Enter an integer, the input ends if it is 0: -1
Enter an integer, the input ends if it is 0: 3
Enter an integer, the input ends if it is 0: 0

The number of positives is 3
The number of negatives is 1
The total is 5
The average is 1.25
"""
def integer():
    count_positive = 0
    count_negative = 0
    total = 0

    x = -1
    while x != 0:
        x = int(input("Enter an integer, the input ends if it is 0:"))
        if x < 0:
            count_negative += 1
        elif x > 0:
            count_positive += 1
        total = total + x
    average = total / (count_positive + count_negative)
    return count_positive, count_negative, total, average


"""
Write a program that prompts the user to enter the month and year and displays the number of days in the month. For 
example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. If the 
user entered month 3 and year 2005, the program should display that March 2005 has 31 days.
"""
def month_year(mont, yea):
    if mont == 1:
        month = "January"
    elif mont == 3:
        month = "March"
    elif mont == 4:
        month = "April"
    elif mont == 5:
        month = "May"
    elif mont == 6:
        month = "June"
    elif mont == 7:
        month = "July"
    elif mont == 8:
        month = "August"
    elif mont == 9:
        month = "September"
    elif mont == 10:
        month = "October"
    elif mont == 11:
        month = "November"
    elif mont == 12:
        month = "December"
    if mont in [1, 3, 5, 7, 8, 10, 12]:
        day = 31
    elif mont in [4, 6, 9, 11]:
        day = 30
    else:
        month = "February"
        remain = yea % 4
        if remain == 0:
            day = 29
        else:
            day = 28
    return month, day


"""
(Financials: currency exchange) Write a program that prompts the user to enter the currency exchange rate between U.S. 
dollars and Chinese Renminbi (RMB). Prompt the user to enter 0 to convert from U.S. dollars to Chinese RMB and 1 for 
vice versa. Prompt the user to enter the amount in U.S. dollars or Chinese RMB to convert it to Chinese RMB or U.S. 
dollars, respectively. Here are some sample runs:

Sample Run 1:
Enter the exchange rate from dollars to RMB: 6.81
Enter 0 to convert dollars to RMB and 1 vice versa: 0
Enter the dollar amount: 100
$100.0 is 681.0 yuan


Sample Run 2:
Enter the exchange rate from dollars to RMB: 6.81
Enter 0 to convert dollars to RMB and 1 vice versa: 1
Enter the RMB amount: 10000
10000.0 yuan is $1468.43
"""
def domb(d_or_rmb, money_amount, rate_dollars_rmb):
    if d_or_rmb == 0:
        return money_amount * rate_dollars_rmb
    else:
        return money_amount / rate_dollars_rmb

