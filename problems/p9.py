'''
Problem 9
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
----------------------------------------------------------------------
notes:
    Details below but conclusion is:
    * loop a from 1 to 333
    * for each a value, calculate b using formula:
        b = (1000000 - 2000a) / (2a + 2000)
    * if b is an integer that is the solution
    * calculate c:
        c = 1000 - a - b

    Constraints
    0 < a <= b < c

    Min max for each:
    c:
        max = 998 (a=1, b=1)
        min = 334 (a=333, b=333) - any lower and there is no way to sum to 1000
    b:
        min = 1
        max = 499 - min and less than c (a=1, c=500)
    a:
        min = 1
        max = 333 - cannot be greater than b or c

    a + b + c = 1000
1:  c = 1000 - a - b
    a^2 + b^2 - c^2 = 0
    sub in 1:
2:  a^2 + b^2 - (1000 - a - b)^2 = 0

    expand: (1000 - a - b)^2
    = 1000000 - 1000a - 1000b - 1000a + a*a + a*b - 1000b + a*b + b*b
3:  = 1000000 - 2000a - 2000b + 2ab + a^2 + b^2

    sub 3 into 2:
    a^2 + b^2 - (1000000 - 2000a - 2000b + 2ab + a^2 + b^2) = 0
    -2ab + 2000a + 2000b - 1000000 = 0

    isolate b:
    b(2000 - 2a) + 2000a - 1000000 = 0
4:  b = (1000000 - 2000a) / (2000 - 2a)
----------------------------------------------------------------------
Solution Found: (200, 375, 425)
Answer: 31875000
[Finished in 0.1s]
----------------------------------------------------------------------
You are the 214013th person to have solved this problem.
'''

if __name__ == '__main__':
    out = []
    for a in range(1,333,1):
        b = (1000000 - 2000*a) / (2000 - 2.0*a)
        if (b % 1.0 == 0):
            b = int(b)
            c = 1000 - a - b
            print("Solution Found: (" + str(a) + ", " + str(b) + ", " + str(c) + ")")
            out = [a, b, c]
            break
        else:
            print("Fail: a=" + str(a) + " b=" + str(b))
    prod = out[0]*out[1]*out[2]
    print("Answer: " + str(prod))
