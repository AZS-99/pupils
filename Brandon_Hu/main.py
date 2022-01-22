import math

from manipulating_input import warming_water
from manipulating_input import root

if __name__ == '__main__':
    a, b, c = input("enter a, b, c:").split(', ')
    a = float(a)
    b = float(b)
    c = float(c)
    a, b = root(a, b, c)

    if a != float('inf') and b != float('inf'):
        print("The roots are", a,  "and", b)
    elif a != float('inf') and b  == float('inf'):
        print("the root is",a)
    else:
        print("the equatia has no real roots")

