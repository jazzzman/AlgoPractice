"""
  DESCRIPTION

  You're given a non-empty array of positive integers representing the amounts  
  of time that specific queries take to execute. Only one query can be executed 
  at a time, but the queries can be executed in any order.


  A query's waiting time is defined as the amount of time that it must
  wait before its execution starts. In other words, if a query is executed      
  second, then its waiting time is the duration of the first query; if a query  
  is executed third, then its waiting time is the sum of the durations of the   
  first two queries.


  Write a function that returns the minimum amount of total waiting time for all
  of the queries. For example, if you're given the queries of durations
  [1, 4, 5], then the total waiting time if the queries were
  executed in the order of [5, 1, 4] would be
  (0) + (5) + (5 + 1) = 11. The first query of duration
  5 would be executed immediately, so its waiting time would be
  0, the second query of duration 1 would have to wait
  5 seconds (the duration of the first query) to be executed, and
  the last query would have to wait the duration of the first two queries before
  being executed.

  Note: you're allowed to mutate the input array.


  Time complexity O(nlogn)
  Space complexity O(1)
"""
import pytest


def minimumWaitingTime(queries):
    queries.sort()
    waiting_time = 0
    for i in range(1,len(queries)):
        waiting_time += sum(queries[:i])
    return waiting_time


# case [queries, expected]
cases = [
    [[3, 2, 1, 2, 6], 17],
    [[2, 1, 1, 1], 6],
    [[1, 2, 4, 5, 2, 1], 23],
    [[25, 30, 2, 1], 32],
    [[1, 1, 1, 1, 1], 10],
    [[7, 9, 2, 3], 19],
    [[4, 3, 1, 1, 3, 2, 1, 8], 45],
    [[2], 0],
    [[7], 0],
    [[8, 9], 8],
    [[1, 9], 1],
    [[5, 4, 3, 2, 1], 20],
    [[1, 2, 3, 4, 5], 20],
    [[1, 1, 1, 4, 5, 6, 8, 1, 1, 2, 1], 81],
    [[17, 4, 3], 10]
]

@pytest.mark.parametrize("queries, expected", cases)
def test_minimumWaitingTime(queries, expected):
    assert minimumWaitingTime(queries)==expected

