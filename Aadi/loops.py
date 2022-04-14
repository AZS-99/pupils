"""
Write a for loop that prints all the numbers between 1 and 15 inclusive.
"""
def numbers():
    for i in range(1, 15):
        print(i)


"""
Write a function that prints the squares of all integers between 1 to 50 exclusive. 
"""
def squares():
    for i in range(2,50):
        print(i**2)


"""
Write a programme that prompts the user to enter an integer, then prints the cubes of all numbers between 1 and the
specified number inclusive. 
"""

def cubes(value):
    for i in range (1,value+1):
        print(i**3)
