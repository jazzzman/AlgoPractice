"""
  DESCRIPTION

  Given an array of positive integers representing the values of coins in your
  possession, write a function that returns the minimum amount of change (the
  minimum sum of money) that you <b>cannot</b> create. The given coins can have
  any positive integer value and aren't necessarily unique (i.e., you can have
  multiple coins of the same value).

  For example, if you're given <span>coins = [1, 2, 5]</span>, the minimum
  amount of change that you can't create is <span>4</span>. If you're given no
  coins, the minimum amount of change that you can't create is <span>1</span>.


  Time complexity
  Space complexity
"""
import pytest


def nonConstuctibleChange(coins):
    coins.sort()
    change = 0
    for coin in coins:
        if coin>change+1:
            return change+1
        else:
            change += coin
    return change+1


cases = [
    [[5, 6, 1, 1, 2, 3, 43], 19],
    [[1, 1], 3],
    [[2], 1],
    [[1], 2],
    [[109, 2000, 8765, 19, 18, 17, 16, 8, 1, 1, 2, 4], 87],
    [[1, 2, 3, 4, 5, 6, 7], 29]
]

@pytest.mark.parametrize("coins, expected",cases)
def test_nonConstructibleChange(coins,expected):
    assert nonConstuctibleChange(coins)==expected

