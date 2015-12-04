'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

------------------------------------------

You are the 275660th person to have solved this problem.

Found Combinations: ['993x913=906609', '968x916=886688', '962x924=888888',
    '932x924=861168', '924x962=888888', '924x932=861168', '916x968=886688',
    '914x902=824428', '913x993=906609', '909x902=819918', '902x914=824428',
    '902x909=819918']
Max: 906609
[Finished in 0.1s]
'''
import math


def isPalindrome(testVal):
    # Ensure the input is a string
    testStr = str(testVal)
    reverse = testStr[::-1]

    # get the string length to test, can ignore middle char in odd length vals
    testLength = int(math.floor(len(testStr)/2))

    # Get the test values concatenated to testLength
    testStr = testStr[0:testLength]
    reverse = reverse[0:testLength]

    return testStr == reverse


def main():

    palindromes = []
    pText = []
    # going to attempt to find it within the 900's
    # while a > 900:
    for a in range(999, 900, -1):
        for b in range(999, 900, -1):
            test = a * b
            # print("testing: " + str(a) + "x" + str(b) + "=" + str(test))
            if isPalindrome(test):
                palindromes.append(test)
                text = str(a) + "x" + str(b) + "=" + str(test)
                pText.append(text)
                print("Found Palindrome: " + text)
            b = b-1
    largest = max(palindromes)
    print("Found Combinations: " + str(pText))
    print("Max: " + str(largest))


if __name__ == '__main__':
    main()
