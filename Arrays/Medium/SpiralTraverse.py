"""
  DESCRIPTION

  Write a function that takes in an n x m two-dimensional array (that can be
  square-shaped when n == m) and returns a one-dimensional array of all the
  array's elements in spiral order.

  Spiral order starts at the top left corner of the two-dimensional array, goes
  to the right, and proceeds in a spiral pattern all the way until every element
  has been visited.


  Time complexity O(m*n)
  Space complexity O(m*n)
"""
import pytest


def spiralTraverse(array):
    result = []

    append_bounds(array,0,len(array[0])-1,0,len(array)-1,result)
        
    return result

def append_bounds(array,left,right,top,bottom,result):
    if left>right or top>bottom:
        return

    for column in range(left,right+1):
        result.append(array[top][column])

    for row in range(top+1,bottom+1):
        result.append(array[row][right])
    
    for column in range(right-1,left-1,-1):
        # edge case for middle column
        if top == bottom:
            break
        result.append(array[bottom][column])

    for row in range(bottom-1,top,-1):
        # edge case for middle row
        if right == left:
            break
        result.append(array[row][left])
    
    append_bounds(array, left+1, right-1, top+1, bottom-1, result)




# case [array, expected]
cases = [
    [[[1, 2, 3, 4], [12, 13, 14, 5], [11, 16, 15, 6], [10, 9, 8, 7]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]],
    [[[1]], [1]],
    [[[1, 2], [4, 3]], [1, 2, 3, 4]],
    [[[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]],
    [[[19, 32, 33, 34, 25, 8], [16, 15, 14, 13, 12, 11], [18, 31, 36, 35, 26, 9], [1, 2, 3, 4, 5, 6], [20, 21, 22, 23, 24, 7], [17, 30, 29, 28, 27, 10]], [19, 32, 33, 34, 25, 8, 11, 9, 6, 7, 10, 27, 28, 29, 30, 17, 20, 1, 18, 16, 15, 14, 13, 12, 26, 5, 24, 23, 22, 21, 2, 31, 36, 35, 4, 3]], 
    [[[4, 2, 3, 6, 7, 8, 1, 9, 5, 10], [12, 19, 15, 16, 20, 18, 13, 17, 11, 14]], [4, 2, 3, 6, 7, 8, 1, 9, 5, 10, 14, 11, 17, 13, 18, 20, 16, 15, 19, 12]], 
    [[[27, 12, 35, 26], [25, 21, 94, 11], [19, 96, 43, 56], [55, 36, 10, 18], [96, 83, 31, 94], [93, 11, 90, 16]], [27, 12, 35, 26, 11, 56, 18, 94, 16, 90, 11, 93, 96, 55, 19, 25, 21, 94, 43, 10, 31, 83, 36, 96]],
    [[[1, 2, 3, 4], [10, 11, 12, 5], [9, 8, 7, 6]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]],
    [[[1, 2, 3], [12, 13, 4], [11, 14, 5], [10, 15, 6], [9, 8, 7]], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]],
    [[[1, 11], [2, 12], [3, 13], [4, 14], [5, 15], [6, 16], [7, 17], [8, 18], [9, 19], [10, 20]], [1, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 10, 9, 8, 7, 6, 5, 4, 3, 2]],
    [[[1, 3, 2, 5, 4, 7, 6]], [1, 3, 2, 5, 4, 7, 6]],
    [[[1], [3], [2], [5], [4], [7], [6]], [1, 3, 2, 5, 4, 7, 6]]
]

@pytest.mark.parametrize("array, expected", cases)
def test_spiralTraverse(array, expected):
    assert spiralTraverse(array)==expected

