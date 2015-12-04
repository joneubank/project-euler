'''
Problem 26

A unit fraction contains 1 in the numerator. The decimal representation of the
unit fractions with denominators 2 to 10 are given:

1/2  =   0.5
1/3  =   0.(3)
1/4  =   0.25
1/5  =   0.2
1/6  =   0.1(6)
1/7  =   0.(142857)
1/8  =   0.125
1/9  =   0.(1)
1/10 =   0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be
seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle
in its decimal fraction part.

----------------------------------------------------------------------
notes:
        getting the correct logic to find repeating decimal patterns
        was somewhat tricky, had to find a matching pattern then reduce

        once the repeat patterns could be identified another problem was
        found where the length of the pattern became very long, and to find a
        pattern you need a number of decimals equal to twice the length of the
        pattern. the final answer is just under 1000 characters long, so
        it wasn't even identified til the decimal precision was raised to 2000.
        From 2000, I raised to 5000 to make sure nothing more was missed.
        Still can't be sure, but am fairly confident this will take care of
        finding the longest repeating string for 1/d with d < 1000

        I guess this is the brute force method, get every answer, check for
        pattern, select the longest. writing the "find repeating pattern" code
        was very rewarding though, so, worth it.

        For interest, there is commented out code in the main block to
        calculate the longest pattern
----------------------------------------------------------------------
output:

Max repeated lenght: 982
Answer: 983
[Finished in 11.6s]

----------------------------------------------------------------------
message:

You are the 52281st person to have solved this problem.
'''
from decimal import Decimal
import decimal
import re
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


def find_repeating_decimal(num):

    def reduce_pattern(pattern):
        #
        candidate = pattern

        length = len(pattern)
        for i in sorted(list(get_factors(length))):
            # print("i: " + str(i))
            a = pattern[:i]
            # print("a: " + a)
            match_found = True

            # check that this matches ALL remaining strings of this length in
            # the pattern
            for j in range(i, length, i):
                b = pattern[j:j+i]
                # print("b: " + b)
                if a != b:
                    match_found = False
                    break

            if match_found:
                candidate = a
                break

        return candidate

    string = str(num)
    string = re.sub("^.*[.]", "", string)
    candidate_answer = None

    length = len(string)
    length_max = length / 2 + 1
    for i in range(length_max, 0, -1):
        for start in range(0, length - 2*i + 1, 1):
            a = string[start:start+i]
            b = string[start+i:start+i+i]
            # print(a + " : " + b)
            if a == b:
                return reduce_pattern(a)

def problem():

    data = [Decimal(1) / Decimal(d) for d in range(1, 1000, 1)]
    patterns = [find_repeating_decimal(x) for x in data]

    top = 0
    top_index = None
    for i, x in enumerate(patterns):
        if x:
            length = len(x)
            if length > top:
                top = length
                top_index = i+1
                print(str(top_index) + " : " + str(top))

    print("Max repeated lenght: " + str(top))
    return top_index
    # return Decimal(1)/Decimal(3)


if __name__ == '__main__':
    decimal.getcontext().prec = 5000

    print("Answer: " + str(problem()))

    # a = Decimal(1) / Decimal(983)
    # print(a)
    # repeat = find_repeating_decimal(a)
    # print(repeat)
    # print(len(repeat))
