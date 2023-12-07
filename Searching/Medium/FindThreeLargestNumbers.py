"""
  DESCRIPTION

  Write a function that takes in an array of at least three integers and,     
  without sorting the input array, returns a sorted array of the three largest
  integers in the input array.


  The function should return duplicate integers if necessary; for example, it 
  should return [10, 10, 12] for an input array of
  [10, 5, 9, 10, 12].


  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def findThreeLargestNumbers(array):
    output = []
    idxs = []
    for i in range(3):
        current_max = float('-inf')
        last_max_idx = -1
        for idx, value in enumerate(array):
            if value>current_max and idx not in idxs:
                current_max = value
                last_max_idx = idx

        output.append(current_max)
        idxs.append(last_max_idx)

    return output[::-1]

# a little bit pretier way to abide the same logic
def findThreeLargestNumbers_v2(array):
    output = [float('-inf')]*3
    idxs = [-1]*3

    for count in range(3):
        for idx, value in enumerate(array):
            if value > output[count] and idx not in idxs:
                output[count] = value
                idxs[coutn] = idx

    return output[::-1]

# case [array, expected]
cases = [
    [[141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7], [18, 141, 541]],
    [[55, 7, 8], [7, 8, 55]],
    [[55, 43, 11, 3, -3, 10], [11, 43, 55]],
    [[7, 8, 3, 11, 43, 55], [11, 43, 55]],
    [[55, 7, 8, 3, 43, 11], [11, 43, 55]],
    [[7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7], [7, 7, 7]],
    [[7, 7, 7, 7, 7, 7, 8, 7, 7, 7, 7], [7, 7, 8]],
    [[-1, -2, -3, -7, -17, -27, -18, -541, -8, -7, 7], [-2, -1, 7]]
]

@pytest.mark.parametrize("array, expected", cases)
def test_findThreeLargestNumbers(array, expected):
    assert findThreeLargestNumbers(array)==expected

