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
def sigma():
    n = int(input("Please enter a number:"))
    total = 0
    for number in range(1,n+1):
        total = total + number
    return total


