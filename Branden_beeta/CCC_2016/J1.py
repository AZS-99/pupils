"""
Problem J1: Tournament Selection

Problem Description
Each player in a tournament plays six games. There are no ties. The tournament director places the players in groups
based on the results of games as follows:
• if a player wins 5 or 6 games, they are placed in Group 1;
• if a player wins 3 or 4 games, they are placed in Group 2;
• if a player wins 1 or 2 games, they are placed in Group 3;
• if a player does not win any games, they are eliminated from the tournament.
Write a program to determine which group a player is placed in.

Input Specification
The input consists of six lines, each with one of two possible letters: W (to indicate a win) or L (to indicate a loss).
Output Specification
The output will be either 1, 2, 3 (to indicate which Group the player should be placed in) or -1 (to indicate the player
has been eliminated).
Sample Input 1
W
L
W
W
L
W
Output for Sample Input 1
2

Sample Input 2
L
L
L
L
L
L
Output for Sample Input 2
-1
"""
def judge():
    file = open("CCC_2016/J1", "r")
    wins = 0
    for i in range(6):
        line = file.readline()
        if line == "W" or line == "W\n":
            wins += 1
    if 6 >= wins >= 5:
        print(1)
    elif 4 >= wins >= 3:
        print(2)
    elif 2 >= wins >= 1:
        print(3)
    else:
        print(-1)
