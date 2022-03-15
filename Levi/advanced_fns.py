
"""""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
def getPentagonalNumber(n):
    x = n*(3*n - 1)//2
    return x

def getPentagonalNumber2():
    num = 1
    for i in range(1, 10):
        for j in range(10):
            print(getPentagonalNumber(num), end=" ")
            num += 1
        print()



"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""
def sumDigits(n):
    total = 0
    while n > 0:
        units_digit = n % 10
        total += units_digit
        n = n // 10
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
    total = 0
    while number > 0:
        total *= 10
        y = number % 10
        total += y
        number //= 10
    return total

def isPalindrome(number):
    if number == reverse(number):
        return True
    return False


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
    numbers = [num1, num2, num3]
    minimum_number = min(numbers)
    maximum_number = max(numbers)
    middle_number =  any(n != minimum_number and n != maximum_number for n in numbers)
    return minimum_number, middle_number, maximum_number



"""
(Financial application: compute the future investment value) Write a function that computes a future investment value at 
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
    numberofMonths = years * 12
    futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)**numberofMonths
    return futureInvestmentValue

def futureInvestmentValue2(investmentAmount, monthlyInterestRate):
    print("{:<10} {:<15}".format("Years", "Future Value"))
    for i in range(1, 31):
        future_value = futureInvestmentValue(investmentAmount, monthlyInterestRate, i)
        print("{:<10} {:<15}".format(i, future_value))



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

def celsiustoFahrenheit(celsius):
    fahrenheit = (9 / 5) * celsius + 32
    return fahrenheit

def fahrenheitToCelsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius

def tables():
    print("{:<15} {:<15} | {:<15} {:<15}".format("Celsius", "Fahrenheit", "Fahrenheit", "Celsius"))
    count = 0
    for i in range(40, 30, -1):
        celsius = i
        fahrenheit = round(celsiustoFahrenheit(celsius),2)
        fahrenheit2 = 40 * 3 - 10 * count
        celsius2 = round(fahrenheitToCelsius(fahrenheit2),2)
        count += 1
        print("{:<15} {:<15} | {:<15} {:<15}".format(celsius, fahrenheit, fahrenheit2, celsius2))


"""
(Display characters) Write a function that prints characters using the following header:
def printChars(ch1, ch2, numberPerLine):
This function prints the characters between ch1 and ch2 with the specified numbers per line. Write a test program that 
prints ten characters per line from A to Z.
"""
def printChars(ch1, ch2, numberPerLine):
    count = 1
    for i in range(ord(ch1), ord(ch2)):
        for a in range(10):
            print(chr(ord(ch1) + count), end=" ")
            count += 1
            if count >= ord(ch2):
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
    meter = 0.305 * foot
    return meter

def meterToFoot(meter):
    foot = meter / 0.305
    return foot

def tables2():
    print("{:<15} {:<15} | {:<15} {:<15}".format("Feet", "Meters", "Meters", "Feet"))
    count = 0
    for i in range(1, 11):
        feet = i
        meters = footToMeter(feet)
        meters2 = i * 6 + 14
        feet2 = round(meterToFoot(meters2),3)
        count += 1
        print("{:<15} {:<15} | {:<15} {:<15}".format(feet, meters, meters2, feet2))


"""
Provide the isPrime(number) function for testing whether a number is prime. Use this function to find the number of 
prime numbers less than 10,000.
"""
def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def count():
    count2 = 0
    for i in range(2, 10001):
        if isPrime(i) == True:
            count2 += 1
    return count2


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

def m(i):
    total = 0
    for j in range(1,i + 1):
        total += j /(j + 1)
    return round(total,4)

def table():
    print("{:<15} {:<15}".format("i", "m(i)"))
    for i in range(1, 21):
        print("{:<15} {:<15}".format(i, m(i)))


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

def estimatePi(i):
    total2 = 0
    for l in range(1, i + 1):
        total2 += (-1)**(l+1) / (2*l - 1)
    return round(total2 * 4, 4)
