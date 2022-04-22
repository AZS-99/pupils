"""
Problem J1: Occupy parking Problem Description
You supervise a small parking lot which has N parking spaces.
Yesterday, you recorded which parking spaces were occupied by cars and which were empty. Today, you recorded the same
information.
How many of the parking spaces were occupied both yesterday and today?
Input Specification
The first line of input contains the integer N (1 ≤ N ≤ 100). The second and third lines of input contain N characters
each. The second line of input records the information about yesterday’s parking spaces, and the third line of input
records the information about today’s parking spaces. Each of these 2N characters will either be C to indicate an
occupied space or . to indicate it was an empty parking space.
Output Specification
Output the number of parking spaces which were occupied yesterday and today.

Sample Input 1
5
CC..C
.CC..
Output for Sample Input 1
1
Explanation of Output for Sample Input 1
Only the second parking space from the left was occupied yesterday and today.

Sample Input 2
7
CCCCCCC
C.C.C.C
Output for Sample Input 2
4
Explanation of Output for Sample Input 2
The first, third, fifth, and seventh parking spaces were occupied yesterday and today.
"""
def parking():
    file = open("CCC_2018/J1", "r")
    parking_spaces = file.readline()
    parking_spaces = int(parking_spaces)
    line1 = file.readline()
    line2 = file.readline()
    count = 0
    for i in range(parking_spaces):
        if line1[i] == line2[i] == 'C':
            count += 1
    return count



