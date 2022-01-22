def sigma(n):
    if n < 2:
        return 1
    else:
        return sigma(n - 1) + n


def factorial(n):
    if n == 1:
        return 1
    else:
        return factorial(n - 1) * n

def sum_digits(num):
    if num < 10:
        return num
    else:
        return sum_digits(num // 10) + num % 10


"""
    Return whether the number is divisible by 11
    As long as the number being tested has more than two digits, form a new number by:
    1- Deleting the units digit
    2- Subtracting the deleted digit from the shortened number
    3- The remaining number is divisible by 11 if and only if the original number is divisible by 11.
    :param num: int
    :return: bool
"""
def divisible_by_11(num):
    if num == 0 or num == 11:
        return True
    if num > 11:
        last_digit = num % 10
        num -= last_digit
        return divisible_by_11(num)