'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that
    the 6th prime is 13.

What is the 10 001st prime number?
-----------------------------------------------------------
note: This implementation is purely brute force. only optimization is skipping
        prime test on even numbers.
      It is extra slow due to a print line at ever new prime found.

-----------------------------------------------------------
You are the 248017th person to have solved this problem.

run time: 31.3s
Answer: 104743
'''
import math

# from utils:
def isPrime(num):
    # Do a check for even off the top, since this check is missed in loop below
    if(num % 2 == 0):
        return False
    halfNum = int(math.floor(num))
    for x in range(3, halfNum, 2):
        if num % x == 0:
            return False
    return True

if __name__ == '__main__':
    out = [2, 3]
    test = 3
    while len(out) < 10001:
        test += 2
        if isPrime(test):
            out.append(test)
            print("Found Prime #" + str(len(out)) + ": " + str(test))

