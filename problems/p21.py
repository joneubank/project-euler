'''
Problem 21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n
    which divide evenly into n).
If d(a) = b and d(b) = a, where a != b, then a and b are an amicable pair and
each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55
and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71
and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

----------------------------------------------------------------------
notes:
        use getFactors and remove itself from response
----------------------------------------------------------------------
output:

Amicables: set([1184, 6368, 220, 5020, 2924, 6232, 1210, 5564, 284, 2620])
Answer: 31626
[Finished in 0.2s]
----------------------------------------------------------------------
message:
You are the 91119th person to have solved this problem.
'''
import math


# from utils
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


def problem():
    amicables = set()

    factor_sums = [sum(get_factors(x))-x for x in range(0, 10000, 1)]

    check_len = len(factor_sums)
    for a, a_sum in enumerate(factor_sums):
        if a_sum < check_len and a != a_sum:
            if factor_sums[a_sum] == a:
                print("Found: " + str(a) + " - " + str(a_sum))
                amicables.add(a)
                amicables.add(a_sum)
    print("Amicables: " + str(amicables))
    return sum(amicables)


if __name__ == '__main__':

    answer = problem()

    print("Answer: " + str(answer))
