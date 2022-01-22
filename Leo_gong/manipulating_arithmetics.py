import math



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
    side_1 = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
    side_2 = math.sqrt(abs(x2 - x3) ** 2 + abs(y2 - y3) ** 2)
    side_3 = math.sqrt(abs(x1 - x3) ** 2 + abs(y1 - y3) ** 2)
    s = (side_1 + side_2 + side_3) / 2
    area = math.sqrt(s * (s - side_1) * (s - side_2) * (s - side_3))
    return round(area, 2)


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
def money(investment_amount, annual_interest_rate, number_year):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    number_months = number_year * 12
    future_investment_value = investment_amount * (1 + monthly_interest_rate) ** number_months
    return round(future_investment_value, 2)


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
def money_2(monthly_saving):
    interest_rate = 0.05 / 12
    amount = monthly_saving * (1 + interest_rate)
    for i in range(5):
        amount = (amount + 100) * (1 + interest_rate)
    return round(amount, 2)


"""
If you know the balance and the annual percentage interest rate, you can compute the interest on the next monthly 
payment using the following formula:
         interest = balance * (annualInterestRate / 1200)
Write a program that reads the balance and the annual percentage interest rate and displays the interest for the next 
month. Here is a sample run:
Enter balance and interest rate (e.g., 3 for 3%): 1000, 3.5 
The interest is 2.91667
"""
def balance(balance_1, interest_rate):
    interest = balance_1 * (interest_rate / 1200)
    return round(interest, 5)


"""
Write a program that prompts the user to enter a four-digit integer and displays the number in reverse order. 
Here is a sample run:
Enter an integer: 3125
The reversed number is 5213
"""
def reversed_number(integer):
    reversed_num = integer[::-1]
    return reversed_num


"""
The two roots of a quadratic equation, for example, ax^2 + bx + c = 0, can be obtained using the following formula:
r1=(-b+ sqrt(b^2-4ac)) / 2a and r2=(-b-sqrt(b^2-4ac)) / 2a
b2 - 4ac is called the discriminant of the quadratic equation. If it is positive, the equation has two real roots. If 
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
def numbers(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    if discriminant < 0:
        print("The equation has no real roots")
    else:

        r1 = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        r2 = (-b - math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        if r1 == r2:
            print("The root is", round(r1, 6))
        else:
            print("The roots are", round(r1, 6), "and", round(r2, 6))


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
def x_y(a, b, c, d, e, f):
    if (a * d - b * c) == 0:
        print("The equation has no solution")
    else:
        x = (e * d - b * f) / (a * d - b * c)
        y = (a * f - e * c) / (a * d - b * c)
        print("x is", x, "and y is", y)


"""
Write a program that prompts the user to enter the month and year and displays the number of days in the month. For 
example, if the user entered month 2 and year 2000, the program should display that February 2000 has 29 days. If the 
user entered month 3 and year 2005, the program should display that March 2005 has 31 days.
"""
def number_days(years, month):
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month in [4, 6, 9, 11]:
        return 30
    else:
        if years % 4 == 0:
            return 29
        else:
            return 28


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
def dollars(rate, dollar, us_cn):
    if us_cn == 0:
        money = dollar * rate
    elif us_cn == 1:
        money = dollar / rate
    return money


