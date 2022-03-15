import math
from conditionals import add_two_lists



if __name__ == '__main__':
        s = input("Enter max 5 integers separated by a comma: ").split(", ")
        x = input("Enter max 5 integers separated by a comma: ").split(", ")
        lst = [int(y) for y in s]
        lst1 = [int(v) for v in x]
        print(add_two_lists(lst, lst1))






















