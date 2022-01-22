"""
Write a program that prompts the user to enter each student’s score, and displays the highest and second
highest scores.
"""
def highest_number():
    with open("scores") as file:
        lines = file.read().splitlines()
        lines = [int(x) for x in lines]
    print(max(lines))

"""
Write a program that displays, ten numbers per line, all the numbers from 100 to 1,000 that are divisible by 5 and 6
"""
def ten_numbers():
    lines = []
    for x in range(100, 1000):
        if x % 6 == 0 and x % 5 == 0:
            lines.append(x)
    print(lines)