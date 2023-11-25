"""
  Given two non-empty arrays of integers, write a function that determines
  whether the second array is a subsequence of the first one.

  A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers <span>[1, 3, 4]</span> form a subsequence of the array
  <span>[1, 2, 3, 4]</span>, and so do the numbers <span>[2, 4]</span>. Note
  that a single number in an array and the array itself are both valid
  subsequences of the array.

  Time complexity 
  Space complexity
"""
import pytest


def isValidSubsequence(array,sequence):
    sPtr = 0
    for v in array:
        if sPtr<len(sequence) and v == sequence[sPtr]:
            sPtr += 1

    return sPtr==len(sequence)


cases = [
    [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 6, -1, 8, 10], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [22, 25, 6], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, 10], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 10], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, -1, 8, 10], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [25], True],
    [[1, 1, 1, 1, 1], [1, 1, 1], True],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 12], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [4, 5, 1, 22, 25, 6, -1, 8, 10], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 23, 6, -1, 8, 10], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 25, 6, -1, 8, 10], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 22, 6, -1, 8, 10], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -1, 10], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, -2], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [26], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 25, 22, 6, -1, 8, 10], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 26, 22, 8], False],
    [[1, 1, 6, 1], [1, 1, 1, 6], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 10, 11, 11, 11, 11], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [5, 1, 22, 25, 6, -1, 8, 10, 10], False],
    [[5, 1, 22, 25, 6, -1, 8, 10], [1, 6, -1, 5], False]
]

@pytest.mark.parametrize("array, sequence, expected",cases)
def test_isValidSubsequence(array,sequence,expected):
    assert isValidSubsequence(array,sequence)==expected
