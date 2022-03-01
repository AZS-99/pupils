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
"""
def reverse(number):
    rev_num = 0
    while number > 0:
        units = number % 10
        rev_num = rev_num * 10 + units
        number = number // 10
    return rev_num

