"""
Write a program which accepts as input a positive integer and checks, using the algorithm described below, to see
whether or not the integer is divisible by 11. This particular test for divisibility by 11 was given in 1897 by
Charles L. Dodgson (Lewis Carroll).

Algorithm:
As long as the number being tested has more than two digits, form a new number by:
deleting the units digit
subtracting the deleted digit from the shortened number
The remaining number is divisible by 11 if and only if the original number is divisible by 11.
Note:
Leading zeroes are not considered part of the number and should not be printed.
As usual, the first number in the input indicates the number of positive integers that follow. Each positive integer
has a maximum of 50 digits. You may assume no leading zeroes exist in the positive integers.

For each positive integer in the input, the output consists of a series of numbers formed as a digit is deleted and
subtracted, followed by a message indicating whether or not the original number is divisible by 11. Outputs for
different positive integers are separated by blank lines.

Sample input

1
12345678901234567900

Sample output

12345678901234567900
1234567890123456790
123456789012345679
12345678901234558
1234567890123447
123456789012337
12345678901226
1234567890116
123456789005
12345678995
1234567884
123456784
12345674
1234563
123453
12342
1232
121
11
The number 12345678901234567900 is divisible by 11.
"""
def is_divisible_original(n):
    is_true = isDivisibleBy11(n)
    if (is_true):
        print(f"Th number {n} is divisible by 11")
    else:
        print(f"The number {n} is not divisible by 11")
    return is_true

def isDivisibleBy11(n:int):
    if n == 11:
        return True
    elif len(str(n)) > 2:
        lastDigit = int(str(n)[-1])
        n = int(str(n)[0:-1]) - lastDigit
        print(n)
        return isDivisibleBy11(n)
    elif n < 11:
        return False

