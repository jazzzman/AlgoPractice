"""
  DESCRIPTION

    You're given an unordered list of unique integers nums in the
    range [1, n], where n represents the length of
    nums + 2. This means that two numbers in this range are missing
    from the list.

    Write a function that takes in this list and returns a new list with the two
    missing numbers, sorted numerically.


  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def missingNumbers(nums):
    nums+=[len(nums)+3]*2
    for i in range(len(nums)-2):
        nums[abs(nums[i])-1]*=-1

    return [i+1 for i,v in enumerate(nums) if v>0]

# Time complexity O(n) Space complexity O(n)
def missingNumbers_extramemory(nums):
    output = set(range(1,len(nums)+3))
    for n in nums:
        output.remove(n)
    return list(output)


# case [nums, expected]
cases = [
    [[], [1, 2]],
    [[1], [2, 3]],
    [[2], [1, 3]],
    [[3], [1, 2]],
    [[1, 3], [2, 4]],
    [[3, 1], [2, 4]],
    [[1, 2, 3], [4, 5]],
    [[3, 2, 1], [4, 5]],
    [[3, 1, 2], [4, 5]],
    [[3, 4, 5], [1, 2]],
    [[4, 5, 3], [1, 2]],
    [[1, 3, 4, 5], [2, 6]],
    [[4, 5, 1, 3], [2, 6]],
    [[1, 2, 4, 5, 7], [3, 6]],
    [[1, 2, 7, 5, 4], [3, 6]],
    [[1, 2, 3, 4, 5, 6, 7], [8, 9]],
    [[7, 6, 5, 4, 3, 2, 1], [8, 9]],
    [[3, 5, 1, 2, 4, 7, 6], [8, 9]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 20, 21, 22], [14, 19]],
    [[3, 5, 7, 8, 1, 10, 11, 2, 4, 13, 17, 22, 18, 21, 16, 20, 6, 9, 15, 12], [14, 19]],
    [[3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [1, 2]],
    [[14, 15, 16, 17, 18, 19, 20, 21, 22, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], [1, 2]],
    [[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22], [23, 24]],
    [[11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [23, 24]]
]

@pytest.mark.parametrize("nums, expected", cases)
def test_missingNumbers(nums, expected):
    assert missingNumbers(nums)==expected

