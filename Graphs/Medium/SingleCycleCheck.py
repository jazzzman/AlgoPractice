"""
  DESCRIPTION

  You're given an array of integers where each integer represents a jump of its 
  value in the array. For instance, the integer 2 represents a jump
  of two indices forward in the array; the integer -3 represents a
  jump of three indices backward in the array.


  If a jump spills past the array's bounds, it wraps over to the other side. For
  instance, a jump of -1 at index 0 brings us to the last index in
  the array. Similarly, a jump of 1 at the last index in the array brings us to 
  index 0.


  Write a function that returns a boolean representing whether the jumps in the 
  array form a single cycle. A single cycle occurs if, starting at any index in 
  the array and following the jumps, every element in the array is visited      
  exactly once before landing back on the starting index.



  Time complexity O(n)
  Space complexity O(1)
"""
import pytest

from icecream import ic


def hasSingleCycle(array):
    jump_count = 1
    idx = get_idx(0,array)
    while jump_count<len(array):
        if idx==0:
            return False
        idx = get_idx(idx, array)
        jump_count += 1
    return idx == 0

def get_idx(idx, array):
    step = array[idx]
    idx += step
    return idx%len(array)


# case [array, expected]
cases = [
    [[2, 3, 1, -4, -4, 2], True],
    [[2, 2, -1], True],
    [[2, 2, 2], True],
    [[1, 1, 1, 1, 1], True],
    [[-1, 2, 2], True],
    [[0, 1, 1, 1, 1], False],
    [[1, 1, 0, 1, 1], False],
    [[1, 1, 1, 1, 2], False],
    [[3, 5, 6, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2], True],
    [[3, 5, 5, -5, -2, -5, -12, -2, -1, 2, -6, 1, 1, 2, -5, 2], False],
    [[1, 2, 3, 4, -2, 3, 7, 8, 1], True],
    [[1, 2, 3, 4, -2, 3, 7, 8, -8], True],
    [[1, 2, 3, 4, -2, 3, 7, 8, -26], True],
    [[10, 11, -6, -23, -2, 3, 88, 908, -26], True],
    [[10, 11, -6, -23, -2, 3, 88, 909, -26], False],
    [[1, -1, 1, -1], False]
]

@pytest.mark.parametrize("array, expected", cases)
def test_hasSingleCycle(array, expected):
    assert hasSingleCycle(array)==expected
