"""
Problem Description
Many communities now have “radar” signs that tell drivers what their speed is, in the hope that they will slow down.
You will output a message for a “radar” sign. The message will display information to a driver based on his/her speed
according to the following table:

Input Specification
The user will be prompted to enter two integers. First, the user will be prompted to enter the speed limit. Second, the
user will be prompted to enter the recorded speed of the car.

Km/hr           Fine
1 to 20         $100
21 to 30        $270
31 or above     $500

Output Specification
If the driver is not speeding, the output should be:
Congratulations, you are within the speed limit!
If the driver is speeding, the output should be:
You are speeding and your fine is $F.

where F is the amount of the fine as described in the table above.


Sample Session 1 (with output shown in text, user input in italics)
Enter the speed limit: 40
Enter the recorded speed of the car: 39
Congratulations, you are within the speed limit!

Sample Session 2
Enter the speed limit: 100
Enter the recorded speed of the car: 131
You are speeding and your fine is $500.

Sample Session 3
Enter the speed limit: 100
Enter the recorded speed of the car: 120
You are speeding and your fine is $100.
"""
def speeding():
    limit = int(input("Enter the speed limit:"))
    speed = int(input("Enter the recorded speed of the car:"))
    overspeed = speed - limit
    if overspeed > 30:
        print("You are speeding and your fine is $500")
    elif 20 < overspeed < 31:
        print("You are speeding and your fine is $270")
    elif 1 < overspeed < 21:
        print("You are speeding and your fine is $100")
    else:
        print("Congratulations, you are within the speed limit!")