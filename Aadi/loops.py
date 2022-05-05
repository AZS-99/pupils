"""
Write a for loop that prints all the numbers between 1 and 15 inclusive.
"""
def numbers():
    for i in range(1, 15):
        print(i)


"""
Write a function that prints the squares of all integers between 1 to 50 exclusive. 
"""
def squares():
    for i in range(2,50):
        print(i**2)


"""
Write a programme that prompts the user to enter an integer, then prints the cubes of all numbers between 1 and the
specified number inclusive. 
"""

def cubes(value):
    for i in range (1,value+1):
        print(i**3)


"""
Write a function that displays all the leap years since 1900 till this year 2022
"""
def leap_year():
    for year in range(1900, 2023):
        if year % 4 == 0:
            print(year)


"""
Using a loop, write a programme that displays the result of 1 + 2 + 3 + 4 + ... + 99 + 100.
"""
def addition():
    total = 0
    for number in range(1,101):
        total = total + number
    return total


"""
Write a programme that prompts the user to enter an integer n, then displays the result of 1 + 2 + 3 + ... + n
"""



"""
Write a programme that prompts the user to enter an integer n, the displays the result of 1^2 + 2^2 + 3^2 + ... + n^2
"""
def powers():
    n = int(input("PLease input a number:"))
    total = 0
    for number in range(1, n + 1):
        total = total + number ** 2
    return total


"""
Assume python doesn't have the "to the power of" feature, that is, the double asterisk used for that purpose. Create a
function named "power" that takes two arguments, the base and the exponent, and returns the result. 
"""
def power(base, exponent):
    total = 1
    for i in range(exponent):
        total = total * base
    return total


"""
Write a function that takes an integer n as an argument, and returns its factorial.
"""
def factorial(n):
    total = 1
    for i in range(2, n+1):
        total = total * i
    return total


"""
Write a function that takes an integer n as an argument, and returns its units digit.
"""
def get_units_digit(n):
    return n % 10


"""
Write a function that takes an integer n as an argument, and returns the number of digits of that number
"""
def count_digits(n):
    total = 0
    while n > 0:
        n = n // 10
        total += 1
    return total





