'''
A palindromic number reads the same both ways. The largest palindrome made from
the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.

------------------------------------------

You are the 275660th person to have solved this problem.

Answer: 906609
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
