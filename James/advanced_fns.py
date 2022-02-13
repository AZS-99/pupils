"""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
def getPentagonalNumber(num):
    pentagonal = num * ((3 * num) - 1 ) // 2
    return pentagonal

def printPentagonalNumber():
    num = 1
    for i in range (1, 10):
        for j in range (1, 10):
            print(getPentagonalNumber(num), end=" ")
            num += 1
        print()


"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""
def sumDigits(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10
    return sum(digits)


"""
Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):
# Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. 
Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.
"""
def reverse(num):
    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    answer = 0
    for i in range(0, len(digits)):
        answer *= 10
        answer += digits[i]
    return answer

def isPalindrome(num):
    return reverse(num) == num



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
    order = [num1, num2, num3]
    order.sort()
    return order



"""
Financial application: compute the future investment value) Write a function that computes a future investment value at 
a given interest rate for a specified number of years. The future investment is determined using the formula:
        futureInvestmentValue = investmentAmount x (1 + monthlyInterestRate)^numberOfMonths
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
    numberOfMonths = years * 12

    futureInvestmentValue = investmentAmount *(1 + monthlyInterestRate) ** numberOfMonths
    return round(futureInvestmentValue, 2)

def printInvestment(initialinvestmentAmount, monthlyInterestRate):
    print("{:<10} {:<10}".format("Years", "Future Value"))
    for i in range(1, 31):
        print("{:<10} {:<10}" .format(i ,futureInvestmentValue(initialinvestmentAmount,monthlyInterestRate, i)))