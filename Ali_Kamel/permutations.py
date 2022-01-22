"""
Write a program that returns the permutations of a list/array of integers. You can assume that the input has to be at
least one integer.

Sample input:
1
2
3

Sample output (order is irrelevant):
[[3, 2, 1], [2, 1, 3], [1, 3, 2], [2, 3, 1], [3, 1, 2], [1, 2, 3]]

You can use any basic built-in container of your choice. Using libraries is not allowed.
"""

def getPermutations(nums: list):
    if len(nums) == 1:
        return [nums]
    else:
        perms1 = getPermutations(nums[1:])
        firstDigit = nums[0]
        perms2 = []
        for perm in perms1:
            for i in range(0,len(perm)+1):
                perms2.append(perm[0:i]+[firstDigit]+perm[i:])
        return perms2

