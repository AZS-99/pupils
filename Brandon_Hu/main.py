
from manipulating_input import months
if __name__ == '__main__':
    month, year = input("Enter month and year:").split(", ")
    month = int(month)
    year = int(year)

    print(months(month, year))




