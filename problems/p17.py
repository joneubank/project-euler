'''
Problem 17
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?


NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
    forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
    20 letters. The use of "and" when writing out numbers is in compliance
    with British usage.
----------------------------------------------------------------------
notes:
Inspired to write a complete number to english word translation script, so
    spent time to create one that handles numbers from positive to negative
    decillions

This wasn't needed for this problem, but it is nice to have. Will only handle
integers so far.
----------------------------------------------------------------------
output:
Answer: 21124
[Finished in 0.1s]
----------------------------------------------------------------------
message:

You are the 94265th person to have solved this problem.
'''
import re


def unitToWord(num):
    if num == 1:
        return "one"
    elif num == 2:
        return "two"
    elif num == 3:
        return "three"
    elif num == 4:
        return "four"
    elif num == 5:
        return "five"
    elif num == 6:
        return "six"
    elif num == 7:
        return "seven"
    elif num == 8:
        return "eight"
    elif num == 9:
        return "nine"
    elif num == 0:
        return "zero"
    return


def tensToWord(num):
    # units
    if num < 10:
        return unitToWord(num)

    # tens
    elif num < 20:
        if num == 10:
            return "ten"
        elif num == 11:
            return "eleven"
        elif num == 12:
            return "twelve"
        elif num == 13:
            return "thirteen"
        elif num == 15:
            return "fifteen"
        elif num == 18:
            return "eighteen"
        else:
            return unitToWord(num%10) + "teen"

    # 20+
    else:
        # units
        units = num % 10
        if units == 0:
            unitText = ""
        else:
            unitText = "-" + unitToWord(units)

        #tens
        tens = num % 100 - units
        if tens == 20:
            tensText = "twenty"
        elif tens == 30:
            tensText = "thirty"
        elif tens == 40:
            tensText = "forty"
        elif tens == 50:
            tensText = "fifty"
        elif tens == 80:
            tensText = "eighty"
        else:
            tensText = unitToWord(tens/10) + "ty"

        return tensText + unitText


def hundredsToWord(num):
    if num < 100:
        return tensToWord(num)
    else:
        # tens
        tens = num%100
        tensText = ""
        if tens != 0:
            tensText = " and " + tensToWord(tens)

        #hundreds
        hundreds = (num - tens)/100
        hundredsText = unitToWord(hundreds)+" hundred"

        return hundredsText + tensText


def numToWord(num):
    PREFIXES = {
        2:"m",
        3:"b",
        4:"tr",
        5:"quadr",
        6:"quint",
        7:"sext",
        8:"sept",
        9:"oct",
        10:"non",
        11:"dec",
    }

    out = ""

    formatted = int(num)

    numArray = str(formatted)

    # Handle negative values
    if formatted < 0:
        out += "negative "
        numArray = numArray[1:]

    length = len(numArray)
    orders = int((length-1)/3)

    for order in range(orders, -1, -1):
        blockStart = -3*(order+1)
        blockEnd = -3*order

        if blockEnd == 0:
            block = int(numArray[-3:])
        else:
            block = int(numArray[blockStart:blockEnd])

        if block != 0 or orders == 0:
            hundredsText = hundredsToWord(block)

            ordersText = ""

            if order in PREFIXES:
                ordersText = " " + PREFIXES[order] + "illion"
            elif order == 1:
                ordersText = " thousand"

            blockText = ""
            if order == 0:
                # last two characters are for padding
                if block < 100 and orders > 0:
                    out = out[:-2]
                    blockText += " and "
                blockText += hundredsText + "  "
            else:
                blockText += hundredsText + ordersText + ", "

            out += blockText

    out = out[:-2]
    return out



if __name__ == '__main__':

    total = 0
    for num in range(1,1001,1):
        text = numToWord(num)
        stripped = re.sub('[^a-z]','',text)
        print(stripped)
        total += len(stripped)


    print(str(total))
