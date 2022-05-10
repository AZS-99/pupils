"""
In CS City, a mathematical place to live, the mayor is elected every 4 years, the treasurer is appointed every 2 years,
the chief programmer is elected every 3 years and the dog-catcher is replaced every 5 years.
This year, Year X, the newly elected mayor announced the appointment of the new treasurer, a new dog-catcher and
congratulated the chief programmer for winning the recent election. That is, all positions were changed over. This is
highly unusual. You will quantify how unusual this really is.
Write a program that inputs the year X and the future year Y and lists all years between X and Y inclusive when all
positions change.

Sample Session
Program Output:
Enter the current year: 2004
Enter a future year: 2100
All positions change in year 2004 All positions change in year 2064
"""
import math
def all_positions_change():
    current_year = int(input("Enter the current year: "))
    future_year = int(input("Enter the future year: "))
    lcm = math.lcm(4, 2, 3, 5)
    next_time = current_year + lcm
    print("All positions change in year " + str(current_year) + " All positions change in year " + str(next_time))