"""
A simile is a combination of an adjective and noun that produces a phrase such as "Easy as pie" or "Cold as ice".
Write a program to input n adjectives (1 < n <= 5) and m nouns (1 < m <= 5) provided by your contest supervisor,
and print out all possible similes. The first two lines of input will provide the values of n and m, in that order
followed, one per line, by n adjectives and m nouns. Your program may output the similes in any order.

Sample Input:
3
2
Easy
Smart
Soft
pie
rock

Sample output:
Easy as pie
Easy as rock
Smart as pie
Smart as rock
Soft as pie
Soft as rock
"""
def simile():
    file = open("CCC_2004/J3", "r")
    n = int(file.readline())
    m = int(file.readline())
    lst = []
    lst2 = []
    for i in range(n):
        word = file.readline()
        lst.append(word[:-1])

    for i in range(m):
        word = file.readline()
        lst2.append(word[:-1] if i < m - 1 else word)

    for i in range(n):
        for j in range(m):
            print(str(lst[i]), "as", str(lst2[j]))