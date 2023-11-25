"""
  DESCRIPTION

  Write a function that takes in a non-empty array of integers that are sorted
  in ascending order and returns a new array of the same length with the squares
  of the original integers also sorted in ascending order.


  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def sortedSquaredArray(array):
    squared = []
    lPt,rPt = 0, len(array)-1

    if len(array)==1:
        return [array[0]**2]

    while lPt<=rPt:
        if abs(array[lPt])>abs(array[rPt]):
            squared.append(array[lPt]**2)
            lPt+=1
        else:
            squared.append(array[rPt]**2)
            rPt-=1
    return squared[::-1]


cases = [
    [[1, 2, 3, 5, 6, 8, 9], [1, 4, 9, 25, 36, 64, 81]],
    [[1], [1]],
    [[1, 2], [1, 4]],
    [[1, 2, 3, 4, 5], [1, 4, 9, 16, 25]],
    [[0], [0]],
    [[10], [100]],
    [[-1], [1]],
    [[-2, -1], [1, 4]],
    [[-5, -4, -3, -2, -1], [1, 4, 9, 16, 25]],
    [[-10], [100]],
    [[-10, -5, 0, 5, 10], [0, 25, 25, 100, 100]],
    [[-7, -3, 1, 9, 22, 30], [1, 9, 49, 81, 484, 900]],
    [[-50, -13, -2, -1, 0, 0, 1, 1, 2, 3, 19, 20], [0, 0, 1, 1, 1, 4, 4, 9, 169, 361, 400, 2500]],
    [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[-1, -1, 2, 3, 3, 3, 4], [1, 1, 4, 9, 9, 9, 16]],
    [[-3, -2, -1], [1, 4, 9]],
    [[-3, -2, -1], [1, 4, 9]]
]

@pytest.mark.parametrize("array, expected",cases)
def test_sortedSquaredArray(array,expected):
    assert sortedSquaredArray(array)==expected

