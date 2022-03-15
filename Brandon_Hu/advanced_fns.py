"""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, 3 , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal numbers with 10 numbers on each line.
"""
def getPentagonalNumber(n):
    num = n * (3 * n - 1) // 2
    return num

def getAllPentagonals():
    lst = []
    for n in range(1 , 101):
        pentagonal_num = getPentagonalNumber(n)
        lst.append(pentagonal_num)
    return lst


"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""

def sumDigits(n):
    total = 0
    while n > 0:
        units_digit = n % 10
        total = total + units_digit
        n = n // 10
    return total


"""
Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654
reverse(435) returns 534
def reverse(number):

# Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. 
Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.
"""
def reverse(number):
    rev_num = 0
    while number > 0:
        units = number % 10
        rev_num = rev_num * 10 + units
        number = number // 10
    return rev_num

def isPalindrome(number):
   if number == reverse(number):
        return True
   return False


"""
(Sort three numbers) Write the following function to display three numbers in increasing order:
def displaySortedNumbers(num1, num2, num3):
Write a test program that prompts the user to enter three numbers and invokes the function to display them in 
increasing order. 
Here are some sample runs:
Enter three numbers: 3, 2.4, 5
The sorted numbers are 2.4 3 5
Enter three numbers: 31, 12.4, 15
The sorted numbers are 12.4 15 31
"""
def displaySortedNumbers(num1, num2, num3):
    biggest = max(num1, num2, num3)
    smallest = min(num1, num2, num3)
    if num1 != biggest and num1 != smallest:
        middle = num1
    elif  num2 != biggest and num2 != smallest:
        middle = num2
    else:
        middle = num3
    return smallest, middle, biggest


"""
Financial application: compute the future investment value) Write a function that computes a future investment value at 
a given interest rate for a specified number of years. The future investment is determined using the formula:
        futureInvestmentValue = investmentAmount * (1 + monthlyInterestRate)^numberOfMonths
Use the following function header:
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
For example, futureInvestmentValue(10000, 0.05/12, 5) returns 12833.59.
Write a test program that prompts the user to enter the investment amount and the annual interest rate in percent and 
prints a table that displays the future value for the years from 1 to 30. Here is a sample run:
The amount invested: 1000
Annual interest rate: 9
Years           Future Value
1               1093.80
2               1196.41
... 
29              13467.25
30              14730.57
"""
def futureInvestmentValue(investmentAmount, monthlyInterestRate, years):
    return investmentAmount * (1 + monthlyInterestRate) ** (years * 12)

def future_value():
    investmentAmount = int(input("The amount invested:"))
    annual_interest_rate = int(input("annual intrest invested:"))
    monthlyInterestRate = annual_interest_rate / 1200
    for i in range(1, 31):
        print(i, futureInvestmentValue(investmentAmount, monthlyInterestRate, i))


"""
Provide the isPrime(number) function for testing whether a number is prime. Use this function to find the number of 
prime numbers less than 10,000.
"""
def isPrime(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def lessPrime():
    count = 0
    for i in range(2 ,10000):
        if isPrime(i):
            count += 1
    return count