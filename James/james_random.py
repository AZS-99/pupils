import random
"""
Create a game that finds the addition of two random numbers between 0 and 100 inclusive. Then asks the user to guess
the number. The program doesn't terminate until the user guesses the correct number, in which case they win, or when 
they enter -1 as an input, in which case game is over. 
"""
def randomnumber(num=-1) :
    if num == -1:
        num = random.randint(0, 100) + random.randint(0, 100)
    newin = int(input("Guess a number between 0 and 200! "))
    if newin == num:
        return "You won!"
    elif newin == -1:
        return "Overridden"
    elif newin != num:
        print("Oooh, try again.")
        return randomnumber(num)

"""
Write a program that lets the user guess whether a flipped coin displays the head or the tail. The program randomly 
generates an integer 0 or 1, which represents head or tail. The program prompts the user to enter a guess and reports 
whether the guess is correct or incorrect.
"""
def coinflip():
    coin = random.randint(0,1)
    guess = int(input("0 (Tails), or 1 (Heads)?"))
    if coin == guess:
        return "Correct guess!"
    else:
        return "Wrong one!"

"""
Write a program that displays a random uppercase letter.
"""
def randletter():
    numid = random.randint(65, 90)
    print(chr(numid))


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
def rps():
    choice = int(input("scissor (0), rock (1), paper (2): "))
    choice2 = random.randint(0,2)
    choices = [0, 1, 2]
    dic = {0: "scissors", 1: "rock", 2: "paper"}
    finalchoice = dic[choice]
    finalchoice2 = dic[choice2]
    if choice == choice2:
        return "The computer is " + finalchoice2 + ". You are " + finalchoice + ". It is a draw."
    elif choices[choice - 1] == choice2:
        return "The computer is " + finalchoice2 + ". You are " + finalchoice + ". You won."
    else:
        return "The computer is " + finalchoice2 + ". You are " + finalchoice + ". You lost."


"""
Write a program to generate a three-digit lottery number. The program prompts the user to enter a three-digit number and 
determines whether the user wins according to the following rules:
1. If the user input matches the lottery number in the exact order, the award is $10,000.
2. If all the digits in the user input match all the digits in the lottery number, the award is $3,000.
3. If one digit in the user input matches a digit in the lottery number, the award is $1,000.
"""
def lottery():
    lotterynumber = random.randint(100,999)
    usernumber = int(input("Enter a three digit number!"))
    digits = []
    lotterydigits = []


    if lotterynumber == usernumber:
        return "You won $10,000!"
    for x in range (3):
        lotterydigits.append(lotterynumber % 10)
        lotterynumber //= 10
    for x in range (3):
        digits.append(usernumber % 10)
        usernumber //= 10

    digits_set = set(digits)
    lottery_set = set(lotterydigits)
    if digits_set == lottery_set:
        return "You won $3,000!"
    elif digits_set.intersection(lottery_set):
        return "You won 1,000$!"
    else:
        return "You didn't win anything :("
