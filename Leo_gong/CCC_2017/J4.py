"""
Problem J4: Favourite Times
Time limit: 1 second

Problem Description
Wendy has an LED clock radio, which is a 12-hour clock, displaying times from 12:00 to 11:59. The hours do not have
leading zeros but minutes may have leading zeros, such as 2:07 or 11:03.
When looking at her LED clock radio, Wendy likes to spot arithmetic sequences in the digits. For example, the times
12:34 and 2:46 are some of her favourite times, since the digits form an arithmetic sequence.
A sequence of digits is an arithmetic sequence if each digit after the first digit is obtained by adding a constant
common difference. For example, 1,2,3,4 is an arithmetic sequence with a common difference of 1, and 2,4,6 is an
arithmetic sequence with a common difference of 2.
Suppose that we start looking at the clock at noon (that is, when it reads 12:00) and watch the clock for some number of
minutes. How many instances are there such that the time displayed on the clock has the property that the digits form an
arithmetic sequence?

Input Specification
The input contains one integer D (0 ≤ D ≤ 1 000 000 000), which represents the duration that the clock is observed.
For 4 of the 15 available marks, D ≤ 10 000.

Output Specification
Output the number of times that the clock displays a time where the digits form an arithmetic sequence starting from
noon (12:00) and ending after D minutes have passed, possibly including the ending time.

Sample Input 1
34
Output for Sample Input 1
1
Explanation of Output for Sample Input 1
Between 12:00 and 12:34, there is only the time 12:34 for which the digits form an arithmetic sequence.

Sample Input 2
180
Output for Sample Input 2
11
"""
def check(hours, mins):
    if mins < 10:
        time = str(hours) + str(0) + str(mins)
    else:
        time = str(hours) + str(mins)

    for i in range(len(time) - 2):
        if int(time[i]) - int(time[i + 1]) != int(time[i + 1]) - int(time[i + 2]):
            return False
    return True


def favourite_time():
    file = open("CCC_2017/J4", "r")
    time = int(file.readline())
    hour = 11
    hours = 0
    count = 0
    for t in range(time + 1):
        mins = t % 60
        if mins % 60 == 0:
            hour += 1
            hours = hour % 12
        if hours == 0:
            hours = 12

        if check(hours, mins):
            count += 1
    print(count)





# def checking(time):
#     lst = [x for x in str(time)]
#     difference = int(lst[1]) - int(lst[0])
#     for i in range(len(lst)):
#         if abs(int(lst[i]) - int(lst[i + 1])) != difference:
#             return False
#     return True
#
#
#
# def favourite_time():
#     file = open("CCC_2017/J4", "r")
#     time = int(file.readline())
#     count = 0
#     if time <= 1259:
#         for i in range(1200, time):
#             if checking(i):
#                 count += 1
#     if time < 1200:
#         for i in range(1200, 1259):
#             if checking(i):
#                 count += 1
#
#         for i in range(0, time):
#             if checking(i):
#                 count += 1
#     print(count)