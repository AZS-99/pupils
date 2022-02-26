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
    total = 0
    sign = True
    for j in range(1, 2*i, 2):
        if sign == False:
            total -= (1 / j)
        elif sign == True:
            total += (1 / j)
        sign = not sign
    total *= 4
    return (round(total, 4))

def printpi():
    print("{:<10} {:<10}".format("i", "m(i)"))
    for i in range(1, 902, 100):
        print("{:<10} {:<10}".format(i, picalc(i)))

"""
(Math: approximate the square root) There are several techniques for implementing the sqrt function in the math module. 
One such technique is known as the Babylonian function. It approximates the square root of a number, n, by repeatedly 
performing a calculation using the following formula:
                            nextGuess = (lastGuess + (n / lastGuess)) / 2
When nextGuess and lastGuess are almost identical, nextGuess is the approximated square root. The initial guess can be 
any positive value (e.g., 1). This value will be the starting value for lastGuess. If the difference between nextGuess 
and lastGuess is less than a very small number, such as 0.0001, you can claim that nextGuess is the approximated square 
root of n. If not, nextGuess becomes lastGuess and the approximation process continues. Implement the following function 
that returns the square root of n.
"""

def calcsqrt(n):
    nextGuess = n / 2
    lastGuess = 0
    while abs(nextGuess - lastGuess) >= 0.0001:
        lastGuess = nextGuess
        nextGuess = (lastGuess + (n / lastGuess)) / 2

    return round(nextGuess, 3)


"""
(Convert milliseconds to hours, minutes, and seconds) Write a function that converts milliseconds to hours, minutes, 
and seconds using the following header:
def convertMillis(millis):
The function returns a string as hours:minutes:seconds. For example, convertMillis(5500) returns the string 0:0:5, 
convertMillis(100000) returns the string 0:1:40, and convertMillis(555550000) returns the string 154:19:10.
Write a test program that prompts the user to enter a value for milliseconds and displays a string in the format of 
hours:minutes:seconds.
"""
def timeprint(millis):
    total_seconds = millis // 1000
    seconds = total_seconds % 60
    mins = total_seconds // 60
    hours = mins // 60
    mins = mins % 60
    print("{0}:{1}:{2}".format(hours,mins,seconds))


"""
A palindromic prime is a prime number that is also palindromic. For example, 131 is a prime and also a palindromic 
prime, as are 313 and 757. Write a program that displays the first 100 palindromic prime numbers. Display 10 numbers 
per line and align the numbers properly, as follows:
 2     3     5     7    11    101    131   151   181   191
313   353   373   383   727   757    787   797   919   929
"""
def palindrome(num):
    if reverse(num) == num:
        return True

def palindromeprint():
    currentnum = 1
    pprimecount = 0
    pprimes = []
    loopcount = 0
    while pprimecount < 100:
        if isPalindrome(currentnum) and isPrime(currentnum):
            pprimecount +=1
            pprimes.append(currentnum)
        currentnum += 1
    for i in range(2):
        for j in range(10):
            loopcount += 1
            print("{:<5}".format(pprimes[loopcount]), end=" ")
        print()


"""
An emirp ( prime spelled backward) is a non-palindromic prime number whose reversal is also a prime. For example, both 
17 and 71 are prime numbers, so 17 and 71 are emirps. Write a program that displays the first 100 emirps. Display 10 
numbers per line and align the numbers properly, as follows:
 13   17   31   37   71   73   79   97  107  113
149  157  167  179  199  311  337  347  359  389
"""
def emirps():
    currentnum = 1
    pemirpcount = 0
    pemirps = []
    loopcount = 0
    while pemirpcount < 100:
        if not isPalindrome(currentnum) and isPrime(reverse(currentnum)) and isPrime(currentnum):
            pemirpcount +=1
            pemirps.append(currentnum)
        currentnum += 1

    for i in range(2):
        for j in range(10):
            print("{:<5}".format(pemirps[loopcount]), end=" ")
            loopcount += 1
        print()


"""
(Mersenne prime) A prime number is called a Mersenne prime if it can be written in the form 2p - 1 for some positive 
integer p. Write a program that finds all Mersenne primes with p ... 31 and displays the output as follows:
p               2^p - 1 
2               3
3               7
5               31
.
.
.
31
"""
def mersenneprimes():
    print("{:<10}{:<10}".format("p", "2^p - 1"))
    for i in range(2, 32):
        if 1 % 2**i - 1 == 0:
            print("{:<10}{:<10}".format(i, 2**i - 1))