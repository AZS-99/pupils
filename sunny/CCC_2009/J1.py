"""
Problem J1: ISBN
Problem Description
The International Standard Book Number (ISBN) is a 13-digit code for identifying books. These numbers have a special
property for detecting whether the number was written correctly.
The 1-3-sum of a 13-digit number is calculated by multiplying the digits alternately by 1’s and 3’s (see example) and
then adding the results. For example, to compute the 1-3-sum of the number 9780921418948 we add
                        9∗1 + 7∗3 + 8∗1 + 0∗3 + 9∗1 + 2∗3 + 1∗1 + 4∗3 + 1∗1 + 8∗3 + 9∗1 + 4∗3 + 8∗1
to get 120.

The special property of an ISBN number is that its 1-3-sum is always a multiple of 10.
Write a program to compute the 1-3-sum of a 13-digit number. To reduce the amount of typing, you may assume that the
first ten digits will always be 9780921418, like the example above. Your program should input the last three digits and
then print its 1-3-sum. Use a format similar to the samples below.

Sample Interactive Session 1 (user input shown in italics)
Digit 11? 9
Digit 12? 4
Digit 13? 8

Output for Sample Interactive Session 1
The 1-3-sum is 120

Sample Interactive Session 2 (user input shown in italics)
Digit 11? 0
Digit 12? 5
Digit 13? 2

Output for Sample Interactive Session 2
The 1-3-sum is 108
"""
def sample_session():

    digit_11 = int(input("Digit 11?"))
    digit_12 = int(input("Digit 12?"))
    digit_13 = int(input("Digit 13?"))
    digit_formula11 = digit_11 * 1
    digit_formula12 = digit_12 * 3
    digit_formula13 = digit_13
    first_part = 9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3
    return first_part + digit_formula11 + digit_formula12 + digit_formula13