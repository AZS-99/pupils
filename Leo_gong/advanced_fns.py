"""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
import math
import random


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
def reverse_1(number):
    answer = 0
    while number != 0:
        answer = answer * 10 + number % 10
        number //= 10
    return answer

def isPalindrome(number):
    if number == reverse_1(number):
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
    count = 0
    for x in range(ord(ch1) + 1, ord(ch2)):
        print(chr(x), end="\n" if count == numberPerLine else " ")
        count += 1
        count %= 5


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
    meters = 0.305 * foot
    return meters

def meterToFoot(meters):
    feet = meters / 0.305
    return feet

def foot_and_meters_table():
    print("{:<10} {:<10} | {:>10} {:>10}".format("Feet", "Meters", "Meters", "Feet"))
    for x in range(10):
        feet = x + 1
        meters = footToMeter(feet)
        meters2 = 20 + x * 6
        feet2 = round(meterToFoot(meters2), 3)
        print("{:<10} {:<10} | {:>10} {:>10}".format(feet, meters, meters2, feet2))


"""
Provide the isPrime(number) function for testing whether a number is prime. Use this function to find the number of 
prime numbers less than 10,000.
"""
def isPrime(number):
    for x in range(2, number):
        if number % x == 0:
            return False
    return True

def all_primes():
    count = 0
    for i in range(2, 10000):
        if isPrime(i) == True:
            count += 1
    return count


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
    m = 0
    for x in range(1, i + 1):
        m += x / (x + 1)
    return round(m, 4)

def table_sum_series():
    print("{:<10} {:<10}".format("i", "m(i)"))
    for i in range(1, 21):
        print("{:<10} {:<10}".format(i, m(i)))


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
def m2(i):
    m = 0
    positive = True
    for x in range(1, i + 1, 2):
        # print("+" if positive else "-", 1, '/', x)
        if positive:
            m += 1 / x
        else:
            m -= 1 / x
        positive = not positive
    return round((m * 4), 4)

def table_m2():
    print("{:<10} {:<10}".format("i", "m(i)"))
    for x in range(1, 902, 100):
        print("{:<10} {:<10}".format(x, m2(x)))


"""
(Financial application: print a tax table) gives a program to compute tax. Write a function 
for computing tax using the following header:
def computeTax(status, taxableIncome):
Use this function to write a program that prints a tax table for taxable income from $50,000 to $60,000 with intervals 
of $50 for all four statuses, as follows:

Taxable Income          Single      Married Joint        Married Separated           Head of House
     
50000                   8688        6665                 8688                        7352
50050                   8700        6673                 8700                        7365
...
59950                   11175       8158                 11175                       9840
60000                   11188       8165                 11188                       9852

"""
def computeTax(status, taxableIncome):
    pass


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
def sqrt(n):
"""
def sqrt(n):
    difference = float("inf")
    guess = 0.5 * n
    while difference > 0.0001:
        nextGuess = (guess + (n / guess)) / 2
        difference = abs(nextGuess - guess)
        guess = nextGuess
    return nextGuess



"""
(Convert milliseconds to hours, minutes, and seconds) Write a function that converts milliseconds to hours, minutes, 
and seconds using the following header:
def convertMillis(millis):

The function returns a string as hours:minutes:seconds. For example, convertMillis(5500) returns the string 0:0:5, 
convertMillis(100000) returns the string 0:1:40, and convertMillis(555550000) returns the string 154:19:10.
Write a test program that prompts the user to enter a value for milliseconds and displays a string in the format of 
hours:minutes:seconds.
"""
def convertMillis(millis):
    total_seconds = millis / 1000
    mins = total_seconds // 60
    seconds = total_seconds % 60
    hours = mins // 60
    mins = mins % 60
    return hours, mins, seconds


