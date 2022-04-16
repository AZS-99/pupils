"""

Problem Description
In a sumac sequence, t1, t2, .., tm, each term is an integer greater than or equal 0. Also, each term, starting with the
third, is the difference of the preceding two terms (that is, tn+2 = tn − tn+1 for n ≥ 1). The sequence terminates at
tm if tm−1 < tm.

For example, if we have 120 and 71, then the sumac sequence generated is as follows:
                                        120, 71, 49, 22, 27.
This is a sumac sequence of length 5.

Input Specification
The input will be two positive numbers t1 and t2, with 0 < t2 < t1 < 10000.

Output Specification
The output will be the length of the sumac sequence given by the starting numbers t1 and t2.

Sample Input
120
71
Output for Sample Input
5
"""
def sumac_sequence():
    file = open("CCC_2011/J3", "r")
    a = int(file.readline())
    b = int(file.readline())
    count = 2
    while a - b > 0:
        num = a - b
        if num > 0:
            a = b
            b = num
            count += 1
    return count