"""
Problem Description
You might be surprised to know that 2013 is the first year since 1987 with distinct digits. The years 2014, 2015, 2016,
2017, 2018, 2019 each have distinct digits. 2012 does not have distinct digits, since the digit 2 is repeated.
Given a year, what is the next year with distinct digits?

Input Specification
The input consists of one integer Y (0 ≤ Y ≤ 10000), representing the starting year.

Output Specification
The output will be the single integer D, which is the next year after Y with distinct digits.

Sample Input 1
1987
Output for Sample Input 1
2013

Sample Input 2
999
Output for Sample Input 2
1023

Sample Input 3
879
Output for sample input 2
890
"""



def is_unique(year):
    year_str = str(year)
    for d in year_str:
        if year_str.count(d) > 1:
            return False
    return True


def distinct_date_finder():
    file = open("CCC_2013/J3", "r")
    year = int(file.readline())
    year += 1
    while not is_unique(year):
        year += 1
    print(year)