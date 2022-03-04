from classes import Account
import advanced_fns
from advanced_fns import  craps

if __name__ == '__main__':
    # arg = [int(x) for x in input("Enter ch1 ch2 and numbers per line: ").split(", ")]
    acc = Account(1122, 20000, 0.045)
    acc.withdraw(2500)
    acc.deposit(3000)
    print(acc.id, acc.balance, acc.getMonthlyInterestRate(), acc.getMonthlyInterest())
    # advanced_fns.displaySortedNumbers(int(input("Enter 3 numbers:"))))




