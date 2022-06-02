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
Write a function that displays all the leap years since 1901 till this year 2022
"""
def leap_year():
    for year in range(1901, 2023):
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


"""
Print the following pattern using loops:
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
"""
def patterns():
    for j in range(2, 7):

        for i in range(1, j):
            print(i)


"""
Write a program to use for loop to print the following reverse number pattern
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
"""
def pattern():
    for j in range (5, 0, -1):
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
def reverse_patterns():
    for j in range(2, 7):
        for i in range(1, j):
            print(i, end=" ")
        print()

    for j in range(4,0, -1):
        for i in range(j, 0, -1):
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
def print_loops():
    for i in range (1, 11):
        print(i, end=" ")
    print()
    for i in range ( 2, 12):
        print(i, end=" ")
    print()
    for i in range (3, 13):
        print(i, end=" ")
    print()
    for i in range (4, 14):
        print(i, end=" ")
    print()
    for i in range (5, 15):
        print(i, end=" ")
    print()

