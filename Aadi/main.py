import math



if __name__ == '__main__':
    side_length_1=int(input("Please enter the side length for rectangle one"))
    side_width_1 = int(input("Please enter the side width for rectangle one"))
    perimeter_1 = side_length_1 * 2 +  side_width_1 * 2
    area_1 = side_length_1 * side_width_1

    side_length_2 = int(input("Please enter the side length for rectangle two"))
    side_width_2 = int(input("Please enter the side width for rectangle two"))
    perimeter_2 = side_length_2 * 2 + side_width_2 * 2
    area_2 = side_length_2 * side_width_2

    if perimeter_1 > perimeter_2:
        if area_1 > area_2:
            print("rectangle one is bigger")
        else:
            print("rectangle on is bigger in perimeter but smaller in area")
    else:
        if area_1 < area_2:
            print("rectangle two is bigger")
        else:
            print("rectangle two is bigger in perimeter but smaller in area")


