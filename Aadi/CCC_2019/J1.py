"""
Problem Description
You record all of the scoring activity at a basketball game. Points are scored by a 3-point shot, a 2-point field goal,
or a 1-point free throw.
You know the number of each of these types of scoring for the two teams: the Apples and the Bananas. Your job is to
determine which team won, or if the game ended in a tie.

Input Specification
The first three lines of input describe the scoring of the Apples, and the next three lines of input describe the
scoring of the Bananas. For each team, the first line contains the number of successful 3-point shots, the second line
contains the number of successful 2-point field goals, and the third line contains the number of successful 1-point free
throws. Each number will be an integer between 0 and 100, inclusive.

Output Specification
The output will be a single character. If the Apples scored more points than the Bananas, output A. If the Bananas
scored more points than the Apples, output B. Otherwise, output T, to indicate a tie.

Sample Input 1
10
3
7
8
9
6
Output for Sample Input 1
B

Explanation of Output for Sample Input 1
The Apples scored 10·3 + 3·2 +7·1 = 43 points and the Bananas scored 8·3+9·2+6·1 = 48 points, and thus the Bananas won.

Input for Sample Input 2
7
3
0
6
4
1
Output for Sample Input 2
T

Explanation of Output for Sample Input 2
The Apples scored 7 · 3 + 3 · 2 + 0 · 1 = 27 points and the Bananas scored 6 · 3 + 4 · 2 + 1 · 1 = 27 points, and thus
it was a tie game.
"""
def basketball():
    file = open("CCC_2019/J1", "r")
    lst = []
    for i in range(2):
        three_points = int(file.readline())
        two_points = int(file.readline())
        one_point = int(file.readline())
        total = three_points * 3 + two_points * 2 + one_point
        lst.append(total)
    if lst[0] > lst[1]:
        print("A")
    elif lst[1] > lst[0]:
        print("B")
    else:
        print("T")


