import math
import random

"""
(Assign grades) Write a program that reads a list of scores and then assigns grades based on the following scheme:
The grade is A if score is >= best – 10.
The grade is B if score is >= best – 20.
The grade is C if score is >= best – 30.
The grade is D if score is >= best – 40.
The grade is F otherwise.

Here is a sample run:

Enter scores: 40 55 70 58
Student 0 score is 40 and grade is C
Student 1 score is 55 and grade is B
Student 2 score is 70 and grade is A
Student 3 score is 58 and grade is B
"""

def assign_grades(marks: list):
    best_mark = max(marks)

    for i in range (len(marks)):
        grade = ""
        if marks[i] >= best_mark - 10:
            grade = "A"
        elif marks[i] >= best_mark - 20:
            grade = "B"
        elif marks[i] >= best_mark - 30:
            grade = "C"
        elif marks[i] >= best_mark - 40:
            grade = "D"
        else:
            grade = "F"
        print("student", i, "score is", marks[i], "and grade is", grade)


"""
(Reverse the numbers entered) Write a program that reads a list of integers and displays them in the reverse order in 
which they were read.



"""
def reverse_numbers(lst):
    num = []
    for i in range(len(lst) - 1, -1, -1):
        num.append(lst[i])
    return num


"""
Write a programme that reads some integers between 1 and 100 and counts the occurrences of each. Here is a sample run of 
the programme:
 
Enter integers between 1 and 100: 2 5 6 5 4 3 23 43 2
2 occurs 2 times
3 occurs 1 time
4 occurs 1 time
5 occurs 2 times
6 occurs 1 time
23 occurs 1 time
43 occurs 1 time

Note that if a number occurs more than one time, the plural word “times” is used in the output.
"""
def times(lst: list) -> None:
    set2 = set(lst)
    for x in set2:
        count = lst.count(x)
        print(x, "occurs", count, "time" if count == 1 else "times")


"""
Write a program that reads an unspecified number of scores and determines how many scores are above or equal to the 
average and how many scores are below the average. Assume the input numbers are separated by one space in one line.

Sample Run:
Enter integers between 1 and 100: 2 5 7 8 8 49 99

Sample output:
5 numbers are below average.
"""
def average(nums: list) -> int:
    count2 = 0
    average1 = 0
    for x in nums:
        average1 += x
    average1 = average1 / len(nums)
    below_average = [x for x in nums if x < average1]
    return len(below_average)


"""
Write a programme that reads in numbers separated by a space in one line and displays distinct numbers (i.e., if a 
number appears multiple times, it is displayed only once). Here is the sample run of the programme:

Enter ten numbers: 1 2 3 2 1 6 3 4 5 2
The distinct numbers are: 1 2 3 6 4 5 (order is irrelevant)
"""
def distinct_number(nums: list) -> set:
    return set(nums)


"""
You can determine whether a number n is prime by checking whether 2, 3, 4, 5, 6, ..., n/2 is a divisor for n. If a 
divisor is found, n is not prime. A more efficient approach is to check whether any of the prime numbers less than or 
equal to √n can divide n evenly. If not, n is prime. Display the first 50 prime numbers using this approach.
You need to use a list to store the prime numbers and later use them to check whether they are possible divisors for n.

Enter a number: 25
25 is not a prime number
"""
def prime_number(num):

    for x in range(2, (int(math.sqrt(num)) + 1)):
        if num % x == 0:
            return False
    return True


"""
(Count single digits) Write a program that generates 1,000 random integers between 0 and 9 and displays the count for 
each number. (Hint: Use a list of ten integers, say counts, to store the counts for the number of 0s, 1s, ..., 9s.)

Sample Run: 
Generating a 1000 random numbers!
The 0s repeated 99 times
The 1s repeated 50 times
The 2s repeated 50 times
The 3s repeated 101 times
The 4s repeated 135 times
The 5s repeated 65 times
The 6s repeated 89 times
The 7s repeated 111 times
The 8s repeated 100 times
The 9s repeated 100 times
"""
def count_single_digits():
    lst = []
    for x in range(1, 1001):
        i = random.randint(0, 9)
        lst.append(i)

    for i in range(10):
        print("The", str(i) + "s repeated", lst.count(i), "times" )


"""
(Find the index of the smallest element) Write a function that returns the index of the smallest element in a list of 
integers. If the number of such elements is greater than 1, return the smallest index. Use the following header:
def indexOfSmallestElement(lst):
Write a test program that prompts the user to enter a list of numbers, invokes this
function to return the index of the smallest element, and displays the index.

Sample Run:
Enter a list of 10 numbers: 2 4 4 2 1 3 6 3 2 1
The index of the smallest number is 4
"""
def indexOfSmallestElement(lst):
    return min([i for i in range(len(lst)) if lst[i] == min(lst)])


"""
Write the function that reverses the list passed in the argument and returns this list. Write a test programme that 
prompts the user to enter a list of num- bers, invokes the function to reverse the numbers, and displays the numbers.
"""
def reverse_lst(lst: list):
    lst.reverse()
    return lst


"""
Random number chooser) You can shuffle a list using random.shuffle(lst). Write your own function without using 
random.shuffle(lst) to shuffle a list and return the list. Use the following function header:
def shuffle(lst):
Write a test program that prompts the user to enter a list of numbers, invokes the
function to shuffle the numbers, and displays the numbers.
"""
def shuffle(lst):
    pass