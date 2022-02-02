"""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
def pentagonal_number(n):
    return n * (3 * n - 1) // 2

def pentagonal_numbers():
    count = 0
    for n in range(1, 101):
        pen_num = pentagonal_number(n)
        count += 1
        count %= 10
        print(pen_num, ", ", end="\n" if count == 0 else "")


"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""
def sumDigits(n):
    total = 0
    while n != 0:
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
    answer = 0
    while number != 0:
        answer = answer * 10 + number % 10
        number //= 10
    return answer

def isPalindrome(number):
    if number == reverse(number):
        print("It is palindrome")
    else:
        print("It is not palindrome")


"""
(Sort three numbers) Write the following function to display three numbers in increasing order:
def displaySortedNumbers(num1, num2, num3):
Write a test program that prompts the user to enter three numbers and invokes the function to display them in 
increasing order. 

Here are some sample runs:
Enter three numbers: 3, 2.4, 5
The sorted numbers are 2.4 3 5

Enter three numbers: 31, 12.4, 15
The sorted numbers are 12.4 15 31
"""
def displaySortNumbers(num1, num2, num3):
    lst = [num1, num2, num3]
    lst.sort()
    return lst


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
    futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate) ** (years * 12)
    return futureInvestmentValue


def allInvestments(investmentAmount, monthlyInterestRate):
    print("{:>10} {:>10}".format('Years', 'Future Value'))
    for i in range(1, 31):
        futureInvestment = futureInvestmentValue(investmentAmount, monthlyInterestRate, i)
        print("{:>10} {:>10}".format(i, round(futureInvestment, 2)))


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
def celsiusToFahrenheit(celsius):
    print("{:>10} {:>10} | {:>10} {:>10}".format('Celsius', 'Fahrenhirt', "Fahernheit", "Celsius"))
    count = 0
    for x in range(celsius, celsius - 10, -1):
        fahrenheit = (9 / 5) * x + 32
        fahrenheit2 = 40 * 3 - 10 * count
        celsius2 = (5 / 9) * (fahrenheit2 - 32)
        print("{:>10} {:>10} | {:>10} {:>10}".format(x, round(fahrenheit, 2), round(fahrenheit2, 2), round(celsius2, 2)))
        count += 1


"""
(Display characters) Write a function that prints characters using the following header:
def printChars(ch1, ch2, numberPerLine):
This function prints the characters between ch1 and ch2 with the specified numbers per line. Write a test program that 
prints ten characters per line from 1 to Z.
"""
def printChars(ch1, ch2, numberPerLine):
