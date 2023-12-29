"""
  DESCRIPTION

  Write a function that takes in an integer matrix of potentially unequal height
  and width and returns the minimum number of passes required to convert all    
  negative integers in the matrix to positive integers.


  A negative integer in the matrix can only be converted to a positive integer  
  if one or more of its adjacent elements is positive. An adjacent element is an
  element that is to the left, to the right, above, or below the current element
  in the matrix. Converting a negative to a positive simply involves multiplying
  it by -1.


  Note that the 0 value is neither positive nor negative, meaning
  that a 0 can't convert an adjacent negative to a positive.


  A single pass through the matrix involves converting all the negative integers
  that can be converted at a particular point in time. For example,
  consider the following input matrix:

    [ 
      [0, -2, -1], 
      [-5, 2, 0], 
      [-6, -2, 0],
    ]

  After a first pass, only 3 values can be converted to positives:

    [ 
      [0, 2, -1], 
      [5, 2, 0], 
      [-6, 2, 0],
    ]

  After a second pass, the remaining negative values can all be converted to    
  positives:

    [ 
      [0, 2, 1], 
      [5, 2, 0], 
      [6, 2, 0],
    ]

  Note that the input matrix will always contain at least one element. If the   
  negative integers in the input matrix can't all be converted to positives,    
  regardless of how many passes are run, your function should return
  -1.



  Time complexity O(V)
  Space complexity O(V)
"""
import pytest

from icecream import ic


def minimumPassesOfMatrix(matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    passes = 0
    
    while has_negative(matrix):
        visited = set()
        modifications = 0
        for row in range(ROWS):
            for col in range(COLS):
                modifications += dfs(row,col,matrix,visited)
        passes+=1
        if modifications == 0:
            return -1

    return passes

def has_negative(matrix):
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col]<0:
                return True
    return False

def dfs(row,col,matrix,visited):
    if (row,col) in visited:
        return 0
    modifications = 0
    if matrix[row][col]>0:
        visited.add((row,col))
        for neighbour in get_neighbours(row,col,matrix):
            if matrix[neighbour[0]][neighbour[1]]<0:
                matrix[neighbour[0]][neighbour[1]]*=-1
                modifications += 1
                visited.add(tuple(neighbour))
    return modifications

def get_neighbours(row, col, matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    candidates = [[row-1,col],[row+1,col],[row,col-1],[row,col+1]]
    return [[row,col] for row,col in candidates if 0<=row<ROWS and 0<=col<COLS]


# case [matrix, expected]
cases = [
    [[[0, -1, -3, 2, 0], [1, -2, -5, -1, -3], [3, 0, 0, -4, -1]], 3],
    [[[1]], 0],
    [[[1, 0, 0, -2, -3], [-4, -5, -6, -2, -1], [0, 0, 0, 0, -1], [1, 2, 3, 0, -2]], 7],
    [[[1, 0, 0, -2, -3], [-4, -5, -6, -2, -1], [0, 0, 0, 0, -1], [1, 2, 3, 0, 3]], 4],
    [[[1, 0, 0, -2, -3], [-4, -5, -6, -2, -1], [0, 0, 0, 0, -1], [-1, 0, 3, 0, 3]], -1],
    [[[-1]], -1],
    [[[1, 2, 3], [4, 5, 6]], 0],
    [[[-1, -9, 0, -1, 0], [-9, -4, -5, 4, -8], [2, 0, 0, -3, 0], [0, -17, -4, 2, -5]], 3],
    [[[-2, -3, -4, -1, -9], [-4, -3, -4, -1, -2], [-6, -7, -2, -1, -1], [0, 0, 0, 0, -3], [1, -2, -3, -6, -1]], 12],
    [[[-1, 2, 3], [4, 5, 6]], 1],
    [[[-1, 2, 3], [4, -5, -6]], 1],
    [[[-1, 0, 3], [0, -5, -6]], -1],
    [[[-1, 0, 3], [0, -5, -6]], -1],
    [[[0, 0, -1, -2], [-2, -3, 4, -1], [-2, -3, 1, -3], [-14, -15, 2, 0], [0, 0, 0, 0], [1, -1, -1, -1]], 3],
    [[[0, 0, -1, -2], [-2, -3, 4, -1], [-2, -3, 1, -3], [-14, -15, 2, 0], [0, 0, 0, 0], [1, -1, -1, 1]], 2],
    [[[-2, 0, -2, 1], [-2, -1, -1, -1]], 5]
]

@pytest.mark.parametrize("matrix, expected", cases)
def test_minimumPassesOfMatrix(matrix, expected):
    ic(matrix)
    assert minimumPassesOfMatrix(matrix)==expected
