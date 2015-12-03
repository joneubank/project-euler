'''
Problem 14
The following iterative sequence is defined for the set of positive integers:

n -> n/2 (n is even)
n -> 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

----------------------------------------------------------------------
notes:
        should be able to reduce number of loops by identifying common patterns
            that lead to short chains
----------------------------------------------------------------------
output:
Longest Start was 837799 with 525 steps
Answer: 837799
[Finished in 39.6s]
----------------------------------------------------------------------
message:
You are the 137971st person to have solved this problem.
'''
def collatzSequence(num):
    current = num
    out = [current]
    while current != 1:
        if current % 2 == 0:
            current = current/2
        else:
            current = current*3 + 1
        out.append(current)

    return out


if __name__ == '__main__':
    top = 0
    topStart = None
    for i in range(1, 1000000, 1):
        seq = collatzSequence(i)
        seqLength = len(seq)
        if seqLength > top:
            top = seqLength
            topStart = i
            print(str(i) + ": " + str(seqLength) )

    print("Longest Start was " + str(topStart) + " with " + str(top) + " steps")
    print("Answer: " + str(topStart) )
