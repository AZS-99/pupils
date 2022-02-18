"""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
import math
import loops

def getPentagonalNumber(num):
    pentagonal = num * ((3 * num) - 1 ) // 2
    return pentagonal

def printPentagonalNumber():
    num = 1
    for i in range (1, 10):
        for j in range (1, 10):
            print(getPentagonalNumber(num), end=" ")
            num += 1
        print()


"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""
def sumDigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return sum(digits)


"""
Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):
# Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. 
Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.
"""
def reverse(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    answer = 0
    for i in range(0, len(digits)):
        answer *= 10
        answer += digits[i]
    return answer

def isPalindrome(num):
    return reverse(num) == num



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
def displaySortedNumbers(num1, num2, num3):
    order = [num1, num2, num3]
    order.sort()
    return order



"""
Financial application: compute the future investment value) Write a function that computes a future investment value at 
a given interest rate for a specified number of years. The future investment is determined using the formula:
        futureInvestmentValue = investmentAmount x (1 + monthlyInterestRate)^numberOfMonths
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
    numberOfMonths = years * 12

    futureInvestmentValue = investmentAmount *(1 + monthlyInterestRate) ** numberOfMonths
    return round(futureInvestmentValue, 2)

def printInvestment(initialinvestmentAmount, monthlyInterestRate):
    print("{:<10} {:<10}".format("Years", "Future Value"))
    for i in range(1, 31):
        print("{:<10} {:<10}" .format(i ,futureInvestmentValue(initialinvestmentAmount,monthlyInterestRate, i)))


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
    return (9 / 5) * celsius + 32

def fahrenheitToCelsius(fahrenheit):
    return (5 / 9) * (fahrenheit - 32)

def printtemp():
    celsius = 40
    fahrenheit = 120
    print("{:<5} {:<10} | {:<10} {:<20}".format("Celsius", "Fahrenheit", "Fahrenheit", "Celsius"))
    for i in range(40, 30, -1):
        f1 = celsiusToFahrenheit(celsius)
        c1 = fahrenheitToCelsius(fahrenheit)
        print("{:<7} {:<10} | {:<10} {:<20}".format(celsius, round(f1, 2), fahrenheit, round(c1, 2)))
        fahrenheit -= 10
        celsius -= 1


"""
(Display characters) Write a function that prints characters using the following header:
def printChars(ch1, ch2, numberPerLine):
This function prints the characters between ch1 and ch2 with the specified numbers per line. Write a test program that 
prints ten characters per line from A to Z.
"""
def printChars(ch1, ch2, numberPerLine):
    ord1 = ord(ch1)
    ord2 = ord(ch2)
    charnum = ord1
    for i in range(ord1, ord2):
        for j in range(numberPerLine):
            print(chr(charnum), end=" ")
            charnum +=1
            if charnum > 90:
                return
        print()


"""
(Conversions between feet and meters) Write a module that contains the following two functions:
# Converts from feet to meters
def footToMeter(foot):
# Converts from meters to feet
def meterToFoot(meter):
The formulas for the conversion are:
                                foot = meter / 0.305    
                                meter = 0.305 * foot
Write a test program that invokes these functions to display the following tables:
Feet       Meters  | Meters     Feet
1.0        0.305   | 20.0       66.574
2.0        0.610   | 26.0       81.967
...
9.0        2.745   | 68         222.951
10.0       3.050   | 74         242.623
"""
def footToMeter(foot):
    return 0.305 * foot

def meterToFoot(meter):
    return meter / 0.305

def printdist():
    feet = 1
    meter = 20
    print("{:<4} {:<10} | {:<10} {:<20}".format("Feet", "Meters", "Feet", "Meters"))
    for i in range(1, 11, 1):
        f1 = footToMeter(feet)
        m1 = meterToFoot(meter)
        print("{:<4} {:<10} | {:<10} {:<20}".format(feet, round(f1, 3), meter, round(m1, 3)))
        meter += 6
        feet += 1


"""
Provide the isPrime(number) function for testing whether a number is prime. Use this function to count the number of 
prime numbers less than 10,000.
"""
def isPrime(num):
    factors = math.sqrt(num)
    rf = math.floor(factors)
    while rf > 1:
        if num % rf == 0:
            return False
        rf -=1
    return True

def primecount():
    count = 0
    for i in range(10000, 1, -1):
        if isPrime(i) == True:
            count += 1
    print(count)


"""
(Sum series) Write a function to compute the following series: 
                    m(i)= 1/2 + 2/3 +  .... + i /(i + 1)
Write a test program that displays the following table:
i               m(i)
1               0.5000
2               1.1667
... 
19              16.4023
20              17.3546
"""
def fracsum(i):
    num = 1
    denom = num + 1
    total = 0
    for i in range(i):
        total += num/denom
        num += 1
        denom += 1
    return total

def fraclist():
    for i in range(1, 21):
        print("{:<5} {:<10}".format(i, round(fracsum(i), 4)))


"""
(Estimate π) π can be computed using the following series:
m(i) = 4(1 - 1/3 + 1/5 - 1/7 + 1/9 - 1/11 + .... + (-1)^(i+1)/(2i - 1)) 
Write a function that returns m(i) for a given i and write a test program that displays the following table:
 i                   m(i)
 1                   4.0000
 101                 3.1515
 201                 3.1466
 301                 3.1449
 401                 3.1441
 501                 3.1436
 601                 3.1433
 701                 3.1430
 801                 3.1428
 901                 3.1427
"""
def picalc(i):
    for i in range()