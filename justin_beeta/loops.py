import math

"""
Print the following pattern:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
def pattern():
    for j in range(2, 7):
        for i in range(1, j):
            print(i, end=" ")
        print()


"""
Write a program to use for loop to print the following reverse number pattern

5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
def reverse_number():
    for j in range(5, 0, -1):
        for i in range(j, 0, -1):
            print(i, end=" ")
        print()


"""
Write a program to use for loop to print the following reverse number pattern

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
"""
def harder_reverse_question():
    for j in range(2, 7):
        for i in range(1, j):
            print(i, end=" ")
        print()
    for j in range(5, 1, -1):
        for i in range(1, j):
            print(i, end=" ")
        print()


"""
Find the loop the prints the following pattern:
1 2 3 4 5 6 7 8 9 10
2 3 4 5 6 7 8 9 10 11
3 4 5 6 7 8 9 10 11 12
4 5 6 7 8 9 10 11 12 13
5 6 7 8 9 10 11 12 13 14
"""
def find_the_loops():
    for j in range(1, 6):
        for i in range(j, j + 10):
            print(i, end=" ")
        print()







"""
Write a program to display all prime numbers within a range. For instance:
Prime numbers between 25 and 50 are:
29
31
37
41
43
47
"""
def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def find_prime_numbers(num1, num2):
    for i in range(num1 + 1, num2):
        if is_prime(i):
            print(i)


"""
Write a program to use the loop to find the factorial of a given number.

The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

For example: calculate the factorial of 5

5! = 5 × 4 × 3 × 2 × 1 = 120
"""
def factorial(num):
    total = 1
    for i in range(1, num + 1):
        total *= i
    return total





"""
Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number
For example, if the user entered 10 the output should be 55 ( because 1+2+3+4+5+6+7+8+9+10 = 55)
"""
def calculate_the_sum(num):
    total = 0
    for i in range(1, num + 1):
        total += i
    return total


"""
Calculate the cube of all numbers from 1 to a given number

Write a program to print the cube of all numbers from 1 to a given number

Given:

input_number = 6

Expected output:

Current Number is : 1  and the cube is 1
Current Number is : 2  and the cube is 8
Current Number is : 3  and the cube is 27
Current Number is : 4  and the cube is 64
Current Number is : 5  and the cube is 125
Current Number is : 6  and the cube is 216
"""
def cube(num):
    for i in range(1, num + 1):
        print("Current Number is:", i, "and the cube is", i ** 3)

















def power(base, exponent):
    total = 1
    for i in range(exponent):
        total = total * base
    print(total)


def factorial(n):
    total = 1
    for i in range(2, n + 1):
        total = total * i
    return total


"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.8
"""
def kilograms_to_pounds():
    print("{:<10} {:<10}".format("Kilograms", "Pounds"))
    for kilo in range(1, 200, 2):
        pound = round(kilo * 2.2, 2)
        print("{:<10} {:<10}".format(kilo, pound))

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
def miles_to_kilometers():
    print("{:<10} {:<10}   |   {:<10} {:<10}".format("Miles", "Kilometers", "Kilometers", "Miles"))
    for miles in range(1, 11):
        kilometers1 = round(miles * 1.609, 3)
        kilometers2 = 5 * miles + 15
        miles2 = kilometers2 * 0.621
        print("{:<10} {:<10}   |   {:<10} {:<10}".format(miles, kilometers1, kilometers2, miles2))



"""
(Find the smallest n such that n^2 > 12,000) Use a while loop to find the smallest integer n such that n^2 is greater 
than 12,000.
"""
def smallest_n():
    n = 1
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

def prime_lst(num):
    lst = []
    for i in range(2, num):
        if is_prime(i):
            lst.append(i)
    return lst

def factors(num):
    lst = prime_lst(num)
    factors_lst = []
    for prime in lst:
        while num % prime == 0:
            factors_lst.append(prime)
            num = num // prime
    return factors_lst

"""
Write a program to sum the following series and find the EXACT value:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99

"""
def sum():
    total = 0
    for i in range(1, 98, 2):
        total = total + (i / (i + 2))
    return round(total, 2)


"""
Write a program that computes the following summation:
1 / (√1 + √2)   +   1 / (√2 + √3)   +   1 / (√3 + √4)   + .... +   1 / (√624 + √625)
"""
def summation():
    total = 0
    for i in range(1, 625):
        total = total + 1 / (math.sqrt(i) + math.sqrt(i + 1))
    return round(total, 2)


"""
You can approximate e by using the following series
e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000, . . ., and 100000.
"""







