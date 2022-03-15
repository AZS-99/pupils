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
The distinct numbers are: 1 2 3 6 4 5
"""
def distinct_number(nums: list) -> set: