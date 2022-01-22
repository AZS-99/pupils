from Revision import compare


if __name__ == "__main__":
   weight_1, price_1 = input("Enter weight and price package 1:").split(', ')
   weight_2, price_2 = input("Enter weight and price package 2:").split(', ')
   weight_1 = float(weight_1)
   weight_2 = float(weight_2)
   price_1 = float(weight_1)
   price_2 = float(weight_2)
   print(compare(weight_1, price_1, weight_2, price_2))










