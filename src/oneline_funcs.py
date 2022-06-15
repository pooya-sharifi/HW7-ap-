# def myfunc():
# 	return ...
from calendar import c
from re import A, I
from string import digits
from tkinter import Y
from unicodedata import digit
from numpy import product, size, sort
from pyrsistent import b


def adjacentElementsProduct(inputArray):
    # return max([product(inputArray[i], inputArray[i+1]) for i in range(0, len(inputArray)-1)])
    return max(
        [inputArray[i] * inputArray[i + 1] for i in range(0, len(inputArray) - 1)]
    )


adjacentElementsProduct([3, 6, -2, -5, 7, 3])


def allLongestStrings(inputArray):
    return [
        inputArray[i]
        for i in range(0, len(inputArray))
        if (
            len(inputArray[i])
            == (max(len(inputArray[i]) for i in range(0, len(inputArray))))
        )
    ]


def checkPalindrome(inputString):
    return [
        inputString[i] == inputString[len(inputString) - 1 - i]
        for i in range(0, len(inputString) - 1)
    ] == [True] * len(
        [
            True
            for i in range(0, len(inputString) - 1)
            if inputString[i] == inputString[len(inputString) - 1 - i]
        ]
    )


def commonCharacterCount(s1, s2):
    #     return [
    #         s1[i] for i in range(0, len(s1)) for j in range(0, len(s2)) if s1[i] == s2[j]
    #     ]

    # # return [
    # #     s2[j] for i in range(0, len(s1)) for j in range(0, len(s2)) if s1[i] == s2[j]
    # # ]
    print(
        sum([s2.count(a) for a in set([a for a in s1 for b in s2 if a == b])]),
        set([a for a in [a for a in s1 for b in s2 if a == b]]),
    )
    return sum(
        [min(s1.count(a), s2.count(a)) for a in set([a for a in s1 and s2])],
    )


d = commonCharacterCount("zzzz", "zzzzzzz")
# d = commonCharacterCount("aabcc", "adcaa")
print(d)
# def areSimilar(A, B):
#     # for i in range(0, len(A)):
#     #     for j in range(0, len(A)):
#     # A[1], A[2] = A[2], A[1]
#     # return A
#     # i = 1
#     # j = 2
#     # return ["".join(set(A[:i])), A[i], "".join(set(A[i + 1 : j])), A[j]]
#     # return [(A[:i], A[i], A[:j], A[j]) == B for i in range(0, len(A)) for j in range(0, len(A))]
#     return[A[i] for i in range(0,len(A))]


# d = areSimilar([1, 2, 3], [1, 2, 3])
# print(d)

# def palindromeRearranging(inputString):


def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [
        substitutionElem if inputArray[i] == elemToReplace else inputArray[i]
        for i in range(0, len(inputArray))
    ]


def evenDigitsOnly(n):
    return [
        True
        for i in range(0, len(str(n)))
        if (((n % (10 ** (i + 1))) // (10**i)) % 2 == 0)
    ] == [True] * len(str(n))


def alphabeticShift(inputString):
    return "".join(
        [
            chr(ord(inputString[i]) + 1) if inputString[i] != "z" else "a"
            for i in range(0, len(inputString))
        ]
    )


def firstDigit(inputString):
    return int(
        [
            inputString[i]
            for i in range(0, len(inputString))
            if inputString[i].isdigit()
        ][0]
    )


d = firstDigit("var_1__Int")
print(d)
