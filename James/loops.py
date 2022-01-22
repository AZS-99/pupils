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
def primefactoring(num):
    factor = 1

def prime(input):
    isPrime = True
    argsqrt = math.sqrt(input)
    currentfactor = math.floor(argsqrt)
    while currentfactor > 1:
        if input % currentfactor == 0:
            isPrime = False
        argsqrt -= 1
    return isPrime