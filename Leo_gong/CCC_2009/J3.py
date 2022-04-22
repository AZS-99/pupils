"""
Problem Description
A mobile cell service provider in Ottawa broadcasts an automated time standard to its mobile users that reflects the
local time at the user’s actual location in Canada. This ensures that text messages have a valid local time attached to
them.
For example, when it is 1420 in Ottawa on Tuesday February 24, 2009 (specified using military, 24 hour format), the
times across the country are shown in the table below:

Pacific Time        Mountain Time       Central Time        Eastern Time        Atlantic Time       Newfoundland Time
Victoria, BC        Edmonton, AB        Winnipeg, MB        Toronto, ON         Halifax, NS         St. John’s, NL
Tuesday             Tuesday             Tuesday             Tuesday             Tuesday             Tuesday
2/24/2009           2/24/2009           2/24/2009           2/24/2009           2/24/2009           2/24/2009
1120 PST            1220 MST            1320 CST            1420 EST            1520 AST            1550 Newfoundland ST

Write a program that accepts the time in Ottawa in 24 hour format and outputs the local time in each of the cities
listed above including Ottawa. You should assume that the input time will be valid (i.e., an integer between 0 and 2359
with the last two digits being between 00 and 59).
You should note that 2359 is one minute to midnight, midnight is 0, and 13 minutes after midnight is 13. You do not need
to print leading zeros, and input will not contain any extra leading zeros.


Sample Input
1300

Sample Output
1300 in Ottawa
1000 in Victoria
1100 in Edmonton
1200 in Winnipeg
1300 in Toronto
1400 in Halifax
1430 in St. John’s
"""
def mobile_cell_service():
    file = open("CCC_2009/J3", "r")
    ottawa = int(file.readline())
    victoria = ottawa - 300
    edmonton = ottawa - 200
    winnipeg = ottawa - 100
    toronto = ottawa
    halifax = ottawa + 100
    st_john = ottawa + 130

