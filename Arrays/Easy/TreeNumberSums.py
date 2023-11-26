"""
  DESCRIPTION

  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all triplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these triplets. The numbers in each triplet should be ordered in ascending
  order, and the triplets themselves should be ordered in ascending order with
  respect to the numbers they hold.

  If no three numbers sum up to the target sum, the function should return an
  empty array.


  Time complexity O(n^2)
  Space complexity O(n)
"""
import pytest


def treeNumberSum(array, targetSum):
    array.sort()
    triplets = []
    for lPt in range(len(array)-2):
        doubles = doubleNumberSum(array[lPt+1:],targetSum-array[lPt])
        for d in doubles:
            triplets.append([array[lPt],*d])
    return triplets

def doubleNumberSum(array, targetSum):
    output = []
    lPt,rPt = 0, len(array)-1
    while lPt<rPt:
        if array[lPt]+array[rPt]>targetSum:
            rPt-=1
        elif array[lPt]+array[rPt]<targetSum:
            lPt+=1
        else:
            output.append([array[lPt],array[rPt]])
            lPt+=1
    return output


# case [arg1,arg2,...,expected]
cases = [
    [[12, 3, 1, 2, -6, 5, -8, 6], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]],
    [[1, 2, 3], 6, [[1, 2, 3]]],
    [[1, 2, 3], 7, []],
    [[8, 10, -2, 49, 14], 57, [[-2, 10, 49]]],
    [[12, 3, 1, 2, -6, 5, 0, -8, -1], 0, [[-8, 3, 5], [-6, 1, 5], [-1, 0, 1]]],
    [[12, 3, 1, 2, -6, 5, 0, -8, -1, 6], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-1, 0, 1]]],
    [[12, 3, 1, 2, -6, 5, 0, -8, -1, 6, -5], 0, [[-8, 2, 6], [-8, 3, 5], [-6, 0, 6], [-6, 1, 5], [-5, -1, 6], [-5, 0, 5], [-5, 2, 3], [-1, 0, 1]]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 18, [[1, 2, 15], [1, 8, 9], [2, 7, 9], [3, 6, 9], [3, 7, 8], [4, 5, 9], [4, 6, 8], [5, 6, 7]]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 32, [[8, 9, 15]]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 33, []],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 15], 5, []]
]

@pytest.mark.parametrize("array, targetSum, expected",cases)
def test_treeNumberSum(array, targetSum, expected):
    assert treeNumberSum(array, targetSum)==expected

