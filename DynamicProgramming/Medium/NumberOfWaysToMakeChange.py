"""
  DESCRIPTION

  Given an array of distinct positive integers representing coin denominations and a
  single non-negative integer n representing a target amount of
  money, write a function that returns the number of ways to make change for
  that target amount using the given coin denominations.
  
  Note that an unlimited amount of coins is at your disposal.
  

  Time complexity O(C*denoms) - C is a count of coins
  Space complexity O(denoms+1)
"""
import pytest


def numberOfWaysToMakeChange(n, denoms):
    helper = [0]*(denoms+1)
    helper[0] = 1
    for c in n:
        for i in range(1,denoms+1):
            if c<=i:
                helper[i]+=helper[i-c]

    return helper[-1]


# case [n, denoms, expected]
cases = [
    [[1, 5], 6, 2],
    [[2, 3, 4, 7], 0, 1],
    [[5], 9, 0],
    [[2, 4], 7, 0],
    [[1, 5, 10, 25], 4, 1],
    [[1, 5, 10, 25], 5, 2],
    [[1, 5, 10, 25], 10, 4],
    [[1, 5, 10, 25], 25, 13],
    [[2, 3, 7], 12, 4],
    [[2, 3, 4, 7], 7, 3]
]

@pytest.mark.parametrize("n, denoms, expected", cases)
def test_numberOfWaysToMakeChange(n, denoms, expected):
    assert numberOfWaysToMakeChange(n, denoms)==expected

