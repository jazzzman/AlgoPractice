"""
  DESCRIPTION

  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing only 0s and 1s. The matrix
  represents a two-toned image, where each 1 represents black and
  each 0 represents white. An island is defined as any number of
  1s that are horizontally or vertically adjacent (but not
  diagonally adjacent) and that don't touch the border of the image. In other  
  words, a group of horizontally or vertically adjacent 1s isn't an
  island if any of those 1s are in the first row, last row, first
  column, or last column of the input matrix.


  Note that an island can twist. In other words, it doesn't have to be a       
  straight vertical line or a straight horizontal line; it can be L-shaped, for
  example.


  You can think of islands as patches of black that don't touch the border of  
  the two-toned image.


  Write a function that returns a modified version of the input matrix, where  
  all of the islands are removed. You remove an island by replacing it with    
  0s.

Naturally, you're allowed to mutate the input matrix.



  Time complexity O(ROWS*COLS)
  Space complexity O(ROWS*COLS)
"""
import pytest

from icecream import ic


def removeIslands(matrix):
    visited = []
    ROWS = len(matrix)
    COLS = len(matrix[0])

    for row in range(ROWS):
        if matrix[row][0] == 1 and (row,0) not in visited:
            dfs(row, 0, matrix, visited)

    for col in range(COLS):
        if matrix[0][col] == 1 and (0, col) not in visited:
            dfs(0, col, matrix, visited)

    for row in range(ROWS):
        if matrix[row][COLS-1] == 1 and (row,COLS-1) not in visited:
            dfs(row, COLS-1, matrix, visited)

    for col in range(COLS):
        if matrix[ROWS-1][col] == 1 and (ROWS-1, col) not in visited:
            dfs(ROWS-1, col, matrix, visited)

    for row in range(1, ROWS-1):
        for col in range(1, COLS-1):
            if matrix[row][col]==1 and (row,col) not in visited:
                matrix[row][col] = 0

    return matrix


def dfs(row, col, matrix, visited):
    if matrix[row][col] == 1 and (row,col) not in visited:
        visited.append((row,col))
        for neighbour in get_neighbours(row,col,matrix):
            dfs(neighbour[0], neighbour[1], matrix, visited)


def get_neighbours(row, col, matrix):
    ROWS = len(matrix)
    COLS = len(matrix[0])
    candedates = [[row-1, col],[row+1, col], [row, col-1], [row, col+1]]
    return [[row,col] for row, col in candedates if 0<=row<ROWS and 0<=col<COLS]

# case [matrix, expected]
cases = [
    [[[1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 1, 1], [0, 0, 1, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 1, 1, 0, 0], [1, 0, 0, 0, 0, 1]], [[1, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 0, 0, 1, 0], [1, 1, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0], [1, 0, 0, 0, 0, 1]]],
    [[[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0], [0, 1, 0, 1, 0], [1, 0, 0, 0, 1]], [[1, 0, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [1, 0, 0, 0, 1]]],
    [[[1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [0, 0, 1, 1, 0]], [[1, 0, 0, 1, 0], [0, 0, 0, 1, 0], [0, 0, 1, 1, 0]]],
    [[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 0, 1, 0, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 0, 1, 0, 1]]],
    [[[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]],
    [[[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]],
    [[[1]], [[1]]],
    [[[1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 1, 0, 1, 0, 1, 0], [1, 1, 0, 1, 0, 0, 1, 0], [1, 1, 0, 1, 1, 0, 1, 0], [1, 0, 0, 0, 1, 0, 0, 0]], [[1, 0, 0, 0, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0], [1, 1, 0, 1, 0, 0, 0, 0], [1, 1, 0, 1, 1, 0, 0, 0], [1, 0, 0, 0, 1, 0, 0, 0]]],
    [[[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 1, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]], [[1, 1, 1, 1, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 0, 0, 0, 1], [1, 1, 1, 1, 1]]],
    [[[1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [1, 0, 1, 0, 1]], [[1, 0, 1, 0, 1], [0, 0, 1, 0, 0], [1, 1, 0, 1, 1], [0, 0, 1, 0, 0], [1, 0, 1, 0, 1]]],
    [[[0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 1, 1, 1, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]],
    [[[1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1]], [[1, 0, 1, 0, 1, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 0, 0, 0, 0], [0, 1, 0, 1, 0, 1]]],
    [[[1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 0, 1, 0, 1], [1, 0, 1, 0, 1, 0], [0, 1, 1, 1, 0, 1]], [[1, 0, 1, 1, 1, 0], [1, 1, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0], [0, 1, 1, 1, 0, 1]]],
    [[[0, 1, 0], [0, 1, 0], [1, 0, 0]], [[0, 1, 0], [0, 1, 0], [1, 0, 0]]],
    [[[1, 1], [1, 1]], [[1, 1], [1, 1]]],
    [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0 , 0, 0, 0], [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]], [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0 , 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]
]

@pytest.mark.parametrize("matrix, expected", cases)
def test_removeIslands(matrix, expected):
    assert removeIslands(matrix)==expected