"""
A palindromic prime is a prime number that is also palindromic. For example, 131 is a prime and also a palindromic 
prime, as are 313 and 757. Write a program that displays the first 100 palindromic prime numbers. Display 10 numbers 
per line and align the numbers properly, as follows:

 2     3     5     7    11    101    131   151   181   191
313   353   373   383   727   757    787   797   919   929
"""
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def is_palindrome(num):
    string = str(num)
    lst1 = [ch for ch in string]
    lst2 = lst1[:]
    lst1.reverse()
    if lst2 == lst1:
        return True
    else:
        return False


def primes(num):
    primes= []
    for x in range(2, num):
        if is_prime(x) and is_palindrome(x):
            primes.append(x)
    return primes


"""
An emirp ( prime spelled backward) is a non-palindromic prime number whose reversal is also a prime. For example, both 
17 and 71 are prime numbers, so 17 and 71 are emirps. Write a program that displays the first 100 emirps. Display 10 
numbers per line and align the numbers properly, as follows:

 13   17   31   37   71   73   79   97  107  113
149  157  167  179  199  311  337  347  359  389
"""

def reverse_2(num):
    string = str(num)
    lst = [ch for ch in string]
    lst.reverse()
    string2 = "".join(lst)
    num2 = int(string2)
    return num2


def primes2(num):
    primes_nums = []
    for x in range(2, num):
        if is_prime(x) and not is_palindrome(x) and is_prime(reverse_2(x)):
            primes_nums.append(x)
    return primes_nums



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
def mersenne_prime():
    print("{:<10} {:>10}".format("p", "2^p - 1"))
    for p in range(2, 32):
        if is_prime(2 ** p - 1):
            print("{:<10} {:>10}".format(p, (2 ** p - 1)))


"""
(Twin primes) Twin primes are a pair of prime numbers that differ by 2. For example, 3 and 5, 5 and 7, and 11 and 13 
are twin primes. Write a program to find all twin primes less than 1,000. Display the output as follows:
 (3, 5)
 (5, 7)
 ...
"""
def twin_primes():
    for x in range(3, 999):
        if is_prime(x) and is_prime(x + 2):
            print("(" + str(x) + ", " + str(x + 2) + ")")


"""
(Game: craps) Craps is a popular dice game played in casinos. Write a program to play a variation of the game, as 
follows:
Roll two dice. Each die has six faces representing values 1, 2, ..., and 6, respectively. Check the sum of the two 
dice. If the sum is 2, 3, or 12 (called craps), you lose; if the sum is 7 or 11 (called natural), you win; if the sum 
is another value (i.e., 4, 5, 6, 8, 9, or 10), a point is established. Continue to roll the dice until either a 7 or the 
same point value is rolled. If 7 is rolled, you lose. Otherwise, you win.
Your program acts as a single player. Here are some sample runs:

Sample Run 1:
You rolled 5 + 6 = 11
You win

Sample Run 2: 
You rolled 1 + 2 = 3
You lose

Sample Run 3:
You rolled 4 + 4 = 8
point is 8
You rolled 6 + 2 = 8
You win

Sample Run 4:
You rolled 3 + 2 = 5
point is 5
You rolled 2 + 5 = 7
You lose
"""
def dice_game():
    num1 = random.randint(1, 6)
    num2 = random.randint(1, 6)
    dice_sum = num1 + num2
    print("You rolled", num1, "+", num2, "=", dice_sum)
    if dice_sum in [7, 11]:
        print("You win")
    elif dice_sum in [2, 3, 12]:
        print("You lose")
    else:
        print("point is", dice_sum)
        dice_sum2 = 0
        while dice_sum2 not in [dice_sum, 7]:
            num1 = random.randint(1, 6)
            num2 = random.randint(1, 6)
            dice_sum2 = num1 + num2
        print("You rolled", num1, "+", num2, "=", dice_sum2)
        if dice_sum2 == 7:
            print("You lose")
        else:
            print("You win")


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2 * math.pi * self.radius

