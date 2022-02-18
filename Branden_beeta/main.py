from arithmetics import future_inv

if __name__ == '__main__':
    amount = int(input("Enter investment amount:"))
    rate = float(input("Enter annual interest rate:"))
    years = int(input("Enter number of years:"))
    fuInvestValue = future_inv(amount, rate, years)
    print("Accumulated value is", fuInvestValue)
