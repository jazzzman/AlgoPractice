"""
  DESCRIPTION

  You're given two positive integers representing the width and height of a
  grid-shaped, rectangular graph. Write a function that returns the number of
  ways to reach the bottom right corner of the graph when starting at the top
  left corner. Each move you take must either go down or right. In other words,
  you can never move up or left in the graph.


  Time complexity O(width*height)
  Space complexity O(width)
"""
import pytest


def numberOfWaysToTraverseGraph(width, height):
    W = [1]*width

    for y in range(1,height):
        for x in range(1,width):
            W[x] += W[x-1]
    
    return W[-1]

# Space complexity O(widht*height)
def numberOfWaysToTraverseGraph2(width, height):
    W = [[0]*width for _ in range(height)]
    W[0] = [1]*width
    for idx in range(height):
        W[idx][0] = 1

    for y in range(1,height):
        for x in range(1,width):
            W[y][x] = sum([W[y-1][x], W[y][x-1]])
    
    return W[-1][-1]


# case [width, height, expected]
cases = [
    [3, 4, 10],
    [2, 3, 3],
    [3, 2, 3],
    [5, 5, 70],
    [6, 5, 126],
    [5, 7, 210],
    [2, 10, 10],
    [2, 11, 11],
    [9, 5, 495],
    [7, 6, 462],
    [5, 8, 330],
    [2, 2, 2],
    [1, 2, 1],
    [2, 1, 1],
    [3, 3, 6]
]

@pytest.mark.parametrize("width, height, expected", cases)
def test_numberOfWaysToTraverseGraph(width, height, expected):
    assert numberOfWaysToTraverseGraph(width, height)==expected

