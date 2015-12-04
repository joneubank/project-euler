'''
Problem 13

Work out the first ten digits of the sum of the following one-hundred 50-digit
numbers.

input: input/i13.txt
----------------------------------------------------------------------
notes:
        Probably are useful tricks to do this but for this puzzle there is
            no reason not to brute force it
----------------------------------------------------------------------
output:
Sum: 5537376230390876637302048746832985971773659831892672
Answer: 5537376230
[Finished in 0.1s]
----------------------------------------------------------------------
message:

You are the 139717th person to have solved this problem.
'''


def getFileLines(filename):

    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]

    return lines


if __name__ == '__main__':

    answer = 0
    for line in getFileLines("input/i13.txt"):
        answer += int(line)
    print("Sum: " + str(answer))
    print("Answer: " + str(answer)[0:10:1])
