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


def table():

    pound = 0
    print("{:<10} {:<10}".format("Kilograms", "Pounds" ))
    for kilo in range(1, 199, 2):
        pound = round(kilo * 2.2, 1)
        print("{:<10} {:<10}".format(kilo, pound))
        kilo += 2


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
def distable():
    # miles = 1
    km1 = 0

    print("{:<10} {:<10} | {:<15} {:<15}".format("Miles","Kilometers","Kilometers", "Miles" ))
    for miles in range(1, 11, 1):
        km1 = miles * 1.609
        km2 = 20 + (miles - 1) * 5
        miles2 = km2 * 0.621
        print("{:<10} {:<10} | {:<15} {:<15}".format(miles,round(km1, 1), km2, round(miles2, 1)))


"""
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that 
computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
"""
def tuition():
    currenttuition = 10000
    for years in range(1, 10):
        currenttuition *= 1.05
    print(round(currenttuition, 2))
    total = currenttuition
    for years2 in range (1, 4):
        currenttuition *= 1.05
        total += currenttuition
    print(round(total, 2))


"""
Use a while loop to find the smallest integer n such that n^2 is greater 
than 12,000.
"""
def expo ():
    n = 1
    while n**2 < 12000:
        n +=1
    print(n)


"""
Write a program to sum the following series:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99
"""
def fracsum():
    total = 0
    for denom in range(3, 100, 2):
        numer = denom - 2
        total += (numer/denom)
    print(round(total, 3))


"""
Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, 
if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5
"""

def is_prime(input):
    argsqrt = math.sqrt(input)
    currentfactor = math.floor(argsqrt)
    while currentfactor > 1:
        if input % currentfactor == 0:
            return False
        currentfactor -= 1
    return True

def prime(max_factors):
    primes = []
    currentprime = 2
    while currentprime < max_factors:
        if is_prime(currentprime) == True:
            primes.append(currentprime)
        currentprime += 1
    return primes

def factors(num):
    primelist = prime(num)
    index = 0
    factorlist = []
    quotient = num
    while index < len(primelist):
        while quotient % primelist[index] == 0:
            factorlist.append(primelist[index])
            quotient //= primelist[index]
        index += 1
    return factorlist


"""
Write a program to sum the following series and find the EXACT value:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99
"""
class Fraction:
    def __init__(self, numerator, denominator):
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd

    def __str__(self):
        return "{0}/{1}".format(self.numerator, self.denominator)

    def __add__(self, other):
        new_denominator = math.lcm(self.denominator, other.denominator)
        numerator1 = self.numerator * (new_denominator // self.denominator)
        numerator2 = other.numerator * (new_denominator // other.denominator)
        new_numerator = numerator1 + numerator2
        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other):
        return self + other


"""
You can approximate e by using the following series
e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000, . . ., and 100000.
"""
def factorial(fac):
    if fac < 2:
        return fac
    else:
        return factorial(fac - 1) * fac


def facfrac(i):
    total = Fraction(1, 1)
    for k in range(1, i):

        frac1 = Fraction(1, factorial(k))
        total += frac1
    return total



"""
Write a program that computes the following summation:
1 / (√1 + √2) + 1 / (√2 + √3) + 1 / (√3 + √4) + .... + 1 / (√624 + √625)
"""
def sqrts():
    total = 0
    for i in range(1, 624, 1):
        total += 1 / (math.sqrt(i) + math.sqrt(i + 1))
    return total


"""
Write a program that reads integers, finds the largest of them, and counts its occurrences. Assume that the input ends 
with number 0. Suppose that you entered 3 5 2 5 5 5 0; the program finds that the largest number is 5 and the 
occurrence count for 5 is 4. (Hint: Maintain two vari- ables, max and count. The variable max stores the current maximum 
number, and count stores its occurrences. Initially, assign the first number to max and 1 to count. Compare each 
subsequent number with max. If the number is greater than max, assign it to max and reset count to 1. If the number is 
equal to max, increment count by 1.)
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
def maxcount():
    max = 0
    count = 0
    zeroentered = False
    while zeroentered == False:
        currentnumber = int(input("Enter a number (0: for end of input):"))
        if currentnumber == 0:
            zeroentered = True
        elif currentnumber == max:
            count += 1
        elif currentnumber > max:
            count = 1
            max = currentnumber

    return count,max


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
...
...
5 6
5 7
6 7
The total number of all combinations is 21
"""
def combos():
    for i in range(1, 7):
        for j in range(i + 1, 8):
            print(i, j)




