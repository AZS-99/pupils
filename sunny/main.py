from Revision import find_sides


if __name__ == "__main__":
   x1, y1, x2, y2, x3, y3 = input("Enter three points for a triangle: ").split(", ")
   x1 = float(x1)
   y1 = float(y1)
   x2 = float(x2)
   y2 = float(y2)
   x3 = float(x3)
   y3 = float(y3)
   print(find_sides(x1, y1, x2, y2, x3, y3))









