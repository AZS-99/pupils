
import loops
import advanced_fns

if __name__ == '__main__':
    arg = [int(x) for x in input("Enter 2 numbers, the investment, and the interest rate: ").split(", ")]
    advanced_fns.printInvestment(arg[0],(arg[1]/12)/100)
    #order = advanced_fns.displaySortedNumbers(arg[0], arg[1], arg[2])

    # advanced_fns.displaySortedNumbers(int(input("Enter 3 numbers:"))))




