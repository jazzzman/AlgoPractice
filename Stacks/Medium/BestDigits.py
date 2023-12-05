"""
  DESCRIPTION

  Write a function that takes a positive integer represented as a string       
  number and an integer numDigits.
  Remove numDigits from the string so that the number represented
  by the string is as large as possible afterwards.


  Note that the order of the remaining digits cannot be changed. You can assume
  numDigits will always be less than the length of number
  and greater than or equal to 0.

  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def bestDigits(number, numDigits):
    idx = 0
    numDigits = list(numDigits)
    while number>0:
        if (idx<len(numDigits)-1 and numDigits[idx]<numDigits[idx+1]) or idx>=len(numDigits)-1:
            numDigits.pop(idx)
            idx = max(0, idx-1)
            number -= 1
        else:
            idx += 1

    return int(''.join(numDigits))


# case [number,  numDigits, expected]
cases = [
    [2, '462839', 6839],
    [4, '129847563', 98763],
    [1, '19', 9],
    [1, '22', 2],
    [1, '23', 3],
    [1, '123', 23],
    [1, '321', 32],
    [2, '123', 3],
    [2, '321', 3],
    [10, '11111111119999999999', 9999999999],
    [9, '10000000002', 12],
    [10, '10000000002', 2],
    [5, '1020304050', 34050],
    [4, '100300200004', 30200004],
    [9, '9999999999', 9],
    [3, '111221', 221],
    [0, '12345', 12345],
    [0, '54321', 54321]
]

@pytest.mark.parametrize("number,  numDigits, expected", cases)
def test_bestDigits(number,  numDigits, expected):
    assert bestDigits(number, numDigits)==expected

