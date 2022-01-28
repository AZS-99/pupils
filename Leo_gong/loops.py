import math
"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.8
"""
def kg_p():
    print("{:<10}  {:<10}".format("Kilograms", "Pounds"))
    for i in range(1, 200, 2):
        pounds = round(i * 2.2, 1)
        print("{:<10}  {:<10}".format(i, pounds))



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
def table():
    print("{:<10}  {:<10}       |      {:<10}      {:<10}".format("Miles", "Kilometers", "Kilometers", "Miles"))
    for i in range(1, 11):
        kilometers1 = round(i * 1.609, 3)
        kilometers2 = 20 + (i -1) * 5
        miles_2 = round(kilometers2 * 0.621, 3)
        print("{:<10}  {:<10}       |      {:<10}      {:<10}".format(i, kilometers1, kilometers2, miles_2))



"""
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that 
computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
"""
def tuition():
    x = 10000
    m = 0
    for i in range(9):
        x = x * 1.05
    for z in range(4):
        m += x * 1.05
    return round(m, 2)

"""
(Find the smallest n such that n^2 > 12,000) Use a while loop to find the smallest integer n such that n^2 is greater 
than 12,000.
"""
def smallest():
    for x in range(1, 12000):
        if x ** 2 > 12000:
            return x


"""
Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, 
if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5
"""

def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def primes(num):
    prime = []
    for x in range(2, num):
        if is_prime(x):
            prime.append(x)
    return prime

def factors(num):
    factor_lst = []
    lst = primes(num)
    index = 0
    while num != 1:
        prime = lst[index]
        while num % prime == 0:
            num //= prime
            factor_lst.append(prime)
        index += 1
    return factor_lst

"""
Write a program to sum the following series:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99
"""
class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return str(self.numerator) + "/" + str(self.denominator)

    def __add__(self, other):
        lcm = math.lcm(self.denominator, other.denominator)
        numerator1 = self.numerator * (lcm // self.denominator)
        numerator2 = other.numerator * (lcm // other.denominator)
        new_numerator = numerator1 + numerator2
        return Fraction(new_numerator, lcm)

def add_fraction():
    z = Fraction(0, 1)
    for x in range(1, 98, 2):
        z += Fraction(x, (x + 2))
    return z


"""
You can approximate e by using the following series
e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000, . . ., and 100000.
"""
def factorial(x):
    total = 1
    for i in range(1, x):
        total *= i
    return total


def i():
    z = Fraction(1, 1)
    for x in range(1, 10000):
        z += Fraction(1, factorial(x))
    return z


"""
Write a program that computes the following summation:
1 / (√1 + √2) + 1 / (√2 + √3) + 1 / (√3 + √4) + .... + 1 / (√624 + √625)
"""
def root():
    s = 0
    for x in range(1, 625):
        s += 1 / (math.sqrt(x) + math.sqrt(x + 1))
    return round(s, 2)


"""
Write a program that reads integers, finds the largest of them, and counts its occurrences. Assume that the input ends 
with number 0. Suppose that you entered 3 5 2 5 5 5 0; the program finds that the largest number is 5 and the 
occurrence count for 5 is 4. (Hint: Maintain two vari- ables, max and count. The variable max stores the current maximum 
number, and count stores its occurrences. Initially, assign the first number to max and 1 to count. Compare each 
subsequent number with max. If the number is greater than max, assign it to max and reset count to 1. If the number is 
equal to max, incre- ment count by 1.)

Enter a number (0: for end of input): 3
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 2
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 0
The largest number is 5
The occurrence count of the largest number is 4
"""
def largest_number():
    x = None
    lst = []
    while x != 0:
        x = int(input("Enter a number (0: for end of input): "))
        lst.append(x)
    largest = max(lst)
    occurrences = lst.count(largest)
    return largest, occurrences



"""
Write a program that displays all possible combinations for picking two numbers from integers 1 to 7. Also display the 
total number of combinations.

Sample Output:
1 2
1 3
...
...
6 7
The total number of all combinations is 21
"""
def combinations(x):
    total_number = 0
    for s in range(x):
        total_number += (x - 1)
    return total_number / 2