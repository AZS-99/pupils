"""
Problem Description
You are hosting a party and do not have room to invite all of your friends. You use the following unemotional
mathematical method to determine which friends to invite.
Number your friends 1, 2, . . . , K and place them in a list in this order. Then perform m rounds. In each round, use a
number to determine which friends to remove from the ordered list.
The rounds will use numbers r1, r2, . . . , rm. In round i remove all the remaining people in positions that are
multiples of ri (that is, ri, 2ri, 3ri, . . .) The beginning of the list is position 1.
Output the numbers of the friends that remain after this removal process.

Input Specification
The first line of input contains the integer K (1 ≤ K ≤ 100). The second line of input contains the integer
m (1 ≤ m ≤ 10), which is the number of rounds of removal. The next m lines each contain one integer. The ith of these
lines (1 ≤ i ≤ m) contains ri ( 2 ≤ ri ≤ 100) indicating that every person at a position which is multiple of ri should
be removed.

Output Specification
The output is the integers assigned to friends who were not removed. One integer is printed per line in increasing
sorted order.

Sample Input
10
2
2
3
Output for Sample Input
1
3
7
9

Explanation of Output for Sample Input
Initially, our list of invitees is 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.
After the first round of removals, we remove the even positions (i.e., every second position), which causes our list of
invitees to be 1, 3, 5, 7, 9. After the second round of removals, we remove every 3rd remaining invitee: thus, we keep 1
and 3, remove 5 and keep 7 and 9, which leaves us with an invitee list of 1, 3, 7, 9.
"""
def party():
    file = open("CCC_2014/J4", "r")
    num_friends = int(file.readline())
    friends = []
    for i in range(1, num_friends + 1):
        friends.append(i)
    num_removal = int(file.readline())
    lst = []
    for i in range(num_removal):
        removal = int(file.readline())
        for j in range(len(friends)):
            if not (j + 1) % removal == 0:
                lst.append(friends[j])
        friends = lst
        lst = []
    print(friends)