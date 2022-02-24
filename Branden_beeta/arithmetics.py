"""
The US Census Bureau projects population based on the following assumptions:
One birth every 7 seconds
One death every 13 seconds
One new immigrant every 45 seconds
Write a program to display the population for the next five years. Assume the current population is 312032486
and one year has 365 days. Hint: in Python, you can use integer division operator // to perform division. The result is
an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
"""

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
    price_p_pound1 = price1 / weight1
    price_per_pound2 = price2 / weight2
    if price_per_pound1 > price_per_pound2:
        return 2
    else:
        return 1