"""
  DESCRIPTION

  You're given an array of integers and another array of three distinct
  integers. The first array is guaranteed to only contain integers that are in  
  the second array, and the second array represents a desired order for the     
  integers in the first array. For example, a second array of
  [x, y, z] represents a desired order of
  [x, x, ..., x, y, y, ..., y, z, z, ..., z] in the first array.


  Write a function that sorts the first array according to the desired order in 
  the second array.


  The function should perform this in place (i.e., it should mutate the input   
  array), and it shouldn't use any auxiliary space (i.e., it should run with    
  constant space: O(1) space).


  Note that the desired order won't necessarily be ascending or descending and  
  that the first array won't necessarily contain all three integers found in the
  second array—it might only contain one or two.



  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def threeNumberSort(array, order):
    base_idx = 0

    for order_value in order:
        right_idx = base_idx
        while right_idx<len(array):
            if array[right_idx] == order_value:
                array[base_idx], array[right_idx] = array[right_idx], array[base_idx]
                base_idx += 1
            right_idx += 1
    return array


# case [array, order, expected]
cases = [
    [[1, 0, 0, -1, -1, 0, 1, 1], [0, 1, -1], [0, 0, 0, 1, 1, 1, -1, -1]],
    [[7, 8, 9, 7, 8, 9, 9, 9, 9, 9, 9, 9], [8, 7, 9], [8, 8, 7, 7, 9, 9, 9, 9, 9, 9, 9, 9]],
    [[], [0, 7, 9], []],
    [[-2, -3, -3, -3, -3, -3, -2, -2, -3], [-2, -3, 0], [-2, -2, -2, -3, -3, -3, -3, -3, -3]],
    [[0, 10, 10, 10, 10, 10, 25, 25, 25, 25, 25], [25, 10, 0], [25, 25, 25, 25, 25, 10, 10, 10, 10, 10, 0]],
    [[6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6], [4, 5, 6], [6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]],
    [[1, 3, 4, 4, 4, 4, 3, 3, 3, 4, 1, 1, 1, 4, 4, 1, 3, 1, 4, 4], [1, 4, 3], [1, 1, 1, 1, 1, 1, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3]],
    [[1, 2, 3], [3, 1, 2], [3, 1, 2]],
    [[0, 1, 2, 0, 1, 2, 0, 1, 2, 0, 1, 1, 2], [1, 2, 0], [1, 1, 1, 1, 1, 2, 2, 2, 2, 0, 0, 0, 0]],
    [[7, 7, 7, 11, 11, 7, 11, 7], [11, 7, 9], [11, 11, 11, 7, 7, 7, 7, 7]],
    [[9, 9, 9, 7, 9, 7, 9, 9, 7, 9], [11, 7, 9], [7, 7, 7, 9, 9, 9, 9, 9, 9, 9]],
    [[9, 9, 9, 7, 9, 7, 9, 9, 7, 9], [7, 11, 9], [7, 7, 7, 9, 9, 9, 9, 9, 9, 9]],
    [[1], [0, 1, 2], [1]],
    [[0, 1], [1, 2, 0], [1, 0]]
]

@pytest.mark.parametrize("array, order, expected", cases)
def test_threeNumberSort(array, order, expected):
    assert threeNumberSort(array, order)==expected

