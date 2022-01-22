"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.8
"""
def kg_p():
    print("{:<10}  {:<10}".format("Kilograms", "Pounds"))
    for i in range(1, 200, 2):
        pounds = round(i * 2.2, 1)
        print("{:<10}  {:<10}".format(i, pounds))



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
def table():
    print("{:<10}  {:<10}       |      {:<10}      {:<10}".format("Miles", "Kilometers", "Kilometers", "Miles"))
    for i in range(1, 11):
        kilometers1 = round(i * 1.609, 3)
        kilometers2 = 20 + (i -1) * 5
        miles_2 = round(kilometers2 * 0.621, 3)
        print("{:<10}  {:<10}       |      {:<10}      {:<10}".format(i, kilometers1, kilometers2, miles_2))



"""
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that 
computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
"""
def tuition():
    x = 10000
    m = 0
    for i in range(9):
        x = x * 1.05
    for z in range(4):
        m += x * 1.05
    return round(m, 2)

"""
(Find the smallest n such that n^2 > 12,000) Use a while loop to find the smallest integer n such that n^2 is greater 
than 12,000.
"""
def smallest():
    for x in range(1, 12000):
        if x ** 2 > 12000:
            return x


"""
Write a program that reads an integer and displays all its smallest factors, also known as prime factors. For example, 
if the input integer is 120, the output should be as follows:
2, 2, 2, 3, 5
"""
def is_prime(num):
    for x in range(2, num):
        if num % x == 0:
            return False
    return True

def all_primes(num):
    primes = []
    for x in range(2, num):
        if is_prime(x):
            primes.append(x)
    return primes

def factors(num):
    primes = all_primes(num)
    all_factors = []
    for prime in primes:
        if num % prime == 0:
            all_factors.append(prime)
    return all_factors



"""
Write a program to sum the following series:
1/3  +  3/5  +  5/7  +  7/9  +  9/11  + .... +  95/97  +  97/99
"""
def aaaa():
    for x in range(1, 97, 2):
