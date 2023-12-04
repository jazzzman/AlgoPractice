"""
  DESCRIPTION

  You're given two positive integers representing the height of a staircase and
  the maximum number of steps that you can advance up the staircase at a time. 
  Write a function that returns the number of ways in which you can climb the  
  staircase.


  For example, if you were given a staircase of height = 3 and
  maxSteps = 2 you could climb the staircase in 3 ways. You could
  take 1 step, 1 step, then 1 step, you could also take
  1 step, then 2 steps, and you could take 2 steps, then 1 step.

  Note that maxSteps <= height will always be true.

  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


def staircaseTraversal(height, maxSteps):
    steps = [0]*(height+1)
    steps[0]=1

    for i in range(len(steps)):
        for s in range(1,maxSteps+1):
            if i-s>=0:
                steps[i]+=steps[i-s]
    
    return steps[-1]


# case [height, maxSteps, expected]
cases = [
    [4, 2, 5],
    [10, 1, 1],
    [10, 2, 89],
    [4, 3, 7],
    [1, 1, 1],
    [5, 2, 8],
    [4, 4, 8],
    [6, 2, 13],
    [100, 1, 1],
    [15, 5, 13624],
    [7, 2, 21],
    [6, 3, 24],
    [3, 2, 3]
]

@pytest.mark.parametrize("height, maxSteps, expected", cases)
def test_staircaseTraversal(height, maxSteps, expected):
    assert staircaseTraversal(height, maxSteps)==expected

