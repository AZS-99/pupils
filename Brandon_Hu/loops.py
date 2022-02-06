"""
Write a program that displays the following table (note that 1 kilogram is 2.2 pounds):
Kilograms   Pounds
1           2.2
3           6.6
...
197         433.4
199         437.8
"""
def kilo_pound():
    print("{:<10} {:<10}".format("kilogram", "pounds"))
    for i in range(1, 200, 2):
        pound = round(i * 2.2,1)
        print("{:<10} {:<10}".format(i, pound))



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
def kilo_miles():
    print("{:<15} {:<15} |   {:<15} {:<15}".format("Miles","Kilometers","Kilometers","Miles"))
    for i in range(1,11):
        kilos1 = round(i * 1.6, 2)
        kilos2 = i * 5 + 15
        miles2 = kilos2 * 0.621
        print("{:<15} {:<15} |   {:<15} {:<15}".format(i, kilos1, kilos2, miles2))


"""
Suppose that the tuition for a university is $10,000 this year and increases 5% every year. Write a program that 
computes the tuition in ten years and the total cost of four years’ worth of tuition starting ten years from now.
"""
def tuition():
    piggy_bank = 10000
    for i in range(9):
        piggy_bank = piggy_bank * 1.05
    total = piggy_bank *
