"""
  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. If any two numbers in the input array sum
  up to the target sum, the function should return them in an array, in any
  order. If no two numbers sum up to the target sum, the function should return
  an empty array.

  Note that the target sum has to be obtained by summing two different integers
  in the array; you can't add a single integer to itself in order to obtain the
  target sum.

  You can assume that there will be at most one pair of numbers summing up to
  the target sum.

  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def twoNumberSum(array, targetSum):
    dic={}
    for i,v in enumerate(array):
        dic[v]=i
    for i in range(len(array)):
        d = targetSum-array[i]
        if d in dic and i != dic[d]:
            return [array[i],d]
    return []


cases = [
    [[3, 5, -4, 8, 11, 1, -1, 6], 10, [11, -1]],
    [[4, 6], 10, [4, 6]],
    [[4, 6, 1], 5, [4, 1]],
    [[4, 6, 1, -3], 3, [6, -3]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9], 17, [8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [3, 15]],
    [[-7, -5, -3, -1, 0, 1, 3, 5, 7], -5, [-5, 0]],
    [[-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 163, [210, -47]],
    [[-21, 301, 12, 4, 65, 56, 210, 356, 9, -47], 164, []],
    [[3, 5, -4, 8, 11, 1, -1, 6], 15, []],
    [[14], 15, []],
    [[15], 15, []]
]

@pytest.mark.parametrize("array, targetSum, expected",cases)
def test_twoNumberSum(array,targetSum,expected):
    assert twoNumberSum(array,targetSum)==expected
