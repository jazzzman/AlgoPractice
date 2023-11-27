"""
  DESCRIPTION

  Write a function that takes in a non-empty array of integers and returns an
  array of the same length, where each element in the output array is equal to
  the product of every other number in the input array.

  In other words, the value at output[i] is equal to the product of
  every number in the input array other than input[i].

  Note that you're expected to solve this problem without using division.


  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def arrayOfProducts(array):
    rightleft = [1]
    leftright = [1]
    
    for i in range(1,len(array)):
        rightleft.append(rightleft[i-1]*array[len(array)-i])
    rightleft = rightleft[::-1]

    for i in range(1,len(array)):
        leftright.append(leftright[i-1]*array[i-1])

    return [leftright[i]*rightleft[i] for i in range(len(array))]




    return result


# case [array, expected]
cases = [
    [[5, 1, 4, 2], [8, 40, 10, 20]],
    [[1, 8, 6, 2, 4], [384, 48, 64, 192, 96]],
    [[-5, 2, -4, 14, -6], [672, -1680, 840, -240, 560]],
    [[9, 3, 2, 1, 9, 5, 3, 2], [1620, 4860, 7290, 14580, 1620, 2916, 4860, 7290]],
    [[4, 4], [4, 4]],
    [[0, 0, 0, 0], [0, 0, 0, 0]],
    [[1, 1, 1, 1], [1, 1, 1, 1]],
    [[-1, -1, -1], [1, 1, 1]],
    [[-1, -1, -1, -1], [-1, -1, -1, -1]],
    [[0, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
    [[0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [362880, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
]

@pytest.mark.parametrize("array, expected", cases)
def test_arrayOfProducts(array, expected):
    assert arrayOfProducts(array)==expected

