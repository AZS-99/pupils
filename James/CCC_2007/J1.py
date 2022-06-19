"""
Problem J1: Who is in the middle?
Problem Description
In the story Goldilocks and the Three Bears, each bear had a bowl of porridge to eat while sitting at his/her favourite
chair. What the story didn’t tell us is that Goldilocks moved the bowls around on the table, so the bowls were not at
the right seats anymore. The bowls can be sorted by weight with the lightest bowl being the Baby Bear’s bowl, the medium
bowl being the Mama Bear’s bowl and the heaviest bowl being the Papa Bear’s bowl. Write a program that reads in three
weights and prints out the weight of Mama Bear’s bowl. You may assume all weights are positive integers less than 100.

Sample Input
10
5
8
Output for Sample Input
8
"""
def goldilocks():
    file = open("CCC_2007/J1", "r")
    bowls = []
    for i in range(3):
        bowls.append(int(file.readline()))
    bowls.sort()
    print(bowls[1])