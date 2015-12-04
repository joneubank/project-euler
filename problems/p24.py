'''
Problem 24

A permutation is an ordered arrangement of objects. For example, 3124 is one
possible permutation of the digits 1, 2, 3 and 4. If all of the permutations
are listed numerically or alphabetically, we call it lexicographic order. The
lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
    0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

----------------------------------------------------------------------
notes:

with 0 first we have 9! permutations of rest of the digits
knowing this, use division to find out what first number is
modulus of 9! from target number to get remaiinder
repeat process with second digit
----------------------------------------------------------------------
output:

Answer: 2783915460
[Finished in 0.1s]
----------------------------------------------------------------------
message:

'''
from math import factorial as F


def problem():
    options = range(0, 10, 1)
    target = 1000000
    remainder = target-1

    answer = []

    while len(options) > 0:
        length = len(options)
        permutations = F(length-1)

        choice = int(remainder / permutations)
        value = options[choice]

        answer.append(value)

        options.remove(value)

        remainder = remainder % permutations

    # first_remainder
    # second = int()

    output = ""
    for x in answer:
        output += str(x)

    return output


if __name__ == '__main__':
    print("Answer: " + str(problem()))
