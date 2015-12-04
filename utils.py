import math


'''
getFileLines(filename)
return: array of the text of each line in the file that is specified
input:
        filename - relative path and filename of file to read
First used: p11
'''
def getFileLines(filename):

    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]

    return lines


'''
arrayProduct(array)
return: numeric value of product of every element in the input
input:
        array - iterable, each item will be multiplied together. if the items
                are not numeric this will break
First Used: p8
'''
def arrayProduct(array):
    out = 1
    for char in array:
        out *= char
    return out


'''
fibSequence(a, b, cutoff, maxsteps = 1000)
return: array with all values in fibonnacci like sequence up to the cutoff value
input:
       a        - first number used in sequence
       b        - second number used in sequence
       cutoff   - output will include all fibonnacci terms that are less than
                  this cutoff values
       maxsteps - maximum number of iterations before method exits.
                  negative values indicate unlimited steps - Default is 1000


example: fibSequence(1, 1, 20) = [1, 1, 2, 3, 5, 8, 13]
note: infinite loops are possible if negatives are used without care
first use: p2
'''
def fibSequence(a, b, cutoff, maxsteps=1000):
    output = []

    # the output should always have the first two numbers, even if above the
    # cutoff value. if b is less than the cutoff it will be added in the first
    # loop, so only force add it here if it is larager than the cutoff
    output.append(a)
    if b > cutoff:
        output.append(b)

    lead = b
    tail = a

    count = 0
    while lead < cutoff:

        output.append(lead)

        temp = lead
        lead = lead + tail
        tail = temp


        # check steps against maximum, break if cap hit
        count += 1
        if (count >= maxsteps) and (maxsteps >= 0):
            break

    return output


'''
isPalindrome(testVal)
return: True if it is the same forward and backward, False otherwise
input:
        testVal - any object, the test will be applied to str(testVal)
                 in theory an object could be a palindrome in the right
                 circumstances, assuming the String representation of that
                 object is a palindrome

first use: p4
'''
def isPalindrome(testVal):
    # Ensure the input is a string
    testStr = str(testVal)
    reverse = testStr[::-1]

    # get the string length to test, can ignore middle char in odd length vals
    testLength = int(math.floor(len(testStr)/2))

    # Get the test values concatenated to testLength
    testStr = testStr[0:testLength]
    reverse = reverse[0:testLength]

    return testStr == reverse


'''
triangleNumber(num)
return: triangle number for the provided input natural number

First Used: p12
'''
def triangleNumber(num):
    return sum([x for x in range(1, num+1, 1)])


'''
get_factors(num)
return: set (not array) with all factors of the input num

First Used: p12
'''
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


'''
isPrime(num)
return: True if num is Prime, False otherwise
input:
        num - integer to check if is prime

todo: input validation as positive integer
first use: p7
'''
def isPrime(num):
    # Do a check for even off the top, since this check is missed in loop below
    if(num % 2 == 0):
        return False
    testMax = int(math.sqrt(num))
    for x in range(3, testMax, 1):
        if num % x == 0:
            return False
    return True


'''
primeFactors(num)
return: array of all prime factors, including duplicates, ordered ascending
input:
        num - number to find the prime factors of. non integer values will
                likely cause errors

first use: p3
'''
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


'''
primes(start, end):
return: array with all prime numbers between low and high, inclusive
inputs:
        start - start of range to check for primes. will be included if it is a
                prime number
        end   - end of range to check for primes. will be included if it is a
                prime number

first use: p10
'''
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


'''
commonPrimeFactors(factorArrays)
returns: array with all shared values in the provided arrays, used for finding
           common prime factor sets
inputs:
        factorArrays - iterable of iterables (array of arrays): [[2,2,3], [2,5]]

note: this isn't actually doing prime or factor checking, just combining the
        distinct values of a set of arrays into an output
first used: p5
'''
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


'''
Convert letters to numbers based on alphabet position
'''
def string_to_number(string):
    return sum([letter_as_number(x) for x in string])


def letter_as_number(letter):
    return ord(letter.lower())-96

if __name__ == '__main__':
    out = primes(5, 15)

    print(str(out))
