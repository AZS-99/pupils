"""
If the Roman Empire had not fallen, then Rome would surely have discovered electricity and used electronic calculators;
 however, the Romans used Roman Numerals! Your task is to implement a simple Roman Calculator which accepts two Roman
 Numerals and outputs the sum in Roman Numerals. You may assume that numbers greater than 1000 will not occur in the input.
 Output numbers greater than 1000 are illegal and should generate the message CONCORDIA CUM VERITATE (In Harmony with Truth).

The input consists of a number, indicating the number of test cases, followed by this many test cases. Each test case
consists of a single line with two numbers in Roman Numerals separated by a + along with an = at the end. There are no
separating spaces.

For each test case the output is a copy of the input with the Roman Numeral that represents the sum. Outputs for different
test cases are separated by a blank line.

Roman Research

The Roman Numerals used by the Romans evolved over many years, and so there are some variations in the way they are
written. We will use the following definitions:

The following symbols are used: I for 1, V for 5, X for 10, L for 50, C for 100, D for 500, and M for 1000.
Numbers are formed by writing symbols from 1. from left to right, as a sum, each time using the symbol for the largest
possible value. The symbols M, C, X, or I may be used at most three times in succession. Only if this rule would be
violated, you can use the following rule:
When a single I immediately precedes a V or X, it is subtracted. When a single X immediately precedes an L or C, it is
subtracted. When a single C immediately precedes a D or M, it is subtracted.
For example: II = 2; IX = 9; CXIII = 113; LIV = 54; XXXVIII = 38; XCIX = 99.
Sample input

3
VII+II=
XXIX+X=
M+I=
Sample output

VII+II=IX
XXIX+X=XXXIX
M+I=CONCORDIA CUM VERITATE
"""


def f(n):
    if n == 11:
        return True
    elif n < 11:
        return False
    else:
        return f(n//10 - n%10)


if __name__ == '__main__':
    with open("divisible_11") as file:
        lines = file.read().splitlines()

    lines_num = [int(x) for x in lines]
    lines_num = lines_num[1:]
    for x in lines_num:
        if f(x):
            print("The number " + str(x) + " is divisible by 11.")
        else:
            print("The number " + str(x) + " is not divisible by 11.")



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
