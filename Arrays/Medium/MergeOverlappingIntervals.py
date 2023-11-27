"""
  DESCRIPTION

  Write a function that takes in a non-empty array of arbitrary intervals,
  merges any overlapping intervals, and returns the new intervals in no
  particular order.

  Each interval interval is an array of two integers, with
  interval[0] as the start of the interval and
  interval[1] as the end of the interval.

  Note that back-to-back intervals aren't considered to be overlapping. For
  example, [1, 5] and [6, 7] aren't overlapping;
  however, [1, 6] and [6, 7] are indeed
  overlapping.

  Also note that the start of any particular interval will always be less than
  or equal to the end of that interval.


  Time complexity O(nlogn)
  Space complexity O(n)
"""
import pytest


def mergeOverlappingIntervals(intervals):
    intervals.sort(key=lambda i:i[0])
    result = []
    if len(intervals)==1:
        return intervals
    # cases:
    #   1. [1,3] [2,4] [6,9] => [1,4] [6,9]  
    #   2. [1,5] [2,3] [6,9] => [1,5] [6,9]
    #   3. [1,4] [1,5] [5,9] => [1,5] [6,9]
    #   4. [1,5] [1,3] [6,9] => [1,5] [6,9]
    ptr = 0
    rPtr = 1
    left,right = intervals[0]
    while rPtr < len(intervals):
        if right>=intervals[rPtr][0]:
            right = max(right,intervals[rPtr][1])
            rPtr += 1
        else:
            result.append([left,right])
            ptr = rPtr
            left,right = intervals[ptr]
            rPtr += 1
                
    result.append([left,right])


    return result


# case [intervals, expected]
cases = [
    [[[1, 2], [3, 5], [4, 7], [6, 8], [9, 10]], [[1, 2], [3, 8], [9, 10]]],
    [[[1, 3], [2, 8], [9, 10]], [[1, 8], [9, 10]]],
    [[[1, 10], [10, 20], [20, 30], [30, 40], [40, 50], [50, 60], [60, 70], [70, 80], [80, 90], [90, 100]], [[1, 100]]],
    [[[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]], [[1, 10], [11, 20], [21, 30], [31, 40], [41, 50], [51, 60], [61, 70], [71, 80], [81, 90], [91, 100]]],
    [[[100, 105], [1, 104]], [[1, 105]]],
    [[[89, 90], [-10, 20], [-50, 0], [70, 90], [90, 91], [90, 95]], [[-50, 20], [70, 95]]],
    [[[-5, -4], [-4, -3], [-3, -2], [-2, -1], [-1, 0]], [[-5, 0]]],
    [[[43, 49], [9, 12], [12, 54], [45, 90], [91, 93]], [[9, 90], [91, 93]]],
    [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0]], [[0, 0]]],
    [[[0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 0], [0, 1]], [[0, 1]]],
    [[[1, 22], [-20, 30]], [[-20, 30]]],
    [[[20, 21], [22, 23], [0, 1], [3, 4], [23, 24], [25, 27], [5, 6], [7, 19]], [[0, 1], [3, 4], [5, 6], [7, 19], [20, 21], [22, 24], [25, 27]]],
    [[[2, 3], [4, 5], [6, 7], [8, 9], [1, 10]], [[1, 10]]]
]

@pytest.mark.parametrize("intervals, expected", cases)
def test_mergeOverlappingIntervals(intervals, expected):
    assert mergeOverlappingIntervals(intervals)==expected

