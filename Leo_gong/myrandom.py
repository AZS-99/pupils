import random

"""
Write a program that generates two integers under 100 and prompts the user to enter the sum of these two integers. 
The program then reports true if the answer is correct, false otherwise
"""

def game():
    num1 = random.randint(0, 100)
    num2 = random.randint(0, 80)
    answer = num1 + num2
    print("What is the value of", str(num1), "+", num2, "?")
    users_answer = int(input())
    if users_answer == answer:
        return True
    else:
        return False


def guess_number():
    num1 = random.randint(0, 100)
    guess = -1
    while guess != num1:
        guess = int(input("Please write down your guess:"))
        if guess > num1:
            print("TOO HIGH")

        elif guess < num1:
            print("TOO LOW")
        else:
            print("Correct answer")

def biggest_number():
    nums =[]
    for i in range(10):
        num = random.randint(0, 10)
        nums.append(num)
    print(nums)
    print("Max num is:", max(nums))


"""
Write a program that reads an unspecified number of integers, determines how many positive and negative values have been 
read, and computes the total and average of the input values (not counting zeros). Your program ends with the input 0. 
Display the average as a floating-point number. Here is a sample run:

Enter an integer, the input ends if it is 0: 1
Enter an integer, the input ends if it is 0: 2
Enter an integer, the input ends if it is 0: -1
Enter an integer, the input ends if it is 0: 3
Enter an integer, the input ends if it is 0: 0

The number of positives is 3
The number of negatives is 1
The total is 5
The average is 1.25
"""

# def leo():
#     nums = []
#     num = -1
#     pos_count = 0
#     neg_count = 0
#     while num != 0:
#         num = int(input("Enter an integer, the input ends if it is 0:"))
#         nums.append(num)
#         if num > 0:
#             pos_count += 1
#         elif num < 0:
#             neg_count += 1
#     total = pos_count + neg_count
#     average = sum(nums) / to
#     print("The number of positives is", pos_count)
#     print("The number of negatives is", neg_count)
#     print("total is", sum(num
#     print("The average is", average))



"""
Write a program that displays kilometers expressed in miles (note that 1 mile is 1.609 kilometers):
"""
def km():
    miles = int(input("The mile is"))
    km = miles * 1.609
    print("The kilometers are", km)


"""
(Random character) Write a program that displays a random uppercase letter.
"""
def character():
    num = random.randint(65, 90)
    return chr(num)


"""
(Game: scissor, rock, paper) Write a program that plays the popular scissor-rock-paper game. (A scissor can cut a paper,
a rock can knock a scissor, and a paper can wrap a rock.) The program randomly generates a number 0, 1, or 2 
representing scissor, rock, and paper. The program prompts the user to enter a number 0, 1, or 2 and displays a message 
indicating whether the user or the computer wins, loses, or draws. Here are sample runs:
 
Sample Run 1:
scissor (0), rock (1), paper (2): 1
The computer is scissor. You are rock. You won.

Sample Run 2:
scissor (0), rock (1), paper (2): 2
The computer is paper. You are paper too. It is a draw.
"""
def scissor_rock_paper():
    computer = random.randint(0, 2)
    user = int(input("scissor (0), rock (1), paper (2):"))
    if (computer == 0 and user == 1) or (computer == 1 and user == 2) or (computer == 2 and user == 0):
        return computer, user, 1
    elif computer == user:
        return computer, user, 0
    else:
        return computer, user, 2


"""
Write a program to generate a three-digit lottery number. The program prompts the user to enter a three-digit number and 
determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is $10,000.
2. If all the digits in the user input match all the digits in the lottery number, the award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is $1,000.
"""
def three_digit(num):
    computer = random.randint(100, 999)
    print("Computer chose:", computer)
    if computer == num:
        return 10000
    else:
        s = set()
        s_computer = set()
        for i in range(3):
            s.add(num % 10)
            num //= 10
        for x in range(3):
            s_computer.add(computer % 10)
            computer //= 10
        if s == s_computer:
            return 3000
        elif s.intersection(s_computer):
            return 1000
        else:
            return 0