"""
  DESCRIPTION

    You're given a 2D array of integers <span>matrix</span>. Write a function
    that returns the transpose of the matrix.
 
    The transpose of a matrix is a flipped version of the original matrix across
    its main diagonal (which runs from top-left to bottom-right); it switches
    the row and column indices of the original matrix.
 
    You can assume the input matrix always has at least 1 value; however its
    width and height are not necessarily the same.
    

  Time complexity O(rows*cols)
  Space complexity O(rows*cols)
"""
import pytest


def transposeMatrix(matrix):
    W = len(matrix[0])
    H = len(matrix)
    transpose = [[0]*H for _ in range(W)]
    for row in range(H):
        for col in range(W): 
            transpose[col][row] = matrix[row][col]
    return transpose


cases = [
    [[[1]], [[1]]],
    [[[1], [-1]], [[1, -1]]],
    [[[1, 2, 3]], [[1], [2], [3]]],
    [[[1], [2], [3]], [[1, 2, 3]]],
    [[[1, 2, 3], [4, 5, 6]], [[1, 4], [2, 5], [3, 6]]],
    [[[0, 0, 0], [1, 1, 1]], [[0, 1], [0, 1], [0, 1]]],
    [[[0, 1], [0, 1], [0, 1]], [[0, 0, 0], [1, 1, 1]]],
    [[[0, 0, 0], [0, 0, 0]], [[0, 0], [0, 0], [0, 0]]],
    [[[1, 4], [2, 5], [3, 6]], [[1, 2, 3], [4, 5, 6]]],
    [[[-7, -7], [100, 12], [-33, 17]], [[-7, 100, -33], [-7, 12, 17]]],
    [[[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 4, 7], [2, 5, 8], [3, 6, 9]]],
    [[[1, 4, 7], [2, 5, 8], [3, 6, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]],
    [[[5, 6, 3, -3, 12], [-3, 6, 5, 2, -1], [0, 0, 3, 12, 3]], [[5, -3, 0], [6, 6, 0], [3, 5, 3], [-3, 2, 12], [12, -1, 3]]],
    [[[0, -1, -2, -3], [4, 5, 6, 7], [2, 3, -2, -3], [42, 100, 30, -42]], [[0, 4, 2, 42], [-1, 5, 3, 100], [-2, 6, -2, 30], [-3, 7, -3, -42]]],
    [[[1234, 6935, 4205], [-23459, 314159, 0], [100, 3, 987654]], [[1234, -23459, 100], [6935, 314159, 3], [4205, 0, 987654]]]
]

@pytest.mark.parametrize("matrix, expected",cases)
def test_transposeMatrix(matrix, expected):
    assert transposeMatrix(matrix)==expected

