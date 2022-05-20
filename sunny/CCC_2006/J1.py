"""
Problem Description
At Chip’s Fast Food emporium there is a very simple menu. Each food item is selected by entering a digit choice.
Here are the three burger choices:

1 – Cheeseburger (461 Calories)
2 – Fish Burger (431 Calories)
3 – Veggie Burger (420 Calories)
4 – no burger

Here are the three drink choices:
1 – Soft Drink ( 130 Calories)
2 – Orange Juice (160 Calories)
3 – Milk (118 Calories)
4 – no drink

Here are the three side order choices:
1 – Fries (100 Calories)
2 – Baked Potato (57 Calories)
3 – Chef Salad (70 Calories)
4 – no side order

Here are the three dessert choices:
1 – Apple Pie (167 Calories)
2 – Sundae (266 Calories)
3 – Fruit Cup (75 Calories)
4 – no dessert

Input Specifications
The program should prompt the user for a number for each type of item then calculate and display the Calorie total.
You may assume that each input will be a number from 1 to 4. That is, each customer has to pick exactly one number from
each of the four options out of each of the four categories.

Output Specifications
The program prints out on the screen the total Calories of the selected meal, and stops executing after this output.

Sample Prompting and User Input (user input in italics) Welcome to Chip’s Fast Food Emporium
Please enter a burger choice: 2
Please enter a side order choice: 1
Please enter a drink choice: 3
Please enter a dessert choice: 4
Output for the Sample
Your total Calorie count is 649.
"""

def sample_input():
    burger_choice = int(input("Please enter a burger choice: "))

    side_order_choice = int(input("Please enter a side order choice: "))
    drink_choice = int(input("Please enter a drink choice: "))
    dessert_choice = int(input("Please enter a dessert choice: "))

    total_calories = 0


    burger_dic = {1: 461, 2: 431, 3: 420, 4: 0}
    total_calories += burger_dic[burger_choice]

    side_order_dic = {1: 100, 2: 57, 3: 70, 4: 0}
    total_calories += side_order_dic[side_order_choice]

    drink_dic = {1: 130, 2: 160, 3: 118, 4: 0}
    total_calories += drink_dic[drink_choice]



    dessert_dic = {1: 167, 2: 266, 3: 75, 4: 0}
    total_calories += dessert_dic[dessert_choice]

    return total_calories





