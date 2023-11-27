"""
  DESCRIPTION

  You're given an array of integers and an integer. Write a function that moves
  all instances of that integer in the array to the end of the array and returns
  the array.

  The function should perform this in place (i.e., it should mutate the input
  array) and doesn't need to maintain the order of the other integers.


  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def moveElementToEnd(array, toMove):
    mPt,rPt = len(array)-1,len(array)-1
    while mPt>=0:
        if array[mPt]==toMove and mPt!=rPt:
            array[mPt], array[rPt] = array[rPt], array[mPt]
            rPt -= 1
        elif array[mPt]==toMove and mPt==rPt:
            rPt -= 1
        mPt -=1
    return array


# case [array, toMove, expected]
cases = [
    [[2, 1, 2, 2, 2, 3, 4, 2], 2, [4, 1, 3, 2, 2, 2, 2, 2]],
    [[], 3, []],
    [[1, 2, 4, 5, 6], 3, [1, 2, 4, 5, 6]],
    [[3, 3, 3, 3, 3], 3, [3, 3, 3, 3, 3]],
    [[3, 1, 2, 4, 5], 3, [5, 1, 2, 4, 3]],
    [[1, 2, 4, 5, 3], 3, [1, 2, 4, 5, 3]],
    [[1, 2, 3, 4, 5], 3, [1, 2, 5, 4, 3]],
    [[2, 4, 2, 5, 6, 2, 2], 2, [6, 4, 5, 2, 2, 2, 2]],
    [[5, 5, 5, 5, 5, 5, 1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12], 5, [12, 11, 10, 9, 8, 7, 1, 2, 3, 4, 6, 5, 5, 5, 5, 5, 5]],
    [[1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5], 5, [1, 2, 3, 4, 6, 7, 8, 9, 10, 11, 12, 5, 5, 5, 5, 5, 5]],
    [[5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12], 5, [12, 1, 2, 11, 10, 3, 4, 6, 7, 9, 8, 5, 5, 5, 5, 5, 5]]
]

@pytest.mark.parametrize("array, toMove, expected", cases)
def test_moveElementToEnd(array, toMove, expected):
    # a little trick for analyzing the end of arrays
    count = len(list(filter(lambda a: a==toMove,array)))
    assert moveElementToEnd(array, toMove)[-count:]==expected[-count:]

