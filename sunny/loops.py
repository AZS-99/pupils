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
    prime =




