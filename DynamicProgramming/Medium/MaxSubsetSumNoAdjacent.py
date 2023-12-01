"""
  DESCRIPTION

  Write a function that takes in an array of positive integers and returns the
  maximum sum of non-adjacent elements in the array.

  If the input array is empty, the function should return 0.


  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def maxSubsetSumNoAdjacent(array):
    if len(array)<1:
        return 0
    elif len(array)<3:
        return max(array)
    else:
        sum_array = [array[0]]
        sum_array.append(max(array[:2]))
        for i in range(2,len(array)):
            sum_array.append(max(sum_array[i-1],sum_array[i-2]+array[i]))
    return sum_array[-1]


# case [array, expected]
cases = [
    [[75, 105, 120, 75, 90, 135], 330],
    [[], 0],
    [[1], 1],
    [[1, 2], 2],
    [[1, 2, 3], 4],
    [[1, 15, 3], 15],
    [[7, 10, 12, 7, 9, 14], 33],
    [[4, 3, 5, 200, 5, 3], 207],
    [[10, 5, 20, 25, 15, 5, 5, 15], 60],
    [[10, 5, 20, 25, 15, 5, 5, 15, 3, 15, 5, 5, 15], 90],
    [[125, 210, 250, 120, 150, 300], 675],
    [[30, 25, 50, 55, 100], 180],
    [[30, 25, 50, 55, 100, 120], 205],
    [[7, 10, 12, 7, 9, 14, 15, 16, 25, 20, 4], 72]
]

@pytest.mark.parametrize("array, expected", cases)
def test_maxSubsetSumNoAdjacent(array, expected):
    assert maxSubsetSumNoAdjacent(array)==expected

