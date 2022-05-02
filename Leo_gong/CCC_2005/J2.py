"""

When a credit card number is sent through the Internet it must be protected so that other people cannot see it.
 Many web browsers use a protection based on "RSA Numbers."
A number is an RSA number if it has exactly four divisors. In other words, there are exactly four numbers that divide
into it evenly. For example, 10 is an RSA number because it has exactly four divisors (1, 2, 5, 10). 12 is not an RSA
number because it has too many divisors (1, 2, 3, 4, 6, 12). 11 is not an RSA number either. There is only one RSA
number in the range 10...12.
Write a program that inputs a range of numbers and then counts how many numbers from that range are RSA numbers. You may
assume that the numbers in the range are less than 1000.

Sample Session 1
Program Output: Enter lower limit of range
User Input: 10
Program Output: Enter upper limit of range
User Input: 12
Program Output: The number of RSA numbers between 10 and 12 is 1

Sample Session 2
Program Output: Enter lower limit of range
User Input: 11
Program Output: Enter upper limit of range
User Input: 15
Program Output: The number of RSA numbers between 11 and 15 is 2

"""
def protected_numbers():
    lowest_num = int(input("Program Output: Enter lower limit of range"))
    greatest_num = int(input("Program Output: Enter upper limit of range"))
    count = 0
    count_nums = 0

    for i in range(lowest_num, greatest_num + 1):
        for j in range(1, i + 1):
            if i % j == 0:
                count += 1

        if count == 4:
            count_nums += 1

        count = 0

    print("The number of RSA numbers between", lowest_num, "and", greatest_num, "is", count_nums)