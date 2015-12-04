'''
Problem 20

n! means n x (n-1) x (n-2) x ... x (n-1) x 1

For example, 10! = 10 x 9 x ... x 3 x 2 x 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

----------------------------------------------------------------------
notes:
        Super easy, cause python handles large factorials

        got level 1 message on completion. Completed this after finishing rest
        of first 25
----------------------------------------------------------------------
output:

Answer: 648
[Finished in 0.1s]
----------------------------------------------------------------------
message:

You are the 127190th person to have solved this problem.

Nice work, joneubank, you've just advanced to Level 1 .
77431 members (14.11%) have made it this far.

You have earned 2 new awards:

The Journey Begins: Progress to Level 1 by solving twenty-five problems
Easy Prey: Solve twenty-five of the fifty easiest problems

'''
from math import factorial as F

def problem():
    return sum([int(x) for x in str(F(100))])


if __name__ == '__main__':
    print("Answer: " + str(problem()))

