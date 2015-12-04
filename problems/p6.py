'''
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural
    numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.
-----------------------------------------------------------
note:
square of sums equal to sum of cubes - proven via induction but can be quickly
    discovered through mental check
so what is being calculated is sum of n*n*(n-1)
-----------------------------------------------------------

You are the 289439th person to have solved this problem.

Total: 25164150
[Finished in 0.1s]
'''

if __name__ == '__main__':
    out = 0
    for x in range(1, 101, 1):
        print(x)
        out += x*x*(x-1)
    print("Total: " + str(out))
