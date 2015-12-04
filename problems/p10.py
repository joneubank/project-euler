'''
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
----------------------------------------------------------------------
notes:
        max divisor you need to test to is sqrt of the number
        there are lots of primes at (n*10 000)+1
----------------------------------------------------------------------
output:
Found 148933 primes.
Answer: 142913828922
[Finished in 13.2s]
----------------------------------------------------------------------
message:
You are the 196532nd person to have solved this problem.

You have earned 1 new award:

Decathlete: Solve ten consecutive problems
'''
import math


def isPrime(num):
    # Do a check for even off the top, since this check is missed in loop below
    if(num % 2 == 0):
        return False
    testMax = int(math.sqrt(num))+1
    for x in range(3, testMax, 2):
        if num % x == 0:
            return False
    if num % 10000 == 1:
        print(num)
    return True


def primes(start, end):
    out = []

    low = start
    if low < 2 and end >= 2:
        low = 2

    if low >= 2:
        if low == 2:
            out.append(2)

        if (low % 2 == 0):
            low = low + 1

        out += [x for x in range(low, end+1, 2) if isPrime(x)]

    return out


if __name__ == '__main__':
    primeList = primes(0, 2000000)
    print("Found " + str(len(primeList)) + " primes.")
    print("Answer: " + str(sum(primeList)))
