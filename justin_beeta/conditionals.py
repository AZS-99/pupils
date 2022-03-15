import random
"""
Write a programme that generates two random numbers between 1 and 100, then asks the user to enter their sum.
The programme returns either true or false.

Sample Run 1:
What is the sum of 5 + 2? 8
False 

Sample Run 2:
What is the sum of 7 + 3? 10
True 
"""
def random_number():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    s = int(input("What is the sum of" + str(num1) + "+" + str(num2) + "?"))
    if num1 + num2 == s:
        return True
    return False


"""
(Find future dates) Write a program that prompts the user to enter an integer for today’s day of the week (Sunday is 0,
Monday is 1, ..., and Saturday is 6). Also prompt the user to enter the number of days after today for a future day and 
display the future day of the week. Here is a sample run:
 
Enter today's day: 1
Enter the number of days elapsed since today: 3
Today is Monday and the future day is Thursday
"""
def today_and_future():
    s = input("Enter today's day: ")
    x = input("Enter the number of days elapsed since today: ")
    pass




"""
Write a programme that prompts the user to enter a number of integers (max 10 numbers), saves the numbers into a list, 
then swaps the first and the last number.

Sample Run 1:
Enter any number of integers separated by a comma: 10, 5, 4, 9
Sample Output 1:
[9, 5, 4, 10]

Sample Run 2:
Enter any number of integers separated by a comma: 7, 9, 2, 5 8
Sample Output 2:
[8, 9, 2, 5, 7]
"""
def swaps_first_last(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst





"""
Write a programme that prompts the user to enter a number of integers (max 10 numbers), saves the numbers into a list, 
then displays that list in a reversed order. (Note: using methods is not allowed)

Sample Run:
Enter any number of integers separated by a comma: 10, 5, 4, 9
Sample Output:
[9, 4, 5, 10]
"""
def reversed_order(lst):
    length = len(lst)
    for i in range(0, length // 2):
        lst[i], lst[-i-1] = lst[-i-1], lst[i]
    return lst





"""
Write a programme that prompts the user to enter 2 lists of integers, of length that does not exceed 5 for each, then 
concatenates both lists and displays the result

Sample Run:
Enter max 5 integers separated by a comma: 10, 5, 4, 9
Enter max 5 integers separated by a comma: 1, 2, 3

Sample Output:
[10, 5, 4, 9, 1, 2, 3]
"""
def add_two_lists(lst1, lst2):
    x = lst1 + lst2
    return x






"""
Write a programme that prompts the user to enter a list of integers, then returns a list of the squares of each integer
in the original list.

Sample Run:  
Enter max 5 integers separated by a comma: 1, 2, 3, 4

Sample Output: 
[1, 4, 9, 8]
"""
def list_squares(lst):
    new_lst = []
    new_lst.append(lst[0] ** 2)






"""
Write a programme that prompts the user to enter 2 lists OF THE SAME LENGTH, then iterates both lists simultaneously and 
displays items from list1 in original order and items from list2 in original order.

Sample Run:
Enter max 10 integers separated by a comma: 1, 2, 3, 4
Enter max 10 integers separated by a comma: 5, 6, 7, 8

Sample Output:
1   5
2   6
3   7
4   8
"""





"""
Write a programme that prompts the user to enter 2 lists OF THE SAME LENGTH, then iterates both lists simultaneously and 
displays items from list1 in original order and items from list2 in REVERSE order.

Sample Run:
Enter max 10 integers separated by a comma: 1, 2, 3, 4
Enter max 10 integers separated by a comma: 5, 6, 7, 8

Sample Output:
1   8
2   7
3   6
4   5
"""



"""
Write a programme that prompts the user to enter 2 lists that do not necessarily have the same length, then iterates 
both lists simultaneously and displays items from list1 in original order and items from list2 in REVERSE order. If one
list is finished before the other, then display a default as an asterisk.

Sample Run:
Enter max 10 integers separated by a comma: 1, 2, 3, 4, 5
Enter max 10 integers separated by a comma: 7, 8, 9

Sample Output:
1   9
2   8
3   7
4   *
5   *
"""

































































