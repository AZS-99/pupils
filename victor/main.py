# This is a sample Python script.
from Fraction import Circle


def fibonacci(n):
    if n < 3:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

"""
    Return whether the number is divisible by 11
    As long as the number being tested has more than two digits, form a new number by:
    1- Deleting the units digit
    2- Subtracting the deleted digit from the shortened number
    3- The remaining number is divisible by 11 if and only if the original number is divisible by 11.
    :param num: int
    :return: bool
"""
def div_by_11(n):
    if n == 0 or n == 11:
        return True
    if n < 11:
        return False
    return div_by_11(n//10 - n % 10)





if __name__ == '__main__':
    c = Circle(3)
    print(c.area())
    print(c.circumference())
