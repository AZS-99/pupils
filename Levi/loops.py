import math
import sys
sys.setrecursionlimit(150000)
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

def interest(balance):
    for i in range(1, 6):
        balance += 100
        balance *= (1 + 0.05/12)
    return balance


"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.8
"""

def table():
    print("{:<10} {:<7}".format("Kilograms", "Pounds"))
    for i in range(1, 200, 2):
        kilograms = i
        pounds = round(kilograms * 2.2, 2)
        print("{:<10} {:<7}".format(kilograms, pounds))


"""
Write a program that displays the following two tables side by side (note that 1 mile is 1.609 kilometers and that 
1 kilometer is 0.621 mile):

Miles         Kilometers   |   Kilometers   Miles     
1             1.609        |   20           12.42     
2             3.218        |   25           15.525    
3             4.827        |   30           18.63     
4             6.436        |   35           21.735    
5             8.045        |   40           24.84     
6             9.654        |   45           27.945    
7             11.263       |   50           31.05     
8             12.872       |   55           34.155    
9             14.481       |   60           37.26     
10            16.09        |   65           40.365   
"""

def tables():
    print("{:<15} {:<15} | {:<15} {:<15}".format("Miles", "Kilometers", "Kilometers", "Miles"))
    for i in range(1, 11):
        miles = i
        kilometers = miles * 1.609
        kilometers_2 = i * 5 + 15
        miles_2 = kilometers_2 * 0.621
        print("{:<15} {:<15} | {:<15} {:<15}".format(miles, kilometers, kilometers_2, miles_2))


"""
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that 
computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
"""

def university():
    tuition = 10000
    tuition_10 = 0
    for i in range(9):
        tuition_10 = tuition * 1.05
    total_cost = tuition_10
    for i in range(3):
        tuition_10 *= 1.05
        total_cost += tuition_10
    return total_cost


"""
Use a while loop to find the smallest integer n such that n^2 is greater
than 12,000.
"""

def n_squared():
    n = 0
    while n**2 < 12000:
        n += 1
    return n


"""
Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, 
if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5
"""

def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_primes(num):
    prime_numbers = []
    for i in range(2, num):
        if is_prime(i) == True:
            prime_numbers.append(i)
    return prime_numbers


def prime_factors(integer):
    primes = find_primes(integer)
    factors = []
    for prime in primes:
        while integer % prime == 0:
            integer //= prime
            factors.append(prime)
    return factors


"""


"""

def big_number(numbers):
    m = max(numbers)
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == m:
            count += 1
    return m, count


"""
Write a program to sum the following series and find the EXACT value:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99
"""

class Fraction:

    def __init__(self, numerator, denominator):
        x = math.gcd(numerator, denominator)
        self.numerator = numerator // x
        self.denominator = denominator // x

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    def __add__(self, other):
        y = math.lcm(self.denominator, other.denominator)
        a = (y // self.denominator) * self.numerator
        b = (y // other.denominator) * other.numerator
        return Fraction(a + b, y)

    def __iadd__(self, other):
        return self + other


def add_fractions():
    total = Fraction(0, 1)
    for i in range(1, 97, 2):
        total += Fraction(i, i+2)
    return total


"""
You can approximate e by using the following series
e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000, . . ., and 100000.
"""
def f(i):
    if i < 2:
        return i
    return f(i - 1) * i

def factorial(i):
    total_1 = Fraction(1, 1)
    for a in range(1, i + 1):
        total_1 += Fraction(1, f(i))
    return total_1

def factorial_2():
    for b in range(10000, 10001, 10000):
        print(factorial(b))


"""
Write a program that computes the following summation:
1 / (√1 + √2)  +  1 / (√2 + √3)  +  1 / (√3 + √4)  + .... +  1 / (√624 + √625)
"""

def square_root():
    e = 0
    for i in range(1, 625):
        e += 1 / (math.sqrt(i) + math.sqrt(i + 1))
    return round(e, 1)


"""
Write a program that displays all possible combinations for picking two numbers from integers 1 to 7. Also display the 
total number of combinations.
Sample Output:
1 2
1 3
1 4
1 5
1 6
1 7
2 3
2 4
...
...
5 6
5 7
6 7
The total number of all combinations is 21
"""

def combinations():
    for i in range(1, 7):
        for j in range(2, 8):
            print(i, j)
