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


def car_speed_check():
    speed_limit = int(input("Enter the speed limit: "))
    speed = int(input("Enter the recorded speed of the car: "))
    if speed <= speed_limit:
        print('Congratulations, you are within the speed limit!')
    else:
        over_speed = speed - speed_limit
        fine = 0
        if over_speed < 21:
            fine = 100
        elif over_speed < 31:
            fine = 270
        else:
            fine = 500
        print('You are speeding and your fine is $' + str(fine) + '.')
