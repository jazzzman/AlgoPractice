"""
  DESCRIPTION

  Given an array of positive integers representing coin denominations and a
  single non-negative integer n representing a target amount of
  money, write a function that returns the smallest number of coins needed to
  make change for (to sum up to) that target amount using the given coin
  denominations.

  Note that you have access to an unlimited amount of coins. In other words, if
  the denominations are [1, 5, 10], you have access to an unlimited
  amount of 1s, 5s, and 10s.


  If it's impossible to make change for the target amount, return
  -1.


  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


def minNumberOfCoinsToChange(n, denoms):
    helper = [float('inf')]*(denoms+1)
    helper[0] = 0
    for c in n:
        for i in range(1,len(helper)):
            if i>=c:
                helper[i] = min(helper[i-c]+1, helper[i])
    return helper[-1] if helper[-1] != float('inf') else -1


# case [n, denoms, expected]
cases = [
    [[1, 5, 10], 7, 3],
    [[1, 10, 5], 7, 3],
    [[10, 1, 5], 7, 3],
    [[1, 2, 3], 0, 0],
    [[2, 1], 3, 2],
    [[1, 5, 10], 4, 4],
    [[1, 5, 10], 10, 1],
    [[1, 5, 10], 11, 2],
    [[1, 5, 10], 24, 6],
    [[1, 5, 10], 25, 3],
    [[2, 4], 7, -1],
    [[3, 7], 7, 1],
    [[3, 5], 9, 3],
    [[3, 4, 5], 9, 2],
    [[39, 45, 130, 40, 4, 1], 135, 3],
    [[39, 45, 130, 40, 4, 1, 60, 75], 135, 2],
    [[1, 3, 4], 10, 3]
]

@pytest.mark.parametrize("n, denoms, expected", cases)
def test_minNumberOfCoinsToChange(n, denoms, expected):
    assert minNumberOfCoinsToChange(n, denoms)==expected

