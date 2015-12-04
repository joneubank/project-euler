'''
Problem 22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file
containing over five-thousand first names, begin by sorting it into
alphabetical order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which
 is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
 COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

----------------------------------------------------------------------
notes:
        use python to sort
        write some ridiculous convoluted single lines that are unreadable
----------------------------------------------------------------------
output:

Answer: 871198282
[Finished in 0.1s]
----------------------------------------------------------------------
message:
You are the 84619th person to have solved this problem.
'''

'''
string_to_number(string)

is really only intended for alpha input, symbols and numbers
    may not have the intended result (or maybe they will)

'''


def get_file_lines(filename):

    with open(filename) as f:
        lines = [line.rstrip('\n') for line in f]

    return lines


def string_to_number(string):
    return sum([letter_as_number(x) for x in string])


def letter_as_number(letter):
    return ord(letter.lower())-96


def problem():
    data = [x.replace("\"", "")
            for x in sorted(get_file_lines("input/i22.py")[0].split(","))]

    return sum([(index + 1) * string_to_number(name)
                for index, name in enumerate(data)])


if __name__ == '__main__':
    print("Answer: " + str(problem()))
