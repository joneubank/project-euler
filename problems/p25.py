'''
Problem 25

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain
1000 digits?

----------------------------------------------------------------------
notes:
        easy since we already have a fibonacci sequence method with cutoffs
        number with 1000 digits is 10**999
----------------------------------------------------------------------
output:
Answer: 4782
[Finished in 0.1s]
----------------------------------------------------------------------
message:
You are the 98369th person to have solved this problem.
'''


def fibonacci(a, b, cutoff, maxsteps=-1):
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

def problem():
    return len(fibonacci(1, 1, 10**999)) + 1


if __name__ == '__main__':
    print("Answer: " + str(problem()))
