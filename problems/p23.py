'''
Problem 23

A perfect number is a number for which the sum of its proper divisors is
exactly equal to the number. For example, the sum of the proper divisors of
28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than
n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
number that can be written as the sum of two abundant numbers is 24. By
mathematical analysis, it can be shown that all integers greater than 28123
can be written as the sum of two abundant numbers. However, this upper limit
cannot be reduced any further by analysis even though it is known that the
greatest number that cannot be expressed as the sum of two abundant numbers is
less than this limit.

Find the sum of all the positive integers which cannot be written as the sum
of two abundant numbers.

----------------------------------------------------------------------
notes:

----------------------------------------------------------------------
output:

Answer: 4179871
[Finished in 2.3s]
----------------------------------------------------------------------
message:
You are the 64306th person to have solved this problem.
'''
import math


def get_factors(num):
    out = set([1, num])

    interval = 2
    if num % 2 == 0:
        interval = 1
        out.add(2)
        out.add(num/2)

    test_max = int(math.sqrt(num)) + 1
    for i in range(3, test_max, interval):
        if num % i == 0:
            out.add(i)
            out.add(num/i)

    return out


def is_abundant(num):
    return (sum(get_factors(num)) - num) > num

def problem():
    abundants = set([x for x in range(1, 28123, 1) if is_abundant(x)])
    total = 0
    for num in range(28123, 0, -1):
        pair_found = False
        for x in abundants:
            if num-x in abundants:
                pair_found = True
                break
        if pair_found:
            continue
        else:
            total += num

    return total


if __name__ == '__main__':
    print("Answer: " + str(problem()))
