from arithmetics import better_price
if __name__ == '__main__':
    weight1, price1 = input("Enter weight and price for package 1:").split(", ")
    weight2, price2 = input("Enter weight and price for package 2:").split(", ")
    weight1 = int(weight1)
    weight2 = int(weight2)
    price1 = float(price1)
    price2 = float(price2)
    wic_ones_bettr = better_price(weight1,price1,weight2,price2)
    print("Package",wic_ones_bettr,"has the better price.")