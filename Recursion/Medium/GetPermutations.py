"""
  DESCRIPTION

  Write a function that takes in an array of unique integers and returns an
  array of all permutations of those integers in no particular order.      

  If the input array is empty, the function should return an empty array.    


  Time complexity O(n*n!)
  Space complexity O(n*n!)
"""
import pytest


def getPermutations(array, root = None):
    result = []
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return [array]
    elif len(array) == 2:
        return [array,array[::-1]]
    for i in range(len(array)):
        perms = getPermutations([array[j] for j in range(len(array)) if j!=i])
        result.extend([ [array[i]]+perm for perm in perms])
    return result


# case [array, expected]
cases = [
    [[1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]],
    [[], []],
    [[1], [[1]]],
    [[1, 2], [[1, 2], [2, 1]]],
    [[1, 2, 3, 4], [[1, 2, 3, 4], [1, 2, 4, 3], [1, 3, 2, 4], [1, 3, 4, 2], [1, 4, 2, 3], [1, 4, 3, 2], [2, 1, 3, 4], [2, 1, 4, 3], [2, 3, 1, 4], [2, 3, 4, 1], [2, 4, 1, 3], [2, 4, 3, 1], [3, 1, 2, 4], [3, 1, 4, 2], [3, 2, 1, 4], [3, 2, 4, 1], [3, 4, 1, 2], [3, 4, 2, 1], [4, 1, 2, 3], [4, 1, 3, 2], [4, 2, 1, 3], [4, 2, 3, 1], [4, 3, 1, 2], [4, 3, 2, 1]]],
]

@pytest.mark.parametrize("array, expected", cases)
def test_getPermutations(array, expected):
    assert getPermutations(array)==expected

