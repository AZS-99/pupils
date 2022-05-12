
"""
Write a programme that prompts the user to enter an integer, then returns true if that integer is even, false otherwise.

Sample Run 1:
Enter an integer: 6

Sample Output 1:
6 is an even number

Sample Run 2:
Enter an integer: 7

Sample Output2:
7 is not an even number
"""
def integers(n):
    if n % 2 == 0:
        return str(n) + " is an even number "
    else:
        return str(n) + " is not an even number "


"""
Write a programme that prompts the user to enter a year, then returns true if it is a leap year, false otherwise.
"""
def leap_year(n):
    if n % 4 == 0:
        return True
    else:
        return False




"""
Write a function that displays all the leap years since 1900 till this year 2022
"""
def leap_years():
    for year in range (1900,2023):
        if year % 4 == 0:
            print (year)


"""
Write a programme the prompts the user to enter two integers, the second of which is a prime number, then returns true
if the prime number provided is a factor of the first integer

Sample Run:
Enter an integer: 8
Enter a prime number: 2

Sample output:
2 is a factor of 8


Sample Run:
Enter an integer: 9
Enter a prime number: 5

Sample output
5 is not a factor of 9
"""
    
def prime_numbers():
    integer = int(input("Please enter an integer:"))
    prime = int(input("Please enter prime number"))
    if integer % prime == 0:
        return prime, True
    else:
        return prime, False
