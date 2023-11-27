"""
  DESCRIPTION

  You walk into a theatre you're about to see a show in. The usher within the
  theatre walks you to your row and mentions you're allowed to sit anywhere
  within the given row. Naturally you'd like to sit in the seat that gives you
  the most space. You also would prefer this space to be evenly distributed on
  either side of you (e.g. if there are three empty seats in a row, you would
  prefer to sit in the middle of those three seats).

  Given the theatre row represented as an integer array, return
  the seat index of where you should sit. Ones represent occupied seats and zeroes
  represent empty seats.

  You may assume that someone is always sitting in the
  first and last seat of the row. Whenever there are two equally good seats,
  you should sit in the seat with the lower index. If there is no seat to sit
  in, return -1. The given array will always have a length of at least one
  and contain only ones and zeroes.


  Time complexity O(n)
  Space complexity O(1)
"""
import pytest


def bestSeat(seats):
    left_ptr,right_ptr = 0,1
    idx=-1
    prev_space = 0
    while right_ptr<len(seats):
        if seats[right_ptr]<seats[right_ptr-1]:
            left_ptr=right_ptr
        elif seats[right_ptr]>seats[right_ptr-1]:
            if right_ptr-left_ptr  > prev_space:
                prev_space = right_ptr-left_ptr
                idx = left_ptr+(prev_space-1)//2
        right_ptr += 1
    return idx


# case [seats, expected]
cases = [
    [[1], -1],
    [[1, 0, 1, 0, 0, 0, 1], 4],
    [[1, 0, 1], 1],
    [[1, 0, 0, 1], 1],
    [[1, 1, 1], -1],
    [[1, 0, 0, 1, 0, 0, 1], 1],
    [[1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 3],
    [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1], 4],
    [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 4],
    [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1], 13],
    [[1, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1], 13],
    [[1, 0, 0, 0, 1, 0, 0, 0, 0, 1], 6],
    [[1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1], 3],
    [[1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 0, 0, 1], 5]
]

@pytest.mark.parametrize("seats, expected", cases)
def test_bestSeat(seats, expected):
    assert bestSeat(seats)==expected

