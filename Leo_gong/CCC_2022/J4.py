"""
Problem Description
A class has been divided into groups of three. This division into groups might violate two types of constraints: some
students must work together in the same group, and some students must work in separate groups.
Your job is to determine how many of the constraints are violated.

Input Specification
The first line will contain an integer X with X ≥ 0. The next X lines will each consist of two different names,
separated by a single space. These two students must be in the same group.
The next line will contain an integer Y with Y ≥ 0. The next Y lines will each consist of two different names, separated
by a single space. These two students must not be in the same group.

Among these X + Y lines representing constraints, each possible pair of students appears at most once.
The next line will contain an integer G with G ≥ 1. The last G lines will each consist of three different names,
separated by single spaces. These three students have been placed in the same group.
Each name will consist of between 1 and 10 uppercase letters. No two students will have the same name and each name
appearing in a constraint will appear in exactly one of the G groups.

Output Specifications:
Output an integer between 0 and X+Y which is the number of constraints that are violated.

Sample Input 1
1
ELODIE CHI
0
2
DWAYNE BEN ANJALI
CHI FRANCOIS ELODIE
Output for Sample Input 1
0

Explanation of Output for Sample Input 1
There is only one constraint and it is not violated: ELODIE and CHI are in the same group.


Sample Input 2
3
A B
G L
J K
2
D F
D G
4
A C G
B D F
E H I
J K L
Output for Sample Input 2
3

Explanation of Output for Sample Input 2
The first constraint is that A and B must be in the same group. This is violated.
The second constraint is that G and L must be in the same group. This is violated.
The third constraint is that J and K must be in the same group. This is not violated. The fourth constraint is that D
and F must not be in the same group. This is violated. The fifth constraint is that D and G must not be in the same
group. This is not violated. Of the five constraints, three are violated.
"""
def groups():
    file = open("CCC_2022/J4", "r")
    num_together = int(file.readline())
    together_lst = []
    for i in range(num_together):
        together_a, together_b = file.readline().split(" ")
        together_lst.append([together_a, together_b[:-1]])

    not_together_lst = []
    num_not_together = int(file.readline())

    for i in range(num_not_together):
        not_together_a, not_together_b = file.readline().split(" ")
        not_together_lst.append([not_together_a, not_together_b[:-1]])

    dic1 = {}
    groups_len = int(file.readline())
    for i in range(groups_len):
        ch_a, ch_b, ch_c = file.readline().split(" ")
        dic1[ch_a] = ch_b
        if i == groups_len - 1:
            dic1[ch_b] = ch_c
            dic1[ch_c] = ch_a
        else:
            dic1[ch_b] = ch_c[:-1]
            dic1[ch_c[:-1]] = ch_a

    mistakes = 0
    for lst in together_lst:
        ch_a = lst[0]
        ch_b = lst[1]
        if not (ch_a in dic1.keys() and dic1[ch_a] == ch_b or ch_b in dic1.keys() and dic1[ch_b] == ch_a):
            mistakes += 1

    for lst in not_together_lst:
        ch_a = lst[0]
        ch_b = lst[1]
        if ch_a in dic1.keys() and dic1[ch_a] == ch_b or ch_b in dic1.keys() and dic1[ch_b] == ch_a:
            mistakes += 1

    print(mistakes)