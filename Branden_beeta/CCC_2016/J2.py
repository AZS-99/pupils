"""
Problem J2: Magic Squares

Problem Description
Magic Squares are square arrays of numbers that have the interesting property that the numbers in each column, and in
each row, all add up to the same total.
Given a 4 × 4 square of numbers, determine if it is magic square. Input Specification
The input consists of four lines, each line having 4 space-separated integers.
Output Specification
Output either magic if the input is a magic square, or not magic if the input is not a magic square.

Sample Input 1
16 3 2 13
5 10 11 8
9 6 7 12
4 15 14 1
Output for Sample Input 1
magic

Explanation for Output for Sample Input 1
Notice that each row adds up to 34, and each column also adds up to 34.

Sample Input 2
5 10 1 3
10 4 2 3
1 2 8 5
3 3 5 0
Output for Sample Input 2
not magic

Explanation for Output for Sample Input 2
Notice that the top row adds up to 19, but the rightmost column adds up to 11.
"""
def magic_square():

    file = open("CCC_2016/J2", "r")
    num1, num2, num3, num4 = [int(i) for i in file.readline().split(" ")]
    num5, num6, num7, num8 = [int(q) for q in file.readline().split(" ")]
    num9, num10, num11, num12 = [int(a) for a in file.readline().split(" ")]
    num13, num14, num15, num16 = [int(s) for s in file.readline().split(" ")]
    sum_of_magic = num1 + num2 + num3 + num4
    if sum_of_magic == num5 + num6 + num7 + num8:
        if sum_of_magic == num9 + num10 + num11 + num12:
            if sum_of_magic == num13 + num14 + num15 + num16:
                if sum_of_magic == num1 + num5 + num9 + num13:
                    if sum_of_magic == num2 + num6 + num10 + num14:
                        if sum_of_magic == num3 + num7 + num11 + num15:
                            if sum_of_magic == num4 + num8 + num12 + num16:
                                print("magic")
                            else:
                                print("not magic")
                        else:
                            print("not magic")
                    else:
                        print("not magic")
                else:
                    print("not magic")
            else:
                print("not magic")
        else:
            print("not magic")
    else:
        print("not magic")
