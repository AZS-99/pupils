"""
Problem Description
Barley the dog loves treats. At the end of the day he is either happy or sad depending on the number and size of treats
he receives throughout the day. The treats come in three sizes: small, medium, and large. His happiness score can be
measured using the following formula:
                                        1×S+2×M+3×L
where S is the number of small treats, M is the number of medium treats and L is the number of
large treats.
If Barley’s happiness score is 10 or greater than he is happy. Otherwise, he is sad. Determine whether Barley is happy
or sad at the end of the day.

Input Specification
There are three lines of input. Each line contains a non-negative integer less than 10. The first line contains the
number of small treats, S, the second line contains the number of medium treats, M, and the third line contains the
number of large treats, L, that Barley receives in a day.

Output Specification
If Barley’s happiness score is 10 or greater, output happy. Otherwise, output sad.
Sample Input 1
3
1
0
Output for Sample Input 1
sad

Explanation of Output for Sample Input 1
Barley’s happiness score is 1 × 3 + 2 × 1 + 3 × 0 = 5, so he will be sad.
Sample Input 2
3
2
1
Output for Sample Input 2
happy

Explanation of Output for Sample Input 2
Barley’s happiness score is 1 × 3 + 2 × 2 + 3 × 1 = 10, so he will be happy.
"""
def dog_feeling():
    file = open("CCC_2020/J1","r")
    small = int(file.readline())
    medium = int(file.readline())
    large = int(file.readline())
    feeling_rate = small + 2 * medium + 3 * large
    if feeling_rate > 9:
        print("happy")
    else:
        print("sad")
