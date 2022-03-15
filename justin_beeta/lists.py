"""
For the following list: [2, 3, 5, 7, 11, 13]
Print every element in the list on a separate line
"""
def print_lst():
    lst = [2, 3, 5, 7, 11, 13]
    for i in range(0, 6):
        print(lst[i])


"""
For the following list: [2, 3, 5, 7, 11, 13]
Print the square of every element in the list 
"""
def print_square_lst():
    lst = [2, 3, 5, 7, 11, 13]
    for i in range(0, 6):
        print(lst[i] ** 2)


"""
Write a programme that accepts 5 integers from the user, and adds those values to a list. Print the list you created
"""
def five_integers(num1, num2, num3, num4, num5):
    lst = [num1, num2, num3, num4, num5]
    for i in range(0, 5):
        print(lst[i])


"""
Write a program that reads an unspecified number of integers, adds them to a list, then prints the square of every 
number in the list. Assume that the input ends with number 0. For example, suppose that the user wants to enter 3 5 2 5 5 6; then
they should enter the values as shown in the sample run, and then enter 0 to signal that they are done.
programme should create the list [3, 5, 2, 5, 5, 6], then return the values as follows:

Sample Run
Enter a number (0: for end of input): 3
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 2
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 6
Enter a number (0: for end of input): 0

Sample Output
The squares are:
9
25
4
25
25
36
"""
def lst_squares(lst):
    for i in range(0, len(lst)):
        print(lst[i] ** 2)


"""
Write a program that reads an unspecified number of integers, adds them to a list, then sums up all the values inside
the created list. Assume that the input ends with number 0.

Sample Run
Enter a number (0: for end of input): 3
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 2
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 6
Enter a number (0: for end of input): 0

Sample output
26
"""
def lst_sum(lst):
    total = 0
    for i in range(0, len(lst)):
        total += lst[i]
    return total


"""
Write a program that reads an unspecified number of integers, adds them to a list, then sums up the cubes of the values 
inside the created list. Assume that the input ends with number 0.

Sample Run
Enter a number (0: for end of input): 3
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 2
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 6
Enter a number (0: for end of input): 0

Sample output
626
"""
def cube_sum(lst):
    total = 0


    for i in range(0, len(lst)):
        total += lst[i] ** 3
    return total


"""
Write a program that reads an unspecified number of integers, adds them to a list, determines how many positive and 
negative values have been read, and computes the total and average of the input values (not counting zeros). Your 
program ends with the input 0. 
Display the average as a floating-point number. Here is a sample run:

Sample Input
Enter an integer, the input ends if it is 0: 1
Enter an integer, the input ends if it is 0: 2
Enter an integer, the input ends if it is 0: -1
Enter an integer, the input ends if it is 0: 3
Enter an integer, the input ends if it is 0: 0

Sample Output
The number of positives is 3
The number of negatives is 1
The total is 5
The average is 1.25
"""
def harder_and_harder_lst_question(lst):
    count_negative = 0
    for i in range(0, len(lst)):
        if lst[i] < 0:
            count_negative += 1
    return count_negative


"""
Write a programme that saves the values of the following sequence in a list:
1  ,  3  ,  5  ,  7  ,  9  , .... , 95  , 97
"""
def sequence_1():
    lst = []
    for i in range(1, 98, 2):
        lst.append(i)
    return lst


"""
Write a programme that saves the values of the following sequence in a list:
1/3  ,  1/5  ,  1/7  ,  1/9  ,  1/11  , .... , 1/97  , 1/99
"""
def sequence_2():
    lst = []
    for i in range(3, 100, 2):
        f = 1/i
        lst.append(f)
    return lst



"""
Write a programme that saves the values of the following sequence in a list:
1/3  ,  3/5  ,  5/7  ,  7/9  ,  9/11  , .... , 95/97  ,97/99
"""
def sequence_3():
    lst = []
    for i in range(1, 98, 2):
        numerator = i
        denominator = i + 2
        lst.append(numerator / denominator)
    return lst




"""
Given fahrenheit = (9 / 5) * celsius + 32

Celsius      Fahrenheit   
40.0         104.0        
39.0         102.2       
...
32.0         89.6         
31.0         87.8  

Create 2 lists, one for the values in celsius, and the other for the corresponding Fahrenheit       
"""
def two_lists():
    celsius = []
    fahrenheit = []
    for i in range(40, 30, -1):
        celsius.append(i)
        fahrenheit.append(round((9 / 5) * i + 32, 2))
    return celsius, fahrenheit




















