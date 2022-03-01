
"""""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
def getPentagonalNumber(n):
    x = n*(3*n - 1)//2
    return x

def getPentagonalNumber2():
    num = 1
    for i in range(1, 10):
        for j in range(10):
            print(getPentagonalNumber(num), end=" ")
            num += 1
        print()



"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""
def sumDigits(n):
    total = 0
    while n > 0:
        units_digit = n % 10
        total += units_digit
        n = n // 10
    return total


"""
Write the functions with the following headers:
# Return the reversal of an integer, e.g. reverse(456) returns # 654
def reverse(number):
# Return true if number is a palindrome
def isPalindrome(number):
Use the reverse function to implement isPalindrome. A number is a palindrome if its reversal is the same as itself. 
Write a test program that prompts the user to enter an integer and reports whether the integer is a palindrome.
"""
def reverse(number):
    total = 0
    while number > 0:
        total *= 10
        y = number % 10
        total += y
        number //= 10
    return total

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
    numbers = [num1, num2, num3]
    minimum_number = min(numbers)
    maximum_number = max(numbers)
    middle_number =  any(n != minimum_number and n != maximum_number for n in numbers)
    return minimum_number, middle_number, maximum_number
