"""
  DESCRIPTION

  Write a function that takes in an array of integers and returns a boolean
  representing whether the array is monotonic.

  An array is said to be monotonic if its elements, from left to right, are
  entirely non-increasing or entirely non-decreasing.

  Non-increasing elements aren't necessarily exclusively decreasing; they simply
  don't increase. Similarly, non-decreasing elements aren't necessarily
  exclusively increasing; they simply don't decrease.

  Note that empty arrays and arrays of one element are monotonic.


  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def isMonotonic(array):
    isNonDecreasing = True
    isNonIncreasing = True

    for i in range(1,len(array)):
        if array[i]<array[i-1]:
            isNonDecreasing = False
        if array[i]>array[i-1]:
            isNonIncreasing = False
    
    return isNonDecreasing or isNonIncreasing


# case [array, expected]
cases = [
    [[-1, -5, -10, -1100, -1100, -1101, -1102, -9001], True],
    [[], True],
    [[1], True],
    [[1, 2], True],
    [[2, 1], True],
    [[1, 5, 10, 1100, 1101, 1102, 9001], True],
    [[-1, -5, -10, -1100, -1101, -1102, -9001], True],
    [[-1, -5, -10, -1100, -900, -1101, -1102, -9001], False],
    [[1, 2, 0], False],
    [[1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 7, 9, 10, 11], False],
    [[1, 1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 11], True],
    [[-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -7, -9, -10, -11], False],
    [[-1, -1, -2, -3, -4, -5, -5, -5, -6, -7, -8, -8, -9, -10, -11], True],
    [[-1, -1, -1, -1, -1, -1, -1, -1], True],
    [[1, 2, -1, -2, -5], False],
    [[-1, -5, 10], False],
    [[2, 2, 2, 1, 4, 5], False],
    [[1, 1, 1, 2, 3, 4, 1], False],
    [[1, 2, 3, 3, 2, 1], False]
]

@pytest.mark.parametrize("array, expected", cases)
def test_isMonotonic(array, expected):
    assert isMonotonic(array)==expected

