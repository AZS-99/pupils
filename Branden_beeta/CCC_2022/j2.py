"""
Problem Description
Fergusonball players are given a star rating based on the number of points that they score and the number of fouls that
they commit. Specifically, they are awarded 5 stars for each point scored, and 3 stars are taken away for each foul
committed. For every player, the number of points that they score is greater than the number of fouls that they commit.
Your job is to determine how many players on a team have a star rating greater than 40. You also need to determine if
the team is considered a gold team which means that all the players have a star rating greater than 40.

Input Specification
The first line of input consists of a positive integer N representing the total number of players on the team. This is
followed by a pair of consecutive lines for each player. The first line in a pair is the number of points that the
player scored. The second line in a pair is the number of fouls that the player committed. Both the number of points and
the number of fouls, are non-negative integers.

Output Specification
Output the number of players that have a star rating greater than 40, immediately followed by a plus sign if the team is
considered a gold team.

Sample Input 1
3
12
4
10
3
9
1
Output for Sample Input 1
3+

Explanation of Output for Sample Input 1
The image shows the star rating for each player. For example, the star rating for the first player is 12×5−4×3 = 48. All
three players have a rating greater than 40 so the team is considered a gold team.


Sample Input 2
2
8
0
12
1
Output for Sample Input 2
1
Explanation of Output for Sample Input 2
The image shows the star rating for each player. Since only one of the two players has a rating greater than 40, this
team is not considered a gold team.
"""

def five_star_calculation():
    file = open("CCC_2022/j2", "r")
    num_of_players = int(file.readline())
    passed_40 = 0
    for i in range(num_of_players):
        score = int(file.readline())
        foul = int(file.readline())
        if score * 5 - foul * 3 > 40:
            passed_40 += 1
    if passed_40 == num_of_players:
        return str(passed_40) + "+"
    else:
        return str(passed_40)
        
        
"""
The CCC harp is a stringed instrument with strings labelled A,B,...,T. Like other instruments, it can be out of tune.
A musically inclined computer science student has written a clever computer program to help tune the harp. The program
analyzes the sounds produced by the harp and provides instructions to fix each string that is out of tune. Each
instruction includes a group of strings, whether they should be tightened or loosened, and by how many turns.


Unfortunately, the output of the program is not very user friendly. It outputs all the tuning instructions on a single
line. For example, the single line AFB+8HC-4 actually con- tains two tuning instructions: AFB+8 and HC-4. The first
instruction indicates that harp strings A, F, and B should be tightened 8 turns, and the second instruction indicates
that harp strings H and C should be loosened 4 turns.

Your job is to take a single line of tuning instructions and make them easier to read.

Input Specification
There will be one line of input which is a sequence of tuning instructions. Each tuning instruction will be a sequence
of uppercase letters, followed by a plus sign (+) or minus sign (-), followed by a positive integer. There will be at
least one instruction and at least one letter per instruction. Also, each uppercase letter will appear at most once.

Output Specification
There will be one line of output for each tuning instruction. Each line of output will consist of three parts, each
separated by a single space: the uppercase letters referring to the strings, tighten if the instruction contained a plus
sign or loosen if the instruction contained a minus sign, and the number of turns.

Sample Input 1
AFB+8HC-4

Output for Sample Input 1
AFB tighten 8
HC loosen 4

Explanation of Sample Output 1
The input contains two tuning instructions: AFB+8 and HC-4.

Sample Input 2
AFB+8SC-4H-2GDPE+9

Output for Sample Input 2
AFB tighten 8
SC loosen 4
H loosen 2
GDPE tighten 9

Explanation of Sample Output 2
The input contains four tuning instructions: AFB+8, SC-4, H-2, and GDPE+9.
"""
