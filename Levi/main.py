


from loops import n_squared
from loops import prime_factors
from loops import big_number
if __name__ == '__main__':

    numbers = []
    value = 1
    while value != 0:
        value = int(input("Enter a number: (0: For end of input): "))
        numbers.append(value)

    n, count = big_number(numbers)
    print("The largest number is", n, "The occurence count of the largest number is", count)















