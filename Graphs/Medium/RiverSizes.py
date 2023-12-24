"""
  DESCRIPTION

  You're given a two-dimensional array (a matrix) of potentially unequal height
  and width containing only 0s and 1s. Each
  0 represents land, and each 1 represents part of a
  river. A river consists of any number of 1s that are either
  horizontally or vertically adjacent (but not diagonally adjacent). The number
  of adjacent 1s forming a river determine its size.


  Note that a river can twist. In other words, it doesn't have to be a straight
  vertical line or a straight horizontal line; it can be L-shaped, for example.


  Write a function that returns an array of the sizes of all rivers represented
  in the input matrix. The sizes don't need to be in any particular order.     
    [[1, 0, 0, 1, 0], 
     [1, 0, 1, 0, 0], 
     [0, 0, 1, 0, 1], 
     [1, 0, 1, 0, 1], 
     [1, 0, 1, 1, 0]]

    [2,1,5,2,2]

  Time complexity O(N*M)
  Space complexity O(N*M)
"""
import pytest

from icecream import ic


def riverSizes(matrix):
    visited = set()
    sizes = []
    COLS = len(matrix[0])
    ROWS = len(matrix)
    for row in range(ROWS):
        for column in range(COLS):
            if matrix[row][column] == 1 and (row,column) not in visited:
                sizes.append(0)
                dfs(row,column,sizes, matrix, visited)

    return sorted(sizes)

def dfs(row, column, sizes, matrix, visited):
    if matrix[row][column]==1 and (row,column) not in visited:
        sizes[-1] += 1
        visited.add((row,column))
        for neighbours in get_neighbours(row,column,matrix):
            dfs(neighbours[0],neighbours[1],sizes,matrix,visited)

def get_neighbours(row,column,matrix):
    COLS = len(matrix[0])
    ROWS = len(matrix)
    candidates=[[row-1,column],[row+1,column],[row,column-1],[row,column+1]]
    return [[r,c] for r,c in candidates if 0<=r<ROWS and 0<=c<COLS]


# case [matrix, expected]
cases = [
[[[1, 0, 0, 1, 0], [1, 0, 1, 0, 0], [0, 0, 1, 0, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0]], [2, 1, 5, 2, 2]],
[[[0]], []],
[[[1]], [1]],
[[[1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0]], [3, 2, 1]],
[[[1, 0, 0, 1], [1, 0, 1, 0], [0, 0, 1, 0], [1, 0, 1, 0]], [2, 1, 3, 1]],
[[[1, 0, 0, 1, 0, 1, 0, 0, 1, 1, 1, 0], [1, 0, 1, 0, 0, 1, 1, 1, 1, 0, 1, 0], [0, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1], [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0], [1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1]], [2, 1, 21,
5, 2, 1]],
[[[1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 0, 1, 0, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 1]], [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
,
[[[1, 0, 0, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 1, 0, 0], [0, 0, 1, 0, 1, 0, 0], [0, 1, 0, 0, 0, 1, 0], [1, 0, 0, 0, 0, 0, 1]], [1, 1, 1, 1, 7, 1, 1, 1, 1]],
[[[0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0]], []],
[[[1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1]], [49]],
[[[1, 1, 0, 0, 0, 0, 1, 1], [1, 0, 1, 1, 1, 1, 0, 1], [0, 1, 1, 0, 0, 0, 1, 1]], [3, 5, 6]],
[[[1, 1, 0], [1, 0, 1], [1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 1, 0], [1, 0, 0], [1, 0, 0], [0, 0, 0], [1, 0, 0], [1, 0, 1], [1, 1, 1]], [10, 1, 1, 2, 6]]
]

@pytest.mark.parametrize("matrix, expected", cases)
def test_riverSizes(matrix, expected):
    assert riverSizes(matrix)==sorted(expected)
