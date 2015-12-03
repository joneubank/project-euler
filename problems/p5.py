'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

-----------------------------------------------------------
Note: lowest common multiple is the product of the set of prime factors for the
        set of numbers.
      Example: for 4, 5, 6, prime factors are (2,2,3,5).
                4 is (2,2) and 6 is (2,3) but we only keep two 2's in our final
                since this is the highest for one number.
                result is 60 (4, 5, 6)
-----------------------------------------------------------

You are the 287523rd person to have solved this problem.

Answer: 232792560
'''

# primeFactors from utils
def primeFactors(num):
    primeFactors = []
    low = 2
    high = num
    while low <= high:
        if high % low == 0:
            high = high/low
            primeFactors.append(low)
        else:
            low = low + 1

    return primeFactors

def commonPrimeFactors(factorArrays):
    # dict to keep record from each set, will build full set from this
    commonFactors = []

    for array in factorArrays:
        unique = list(set(array))
        for factor in unique:
            countInArray = array.count(factor)
            countInCommon = commonFactors.count(factor)

            for x in xrange(countInArray, countInCommon, -1):
                commonFactors.append(factor)

    return commonFactors


if __name__ == '__main__':
    start = 1
    end = 20

    factorArrays = []
    for x in xrange(start, end):
        factorArrays.append(primeFactors(x))

    commonFactors = commonPrimeFactors(factorArrays)
    print("Common Prime Factors: " + str(commonFactors))

    product = 1;
    for x in commonFactors:
        product *= x

    print("Lowest Common Multiple: " + str(product))
