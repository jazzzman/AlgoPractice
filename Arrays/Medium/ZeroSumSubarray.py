"""
  DESCRIPTION

    You're given a list of integers nums. Write a function that
    returns a boolean representing whether there exists a zero-sum subarray of
    nums.
 
    A zero-sum subarray is any subarray where all of the values add up to zero.
    A subarray is any contiguous section of the array. For the purposes of this
    problem, a subarray can be as small as one element and as long as the
    original array.
   

  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def zeroSumSubarray(nums):
    sums = set([0])
    current_sum = 0
    for n in nums:
        current_sum += n
        if current_sum in sums:
            return True
        sums.add(current_sum)
    return False


# case [nums, expected]
cases = [
    [[], False],
    [[0], True],
    [[1], False],
    [[1, 2, 3], False],
    [[1, 1, 1], False],
    [[-1, -1, -1], False],
    [[0, 0, 0], True],
    [[1, 2, -2, 3], True],
    [[2, -2], True],
    [[-1, 2, 3, 4, -5, -3, 1, 2], True],
    [[-2, -3, -1, 2, 3, 4, -5, -3, 1, 2], True],
    [[2, 3, 4, -5, -3, 4, 5], True],
    [[2, 3, 4, -5, -3, 5, 5], False],
    [[1, 2, 3, 4, 0, 5, 6, 7], True],
    [[1, 2, 3, -2, -1], True],
    [[-8, -22, 104, 73, -120, 53, 22, -12, 1, 14, -90, 13, -22], False],
    [[-8, -22, 104, 73, -120, 53, 22, 20, 25, -12, 1, 14, -90, 13, -22], True]
]

@pytest.mark.parametrize("nums, expected", cases)
def test_zeroSumSubarray(nums, expected):
    assert zeroSumSubarray(nums)==expected

