"""
  DESCRIPTION

  Write a function that takes in an array of unique integers and returns its   
  powerset.


  The powerset P(X) of a set X is the set of all
  subsets of X. For example, the powerset of [1,2] is
  [[], [1], [2], [1,2]].


  Note that the sets in the powerset do not need to be in any particular order.

  Time complexity O(n*2^n)
  Space complexity O(n*2^n)
"""
import pytest


def powerset(array):
    result = [[]]

    while array:
        sub = [array.pop(0)] 
        for i in range(len(result)):
            result.append(result[i]+sub)

    return result


# case [array, expected]
cases = [
    [[1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]],
    [[], [[]]],
    [[1], [[], [1]]],
    [[1, 2], [[], [1], [2], [1, 2]]],
    [[1, 2, 3, 4], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]],
    [[1, 2, 3, 4, 5], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], [5], [1, 5], [2, 5], [1, 2, 5], [3, 5], [1, 3, 5], [2, 3, 5], [1, 2, 3, 5], [4, 5], [1, 4, 5], [2, 4, 5], [1, 2, 4, 5], [3, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5]]], 
    [[1, 2, 3, 4, 5, 6], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4], [5], [1, 5], [2, 5], [1, 2, 5], [3, 5], [1, 3, 5], [ 2, 3, 5], [1, 2, 3, 5], [4, 5], [1, 4, 5], [2, 4, 5], [1, 2, 4, 5], [3, 4, 5], [1, 3, 4, 5], [2, 3, 4, 5], [1, 2, 3, 4, 5], [6], [1, 6], [2, 6], [1, 2, 6], [3, 6], [1, 3, 6], [2, 3, 6], [1, 2, 3, 6], [4, 6], [1, 4, 6], [2, 4, 6], [1, 2, 4, 6], [3, 4, 6], [1, 3, 4, 6], [2, 3, 4, 6], [1, 2, 3, 4, 6], [5, 6], [1, 5, 6], [2, 5, 6], [1, 2, 5, 6], [3, 5, 6], [1, 3, 5, 6], [2, 3, 5, 6], [1, 2, 3, 5, 6], [4, 5, 6 ], [1, 4, 5, 6], [2, 4, 5, 6], [1, 2, 4, 5, 6], [3, 4, 5, 6], [1, 3, 4, 5, 6], [2, 3, 4, 5, 6], [1, 2, 3, 4, 5, 6]]]
]

@pytest.mark.parametrize("array, expected", cases)
def test_powerset(array, expected):
    assert powerset(array)==expected

