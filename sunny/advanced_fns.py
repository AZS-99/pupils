"""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, 3, and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
def getPentagonalNumber(n):
    return n * (3 * n - 1) // 2

def program():
    for i in range(1, 101):
        print(getPentagonalNumber(i))


"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""
def sumDigits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


"""
Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):
# Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. 
Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.
"""
def reverse(number):
    reversed_num = 0
    while number > 0:
        reversed_num = reversed_num * 10 + original % 10
        number //= 10
    return reversed_num

def isPalindrome(number):
    r_number = reverse(number)
    if r_number == number:
        return True
    return False


"""
Financial application: compute the future investment value) Write a function that computes a future investment value at 
a given interest rate for a specified number of years. The future investment is determined using the formula:
        futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)^numberOfMonths
Use the following function header:
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
For example, futureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.
Write a test program that prompts the user to enter the investment amount and the annual interest rate in percent and 
prints a table that displays the future value for the years from 1 to 30. Here is a sample run:
The amount invested: 1000
Annual interest rate: 9
Years           Future Value
1               1093.80
2               1196.41
... 
29              13467.25
30              14730.57
"""
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount * (1 + monthlyInterestRate) ** (years * 12)

def format(amount, annual_interest):
    print("{:<10} {:>10}".format("years", "future value"))
    for i in range(1, 31):
        future_value = futureInvestmentValue(amount, annual_interest/1200, i)
        print("{:<10} {:>10}".format(i, future_value))


"""
(Conversions between Celsius and Fahrenheit) Write a module that contains the following two functions:
     # Converts from Celsius to Fahrenheit
def celsiusToFahrenheit(celsius):
# Converts from Fahrenheit to Celsius
def fahrenheitToCelsius(fahrenheit): The formulas for the conversion are:
celsius = (5 / 9) * (fahrenheit – 32) fahrenheit = (9 / 5) * celsius + 32
Celsius      Fahrenheit   |   Fahrenheit  Celsius
40.0         104.0        |   120.0       48.89 
39.0         102.2        |   110.0       43.33
...
32.0         89.6         |   40.0        4.44
31.0         87.8         |   30.0        -1.11
"""
# def format():
#     print("{:<10} {:<10}".format("Celsius", "Fahrenheit"))
#     for i in range(40, 30, -1):
#         f = celsiusToFahrenheit(i)
#         print("{:<10} {:<10}".format(i, f))

def formatfc():
    print("{:<10} {:<10}".format("Celsius", "Fahrenheit"))
    for j in range(120, 29, -10):
        c = (5 / 9) * (j - 32)
        print("{:<10} {:<10}".format(j, c))

def celsiusToFahrenheit(celsius):
    return (9 / 5) * celsius + 32

def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * fahrenheit - 32


"""
Provide the isPrime(number) function for testing whether a number is prime. 
Use this function to find the number of 
prime numbers less than 10,000.
"""

def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def number():
    count = 0
    for i in range(2, 10000):
        if isPrime(i):
            count += 1
    return count


"""
Write a program that prompts the user to enter an integer n, the displays the result of 1^2 + 2^2 + 3^2 + ... + n^2
"""
def integer():
    n = int(input("Enter a number: "))
    total = 0
    for i in range(1, n):
        total += i**2
    print(total)















