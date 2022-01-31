"""
(Math: pentagonal numbers) A pentagonal number is defined as n(3n - 1)/2 for n = 1, 2, c , and so on. So, the first few
numbers are 1, 5, 12, 22, .... Write a function with the following header that returns a pentagonal number:
def getPentagonalNumber(n):
Write a test program that uses this function to display the first 100 pentagonal
numbers with 10 numbers on each line.
"""
def pentagonal_number(n):
    return n * (3 * n - 1) // 2

def pentagonal_numbers():
    count = 0
    for n in range(1, 101):
        pen_num = pentagonal_number(n)
        count += 1
        count %= 10
        print(pen_num, ", ", end="\n" if count == 0 else "")


"""
(Sum the digits in an integer) Write a function that computes the sum of the digits in an integer. Use the following 
function header: def sumDigits(n):
For example, sumDigits(234) returns 9. 
"""
def sumDigits(n):
    total = 0
    while n != 0:
        total += n % 10
        n //= 10
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
    answer = 0
    while number != 0:
        answer = answer * 10 + number % 10
        number //= 10
    return answer

def isPalindrome(number):
    if number == reverse(number):
        print("It is palindrome")
    else:
        print("It is not palindrome")