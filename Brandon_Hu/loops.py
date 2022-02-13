"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.8
"""
import math


def kilo_pound():
    print("{:<10} {:<10}".format("kilogram", "pounds"))
    for i in range(1, 200, 2):
        pound = round(i * 2.2,1)
        print("{:<10} {:<10}".format(i, pound))



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
def kilo_miles():
    print("{:<15} {:<15} |   {:<15} {:<15}".format("Miles","Kilometers","Kilometers","Miles"))
    for i in range(1,11):
        kilos1 = round(i * 1.6, 2)
        kilos2 = i * 5 + 15
        miles2 = kilos2 * 0.621
        print("{:<15} {:<15} |   {:<15} {:<15}".format(i, kilos1, kilos2, miles2))


"""
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that 
computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
"""
def tuition():
    piggy_bank = 10000
    for i in range(9):
        piggy_bank = piggy_bank * 1.05
    total = piggy_bank
    for i in range(3):
        piggy_bank = piggy_bank * 1.05
        total = round(total + piggy_bank,2)
    return total


"""
(Find the smallest n such that n^2 > 12,000) Use a while loop to find the smallest integer n such that n^2 is greater 
than 12,000.
"""
def smallest():
    n = 2
    while n ** 2 < 12000:
        n = n + 1
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

def primes(num):
    primelst = []
    for i in range(2, num):
        if is_prime(i):
            primelst.append(i)
    return primelst

def factors(num):
    prime_lst = primes(num)
    factors = []
    for prime in prime_lst:
        while num % prime == 0:
            factors.append(prime)
            num //= prime
    return factors


"""
Write a program to sum the following series and find the EXACT value:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99
"""
class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __add__(self, other):










