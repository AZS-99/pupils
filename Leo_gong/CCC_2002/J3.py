"""
The Students council in your school wants to organize a charity breakfast, and since older students are both wiser and
richer, the members of the council decide that the price of each ticket will be based on how many years you have been in
the school. A first year student will buy a PINK ticket, a second year student will buy a GREEN ticket, a third year
student will buy a RED ticket, and a fourth year student will buy an ORANGE ticket.
Assume that all tickets are sold. Each colour of ticket is uniquely priced. Input the cost of a PINK, GREEN, RED, and
ORANGE ticket (in that exact order). Input the exact amount of money to be raised by selling tickets. Output all
combinations of tickets that produce exactly the desired amount to be raised. The combinations may appear in any order.
Output the total number of combinations found. Output the smallest number of tickets to print to raise the desired
amount so that printing cost is minimized.
Keyboard input and screen output is expected.

Sample Session. User input in italics.
Cost of PINK tickets:
1
Cost of GREEN tickets:
2
Cost of RED tickets:
3
Cost of ORANGE tickets:
4
How much must be raised with ticket sales?
3

Combinations are
# of PINK is 0      # of Green is 0     # of RED is 1       # of ORANGE is 0
# of PINK is 1      # of Green is 1     # of RED is 0       # of ORANGE is 0
# of PINK is 3      # of Green is 0     # of RED is 0       # of ORANGE is 0

Total combinations is 3
Minimum number of ticket print is 1
"""
def tickets():
    pink = int(input("Cost of PINK tickets:"))
    green = int(input("Cost of GREEN tickets:"))
    red = int(input("Cost of RED tickets:"))
    orange = int(input("Cost of ORANGE tickets:"))
    money = int(input("How much be raised with ticket sales?"))
    max_p = money // pink
    max_g = money // green
    max_r = money // red
    max_o = money // orange
    combinations = 0
    min_num = float('inf')
    for p in range(max_p + 1):
        for g in range(max_g + 1):
            for r in range(max_r + 1):
                for o in range(max_o + 1):
                    if p * pink + g * green + r * red + o * orange == money:
                        print("# of PINK is", str(p) + "\t", "# of Green is", str(g) + "\t", "# of RED is", str(r) +\
                              "\t", "# of ORANGE is", str(o) + "\t")
                        combinations += 1
                        if p + g + r + o < min_num:
                            min_num = p + g + r + o
    print()
    print("Total combinations is", combinations)
    print("Minimum number of ticket print is", min_num)