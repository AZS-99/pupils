"""
Problem Description
Barbara plants N different sunflowers, each with a unique height, ordered from smallest to largest, and records their
heights for N consecutive days. Each day, all of her flowers grow taller than they were the day before.
She records each of these measurements in a table, with one row for each plant, with the first row recording the
shortest sunflower’s growth and the last row recording the tallest sunflower’s growth. The leftmost column is the first
measurement for each sunflower, and the rightmost column is the last measurement for each sunflower.

If a sunflower was smaller than another when initially planted, it remains smaller for every mea- surement.
Unfortunately, her children may have altered her measurements by rotating her table by a multiple of 90 degrees.
Your job is to help Barbara determine her original data.

Input Specification
The first line of input contains the number N (2 ≤ N ≤ 100). The next N lines each contain N positive integers, each of
which is at most 109. It is guaranteed that the input grid represents a rotated version of Barbara’s grid.

Output Specification
Output Barbara’s original data, consisting of N lines, each of which contain N positive integers.
Sample Input 1
2
1 3
2 9
Output for Sample Input 1
1 3
2 9

Explanation of Output for Sample Input 1
The data has been rotated a multiple of 360 degrees, meaning that the input arrangement is the original arrangement.

Sample Input 2
3
4 3 1
6 5 2
9 7 3
Output for Sample Input 2
1 2 3
3 5 7
4 6 9

Explanation of Output for Sample Input 2
The original data was rotated 90 degrees to the right/clockwise.

Sample Input 3
3
3 7 9
2 5 6
1 3 4
Output for Sample Input 3
1 2 3
3 5 7
4 6 9

Explanation of Output for Sample Input 3
The original data was rotated 90 degrees to the left/counter-clockwise.
"""
def checking(lst):
    num_line = len(lst)
    for i in range(num_line):
        if not lst[i][0] < lst[i][1] < lst[i][2]:
            return False

    for i in range(num_line):
        if not lst[0][i] < lst[1][i] < lst[2][i]:
            return False
    return True

def rotate(lst):
    length = len(lst)
    for r in range(length):
        for c in range(length):
            lst[r][c], lst[c][length - 1 - r] = lst[c][length - 1 - r], lst[r][c]

    return lst



def sunflower():
    file = open("CCC_2018/J4", "r")
    num_line = int(file.readline())
    lst_of_lsts = []
    for i in range(num_line):
        line = [int(x) for x in file.readline().split(" ")]
        lst_of_lsts.append(line)

    for i in range(3):
        if checking(lst_of_lsts) == False:
            lst_of_lsts = rotate(lst_of_lsts)
        else:
            print(lst_of_lsts)

    print(lst_of_lsts)

