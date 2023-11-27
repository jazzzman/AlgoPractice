"""
  DESCRIPTION

  Write a function that takes in an array of integers and returns the length of
  the longest peak in the array.

  A peak is defined as adjacent integers in the array that are strictly
  increasing until they reach a tip (the highest value in the peak), at which
  point they become strictly decreasing. At least three integers are required to
  form a peak.

  For example, the integers 1, 4, 10, 2 form a peak, but the
  integers 4, 0, 10 don't and neither do the integers
  1, 2, 2, 0. Similarly, the integers 1, 2, 3 don't
  form a peak because there aren't any strictly decreasing integers after the
  3.


  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def longestPeak(array):
    ptr = 1
    peak_length = 0
    while ptr<len(array)-1:
        if isPeak(array[ptr-1],array[ptr],array[ptr+1]):
            curr_length = leftSide(ptr,array)+rightSide(ptr,array)+1
            peak_length = max(peak_length, curr_length)
        ptr+=1
    return peak_length

def isPeak(a,b,c):
    if a<b and b>c:
        return True
    return False

def leftSide(ptr, array):
    length = 0
    while ptr>0:
        if array[ptr-1]<array[ptr]:
            length+=1
        else:
            break
        ptr-=1
    return length

def rightSide(ptr,array):
    length = 0
    while ptr<len(array)-1:
        if array[ptr]>array[ptr+1]:
            length+=1
        else:
            break
        ptr+=1
    return length


# case [array, expected]
cases = [
    [[1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3], 6],
    [[], 0],
    [[1, 3, 2], 3],
    [[1, 2, 3, 4, 5, 1], 6],
    [[5, 4, 3, 2, 1, 2, 1], 3],
    [[5, 4, 3, 2, 1, 2, 10, 12, -3, 5, 6, 7, 10], 5],
    [[5, 4, 3, 2, 1, 2, 10, 12], 0],
    [[1, 2, 3, 4, 5, 6, 10, 100, 1000], 0],
    [[1, 2, 3, 3, 2, 1], 0],
    [[1, 1, 3, 2, 1], 4],
    [[1, 2, 3, 2, 1, 1], 5],
    [[1, 1, 1, 2, 3, 10, 12, -3, -3, 2, 3, 45, 800, 99, 98, 0, -1, -1, 2, 3, 4, 5, 0, -1, -1], 9],
    [[1, 2, 3, 3, 4, 0, 10], 3]
]

@pytest.mark.parametrize("array, expected", cases)
def test_longestPeak(array, expected):
    assert longestPeak(array)==expected

