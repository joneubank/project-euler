'''
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

--------------------------------------------------------

You are the 516922nd person to have solved this problem.

Answer: 233168
[Finished in 0.1s]
'''


def sumOfMultiples(num, multiples):
    total = 0

    for i in xrange(num):
        isMultiple = False
        for j in multiples:
            if(i % j == 0):
                isMultiple = True
                break
        if isMultiple:
            total += i

    return total

if __name__ == '__main__':
    total = sumOfMultiples(1000, [3, 5])
    print(total)
