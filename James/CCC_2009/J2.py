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

Sample Output
1 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
2 Brown Trout, 0 Northern Pike, 0 Yellow Pickerel
0 Brown Trout, 1 Northern Pike, 0 Yellow Pickerel
Number of ways to catch fish: 3
"""
def fishing():
    file = open("CCC_2009/J2", "r")
    bt = int(file.readline())
    np = int(file.readline())
    yp = int(file.readline())
    point_limit = int(file.readline())
    max_b = point_limit // bt
    max_n = point_limit // np
    max_y = point_limit // yp

    ways = 0

    for b in range(max_b + 1):
        for n in range(max_n + 1):
            for y in range(max_y + 1):
                if 0 < b * bt + n * np + y * yp <= point_limit:
                    print(b, "Brown Trout,", n, "Northern Pike,", y, "Yellow Pickerel")
                    ways += 1
    print("Number of ways to catch fish:", ways)

    # if max_b != 0:
    #     for i in range(max_b):
    #         if max_b * bt <= point_limit:
    #             ways += 1
    #
    # if max_y and max_n != 0:
    #     for i in range(max_y):
    #         for i in range(max_n):
    #             if max_y * yp + max_n * np <= point_limit:
    #                 ways += 1

