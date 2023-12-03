"""
  DESCRIPTION

  The Fibonacci sequence is defined as follows: the first number of the sequence
  is 0, the second number is 1, and the nth number is the sum of the (n - 1)th  
  and (n - 2)th numbers. Write a function that takes in an integer
  n and returns the nth Fibonacci number.


  Important note: the Fibonacci sequence is often defined with its first two    
  numbers as F0 = 0 and F1 = 1. For the purpose of
  this question, the first Fibonacci number is F0; therefore,
  getNthFib(1) is equal to F0, getNthFib(2)
  is equal to F1, etc..


  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def getNthFib(n):
    prevs = [0,1]
    if n<=1:
        return prevs[n-1]

    for val in range(n-2):
        prevs[1],prevs[0]=sum(prevs),prevs[1]

    return prevs[1]


# case [n, expected]
cases = [
    [6, 5],
    [1, 0],
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 3],
    [7, 8],
    [8, 13],
    [9, 21],
    [10, 34],
    [11, 55],
    [12, 89],
    [13, 144],
    [14, 233],
    [15, 377],
    [16, 610],
    [17, 987],
    [18, 1597]
]

@pytest.mark.parametrize("n, expected", cases)
def test_getNthFib(n, expected):
    assert getNthFib(n)==expected

