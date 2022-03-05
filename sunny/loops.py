def squares():
    for i in range(1, 11):
      print(i**2)


# nested loops
def times_table():
    for i in range(1,32):
        for j in range(1,11):
            print(i,"x",j,"=",i*j)


# accumulation
def sum_numbers(n):
    piggy_bank = 0
    for i in range(1,n):
        piggy_bank += i
    print("piggy_bank=",piggy_bank)


def sum_squares(n):
    piggy_bank = 0
    for i in range(1,n):
        piggy_bank += i**2
    print(piggy_bank)


def factorial(n):
    piggy_bank = 1
    for i in range(n):
        piggy_bank *= i
    print(piggy_bank)


"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
5
...
197         433.4
199         437.8
"""
def kilograms():
    print("{:>10} {:>10}".format("kilograms", "pounds"))
    for k in range(1,200, 2):
        pounds = round(k * 2.2, 1)
        print("{:<10} {:>10}".format(k,pounds))


"""
Write a program that displays the following two tables side by side (note that 1 mile is 1.609 kilometers and that 
1 kilometer is 0.621 mile):
Miles         Kilometers   |   Kilometers   Miles     
1             1.609        |   20           12.42     
2             3.218        |   25           15.525    
3             4.827        |   30           18.63     
4             6.436        |   35           21.735    
5             8.045        |   40           24.84     
6             9.654        |   45           27.945    
7             11.263       |   50           31.05     
8             12.872       |   55           34.155    
9             14.481       |   60           37.26     
10            16.09        |   65           40.365   
"""

def kilometers():
    print("{:<10} {:>10} | {:<10} {:>10}".format("Miles", "Kilometers", "Kilometers", "Miles"))
    for miles in range(1,11):
        km1 = round(miles * 1.609, 3)
        km2 = 5 * miles + 15
        miles2 = round(km2 * 0.621, 3)
        print("{:<10} {:>10} {:<10} {:>10}".format(miles, km1, km2,miles2))


"""
Use a while loop to find the smallest integer in such that n^2 is greater
than 12,000.
"""
def wl():
    n = 1
    while n**2 < 12000:
        n = n+1
    return n


"""
Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, 
if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5
"""
def is_prime(num):
    for i in range(2,num):
        if num % i == 0:
            return False
    return True

def primes(num):
    primes_lst = []
    for i in range(2,num):
        if is_prime(i):
            primes_lst.append(i)
    return primes_lst

def factors(num):
    factors_lst = []
    primes_lst = primes(num)
    for i in primes_lst:
        while num % i == 0:
            num = num // i
            factors_lst.append(i)
    return factors_lst



"""
Write a program to sum the following series and find the EXACT value:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99
"""

def fractions():
    total = 0
    for i in range(1, 98, 2):
        numerator = i
        denominator = numerator + 2
        fractions = numerator/denominator
        total += fractions
    return round(total, 4)


"""
You can approximate e by using the following series
e = 1 + 1/1! + 1/2! + 1/3! + ... + 1/i!
Write a program that displays the e value for i = 10000, 20000, . . ., and 100000.
"""
def factorial(n):
    total = 1
    for i in range(1, n+1):
        total = total * i
    return total

def e():
    total = 1
    for i in range(1, 1000):
        numerator = 1
        denominator = factorial(i)
        fraction = numerator / denominator
        total += fraction
    return round(total, 3 )


import math
"""
Write a program that computes the following summation:
1 / (√1 + √2)   +   1 / (√2 + √3)   +   1 / (√3 + √4)    +   ....   +    1 / (√624 + √625)
"""
def summation():
    total = 0
    for i in range(1, 625):
        numerator = 1
        denominator = math.sqrt(i) + math.sqrt(i + 1)
        fraction = numerator / denominator
        total += fraction
    return round(total)


"""
Write a program that reads integers, finds the largest of them, and counts its occurrences. Assume that the input ends 
with number 0. Suppose that you entered 3 5 2 5 5 5 0; the program finds that the largest number is 5 and the 
occurrence count for 5 is 4. (Hint: Maintain two variables, max and count. The variable max stores the current maximum 
number, and count stores its occurrences. Initially, assign the first number to max and 1 to count. Compare each 
subsequent number with max. If the number is greater than max, assign it to max and reset count to 1. If the number is 
equal to max, increment count by 1.)
Enter a number (0: for end of input): 3
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 2
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 5
Enter a number (0: for end of input): 0
The largest number is 5
The occurrence count of the largest number is 4
"""
def inputing():
    x = -1
    lst = []
    while x != 0:
        x = int(input("Enter a number (0: for end of input): "))
        lst.append(x)
    biggest_num = max(lst)
    count = lst.count(biggest_num)
    return biggest_num, count


"""
Write a program that displays all possible combinations for picking two numbers from integers 1 to 7. Also display the 
total number of combinations.
Sample Output:
1 2
1 3
1 4
1 5
1 6
1 7
2 3
2 4
...
...
5 6
5 7
6 7
The total number of all combinations is 21
"""
def combination():
    for i in range(1, 7):
        for j in range(i + 1, 8):
            print(i, j)

