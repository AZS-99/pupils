"""

In many cryptographic applications the Modular Inverse is a key point. This question involves finding the modular
inverse of a number.
Given 0 < x < m, where x and m are integers, the modular inverse of x is the unique integer n,
0 < n < m, such that the remainder upon dividing x ¥ n by m is 1.
For example, 4 ¥ 13 = 52 = 17 ¥ 3 + 1 , so the remainder when 52 is divided by 17 is 1, and thus 13 is the inverse of 4
modulo 17.
You are to write a program which accepts as input the two integers x and m, and outputs either the modular inverse n, or
the statement "No such integer exists." if there is no such integer n.
Input is from the keyboard, and you may assume that m ≤ 100. Output is to the screen.

Sample session: (user input in italics)
Enter x:
4
Enter m:
17

13

Enter x:
6
Enter m:
10
No such integer exists.
"""
def calculation():
    x = int(input("Enter x:"))
    m = int(input("Enter m:"))
    n = 0
    answer = x * n % m
    count = 0
    while answer != 1 and count < 1000:
        n += 1
        answer = x * n % m
        count += 1

    print(n if answer == 1 else "no such integer")