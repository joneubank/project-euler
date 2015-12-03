'''
Problem 15
Starting in the top left corner of a 2x2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.

----------------------------------------------------------------------
notes:
(0, 0) -> (20, 20) using only (1, 0) and (0, 1)
this is a counting puzzle, permutations

how many ways can you arrange N x's and N o's?

N = 1 : 2
    xo
    ox

N = 2 : 6
    xxoo
    xoxo
    xoox
    oxxo
    oxox
    ooxx

N = 3 :
    xxxooo (123)
    xxoxoo (124)
    xxooxo (125)
    xxooox (126)

    xoxxoo (134)
    xoxoxo (135)
    xoxoox (136)

    xooxxo (145)
    xooxox (146)

    xoooxx (156)


    oxxxoo (234)
    oxxoxo (235)
    oxxoox (236)

    oxoxxo (245)
    oxoxox (246)

    oxooxx (256)

    ooxxxo (345)
    ooxxox (346)

    ooxoxx (356)

    oooxxx (456)

    ... more but i see the pattern

    is arranging 3 things among 6 places
    is selecting 3 out of 6 things, combinations not permutations
    Triangle numbers: triangle(4) + triangle(3) + triangle(2) + 1

By looking at wiki to jog the memory:
there are x combinations of k items out of a set of n options:
x = n!/k!/(n-k)!

applied to this scenario, where there are N moves to make like in my examples:
x = (2N)!/N!/N!

so for 20:
x = 40!/20!/20!
----------------------------------------------------------------------
output:
Answer for 20: 137846528820
[Finished in 0.1s]
----------------------------------------------------------------------
message:

You are the 114824th person to have solved this problem.

'''
from math import factorial as F
if __name__ == '__main__':
    n = 20
    answer = F(2*n)/F(n)/F(n)
    print("Answer for " + str(n) + ": " + str(answer))
