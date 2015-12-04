'''
Problem 19
You are given the following information, but you may prefer to do some research
for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century
    unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century
    (1 Jan 1901 to 31 Dec 2000)?

----------------------------------------------------------------------
notes:
        this is a really annoying problem. not hard just tedius.
----------------------------------------------------------------------
output:

----------------------------------------------------------------------
message:
You are the 84750th person to have solved this problem.
'''

MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAY_ONES = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
DAY_ONES_LEAP = [0, 31, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]


def problem():
    year = 1900
    day = -1
    count = 0

    while year < 2001:
        year_days = 365
        check_days = DAY_ONES

        if year % 4 == 0:
            year_days = 366
            check_days = DAY_ONES_LEAP

        while day < year_days:
            if year > 1900:
                if day in check_days:
                    count += 1

            day += 7


        day = day % year_days
        year += 1

    return count


if __name__ == '__main__':
    answer = problem()
    print("Answer: " + str(answer))
