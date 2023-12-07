"""
  DESCRIPTION

  Given an array of buildings and a direction that all of the buildings face, 
  return an array of the indices of the buildings that can see the sunset.    


  A building can see the sunset if it's strictly taller than all of the       
  buildings that come after it in the direction that it faces.


  The input array named buildings contains positive, non-zero
  integers representing the heights of the buildings. A building at index     
  i thus has a height denoted by buildings[i]. All of
  the buildings face the same direction, and this direction is either east or 
  west, denoted by the input string named direction, which will
  always be equal to either "EAST" or "WEST". In
  relation to the input array, you can interpret these directions as right for
  east and left for west.


  Important note: the indices in the ouput array should be sorted in ascending
  order.

  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def sunsetViews(buildings, direction):
    result = []
    if direction == 'EAST':
        for idx in reversed(range(len(buildings))):
            if len(result)==0 or buildings[idx]>buildings[result[-1]]:
                result.append(idx)
    else:
        for idx in range(len(buildings)):
            if len(result)==0 or buildings[idx]>buildings[result[-1]]:
                result.append(idx)

    return result


# case [buildings, direction, expected]
cases = [
    [[3, 5, 4, 4, 3, 1, 3, 2], 'EAST', [1, 3, 6, 7]],
    [[3, 5, 4, 4, 3, 1, 3, 2], 'WEST', [0, 1]],
    [[10, 11], 'EAST', [1]],
    [[2, 4], 'WEST', [0, 1]],
    [[1], 'EAST', [0]],
    [[1], 'WEST', [0]],
    [[], 'EAST', []],
    [[], 'WEST', []],
    [[7, 1, 7, 8, 9, 8, 7, 6, 5, 4, 2, 5], 'EAST', [4, 5, 6, 7, 11]],
    [[1, 2, 3, 4, 5, 6], 'EAST', [5]],
    [[1, 2, 3, 4, 5, 6], 'WEST', [0, 1, 2, 3, 4, 5]],
    [[1, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8], 'WEST', [0, 1, 2, 4, 5, 6, 10, 13]],
    [[20, 2, 3, 1, 5, 6, 9, 1, 9, 9, 11, 10, 9, 12, 8], 'EAST', [0, 13, 14]]
]

@pytest.mark.parametrize("buildings, direction, expected", cases)
def test_sunsetViews(buildings, direction, expected):
    assert sorted(sunsetViews(buildings, direction))==expected

