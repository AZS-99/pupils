"""
Problem J2: Old Fishin’ Hole
Problem Description

Fishing habitat and fish species are a resource that must be carefully managed to ensure that they will be there for the
future. Accordingly, fishing limits have been established for a particular river based on the population of each
species. Specifically, points are associated with the fish caught and the total points you catch must be less than or
equal to the points allowed for that river.

As an example, suppose each brown trout counts as 2 points, each northern pike counts as 5 points and each yellow
pickerel counts as 2 points, and the total points allowed must be less than or equal to 12. One acceptable catch could
consist of 3 brown trout and 1 northern pike, but, other combinations would also be allowed.
Your job is to write a program to input the points allocated for a river, and find how many different ways an angler who
catches at least one fish can stay within his/her limit.

Input Description
You will be given 4 integers, one per line, representing trout points, pike points, pickerel points, and total points
allowed in that order.
You can assume that each integer will be greater than 0 and less than or equal to 100.

Output Description
For each different combination of fish caught, output the combination of brown trout, northern pike, and yellow pickerel
in that order. The combinations may be listed in any order. The last line of output should display the total number of
unique ways to catch fish within the established limit.

Sample Input
1
2
3
2

Sample Output
1 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
2 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
0 Brown Trout, 1 Northern Pike, 0 Yellow Pickerel
Number of ways to catch fish: 3
"""
def old_fishin_hole():
    file = open("CCC_2009/J2", "r")
    brown_trout, northern_pike, yellow_pickerel, total_points = int(file.readline()), int(file.readline()), \
                                                                int(file.readline()), int(file.readline())
    num_bt = total_points // brown_trout
    num_np = total_points // northern_pike
    num_yp = total_points // yellow_pickerel
    num_bt_np = total_points // (brown_trout + northern_pike)
    num_bt_yp = total_points // (brown_trout + yellow_pickerel)
    num_np_yp = total_points // (northern_pike + yellow_pickerel)
    num_three = total_points // (brown_trout + northern_pike + yellow_pickerel)

    for i in range(num_bt):
        print(i + 1, "Brown Trout, 0 Northern Pike, 0 Yellow Pickerel")

    for i in range(num_np):
        print("0 Brown Trout,", i + 1, "Northern Pike, 0 Yellow Pickerel")

    for i in range(num_yp):
        print("1 Brown Trout, 0 Northern Pike,", i + 1, "Yellow Pickerel")

    for i in range(num_bt_np):
        print(i, "Brown Trout,", i + 1, "Northern Pike, 0 Yellow Pickerel")

    for i in range(num_bt_yp):
        print(i, "Brown Trout, 0 Northern Pike,", i + 1, "Yellow Pickerel")

    for i in range(num_np_yp):
        print("0 Brown Trout,", i + 1, "Northern Pike,", i + 1, "Yellow Pickerel")

    for i in range(num_three):
        print(i, "Brown Trout,", i + 1, "Northern Pike,", i + 1, "Yellow Pickerel")

    print("Number of ways to catch fish:", num_bt + num_np + num_yp + num_bt_np + num_bt_yp + num_np_yp + num_three)