"""
Suppose you save $100 each month into a savings account with an annual interest rate of 5%. Therefore, the monthly
interest rate is 0.05/12 = 0.00417. After the first month, the value in the account becomes
          100 * (1 + 0.00417) = 100.417
After the second month, the value in the account becomes
          (100 + 100.417) * (1 + 0.00417) = 201.252
After the third month, the value in the account becomes
          (100 + 201.252) * (1 + 0.00417) = 302.507
and so on.
Write a program that prompts the user to enter a monthly saving amount and displays the account value after the sixth
month. Here is a sample run of the program:
Enter the monthly saving amount: 100
After the sixth month, the account value is 608.81
"""

def interest(balance):
    for i in range(1, 6):
        balance += 100
        balance *= (1 + 0.05/12)
    return balance


"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.8
"""

def table():
    print("{:<10} {:<7}".format("Kilograms", "Pounds"))
    for i in range(1, 200, 2):
        kilograms = i
        pounds = round(kilograms * 2.2, 2)
        print("{:<10} {:<7}".format(kilograms, pounds))


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

def tables():
    print("{:<15} {:<15} | {:<15} {:<15}".format("Miles", "Kilometers", "Kilometers", "Miles"))
    for i in range(1, 11):
        miles = i
        kilometers = miles * 1.609
        kilometers_2 = i * 5 + 15
        miles_2 = kilometers_2 * 0.621
        print("{:<15} {:<15} | {:<15} {:<15}".format(miles, kilometers, kilometers_2, miles_2))


"""
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that 
computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
"""

def university():
    tuition = 10000
    tuition_10 = 0
    for i in range(9):
        tuition_10 = tuition * 1.05
    total_cost = tuition_10
    for i in range(3):
        tuition_10 *= 1.05
        total_cost += tuition_10
    return total_cost


"""
Use a while loop to find the smallest integer n such that n^2 is greater
than 12,000.
"""

def n_squared():
    n = 0
    while n**2 < 12000:
        n += 1
    return n