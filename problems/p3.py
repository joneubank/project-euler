'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

------------------------------------------
You are the 305917th person to have solved this problem.

You have earned 1 new award:

Baby Steps: Solve three problems

Added Factor: 6857
[71, 839, 1471, 6857]
[Finished in 0.1s]
'''


def primeFactors(num):
    primeFactors = []
    low = 2
    high = num
    while low <= high:
        print("Testing: " + str(low))

        if high % low == 0:
            high = high/low
            primeFactors.append(low)
            print("Added Factor: " + str(low))
        else:
            low = low + 1

    return primeFactors

if __name__ == '__main__':
    primes = primeFactors(600851475143)
    print(primes)
