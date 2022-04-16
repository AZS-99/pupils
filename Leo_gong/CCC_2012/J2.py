"""
Problem J2: Sounds fishy!
Problem Description
A fish-finder is a device used by anglers to find fish in a lake. If the fish-finder finds a fish, it will sound an
alarm. It uses depth readings to determine whether to sound an alarm. For our purposes, the fish-finder will decide that
a fish is swimming past if:

• there are four consecutive depth readings which form a strictly increasing sequence (such as 3 4 7 9) (which we will
call “Fish Rising”), or
• there are four consecutive depth readings which form a strictly decreasing sequence (such as 9 6 5 2) (which we will
call “Fish Diving”), or
• there are four consecutive depth readings which are identical (which we will call “Constant Depth”).
All other readings will be considered random noise or debris, which we will call “No Fish.” Your task is to read a
sequence of depth readings and determine if the alarm will sound.

Input Specification
The input will be four positive integers, representing the depth readings. Each integer will be on its own line of input

Output Specification
The output is one of four possibilities. If the depth readings are increasing, then the output should be Fish Rising. If
the depth readings are decreasing, then the output should be Fish Diving. If the depth readings are identical, then the
output should be Fish At Constant Depth. Otherwise,the output should be No Fish.

Sample Input 1
30
10
20
20
Output for Sample Input 1
No Fish

Sample Input 2
1
10
12
13
Output for Sample Input 2
Fish Rising
"""
def fishing():
    file = open("CCC_2012/J2", "r")
    first_time = int(file.readline())
    second_time = int(file.readline())
    third_times = int(file.readline())
    fourth_times = int(file.readline())
    if first_time > second_time > third_times > fourth_times:
        print("Fish Diving")
    elif first_time == second_time == third_times == fourth_times:
        print("Constant Depth")
    elif first_time < second_time < third_times < fourth_times:
        print("Fish Rising")
    else:
        print("No Fish")