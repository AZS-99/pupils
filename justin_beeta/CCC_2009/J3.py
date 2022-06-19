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
def convert_to_mins(hrs, mins):
    return hrs * 60 + mins

def convert_to_clock(mins):
    return mins // 60, mins % 60


def time_in_different_areas():
    file = open("CCC_2009/J3", 'r')
    time_str = file.readline()
    hrs = int(time_str[0:2])
    mins = int(time_str[2:])
    time_ottawa = convert_to_mins(hrs, mins)
    print(time_str, "in Ottawa")
    victoria_diff = convert_to_mins(3, 0)
    time_victoria = time_ottawa - victoria_diff
    hrs_victoria, mins_victoria = convert_to_clock(time_victoria)
    print("{:02d}".format(hrs_victoria) + "{:02d}".format(mins_victoria), "in Victoria")

    edmonton_diff = convert_to_mins(2, 0)
    time_edmonton = time_ottawa - edmonton_diff
    hrs_edmonton, mins_edmonton = convert_to_clock(time_edmonton)
    print("{:02d}".format(hrs_edmonton) + "{:02d}".format(mins_edmonton), "in Edmonton")

    winnipeg_diff = convert_to_mins(1, 0)
    time_winnipeg = time_ottawa - winnipeg_diff
    hrs_winnipeg, mins_winnipeg = convert_to_clock(time_winnipeg)
    print("{:02d}".format(hrs_winnipeg) + "{:02d}".format(mins_winnipeg), "in Winnipeg")

    print(time_str, "in Toronto")

    halifax_diff = convert_to_mins(1, 0)
    time_halifax = time_ottawa + halifax_diff
    hrs_halifax, mins_halifax = convert_to_clock(time_halifax)
    print("{:02d}".format(hrs_halifax) + "{:02d}".format(mins_halifax), "in Halifax")

    stjohn_diff = convert_to_mins(1, 30)
    time_stjohn = time_ottawa + stjohn_diff
    hrs_stjohn, mins_stjohn = convert_to_clock(time_stjohn)
    print("{:02d}".format(hrs_stjohn) + "{:02d}".format(mins_stjohn), "in St. John's")




