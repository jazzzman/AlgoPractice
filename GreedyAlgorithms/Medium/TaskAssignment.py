"""
  DESCRIPTION

  You're given an integer k representing a number of workers and an
  array of positive integers representing durations of tasks that must be       
  completed by the workers. Specifically, each worker must complete two unique  
  tasks and can only work on one task at a time. The number of tasks will always
  be equal to 2k such that each worker always has exactly two tasks
  to complete. All tasks are independent of one another and can be completed in 
  any order. Workers will complete their assigned tasks in parallel, and the    
  time taken to complete all tasks will be equal to the time taken to complete  
  the longest pair of tasks (see the sample output for an explanation).


  Write a function that returns the optimal assignment of tasks to each worker  
  such that the tasks are completed as fast as possible. Your function should   
  return a list of pairs, where each pair stores the indices of the tasks that  
  should be completed by one worker. The pairs should be in the following       
  format: [task1, task2], where the order of task1 and
  task2 doesn't matter. Your function can return the pairs in any
  order. If multiple optimal assignments exist, any correct answer will be      
  accepted.


  Note: you'll always be given at least one worker (i.e., k will
  always be greater than 0).

  Time complexity O(nlogn)
  Space complexity O(n)
"""
import pytest


def taskAssignment(k, tasks):
    task_indecies = {}
    for idx,task in enumerate(tasks):
        if task in task_indecies:
            task_indecies[task].append(idx)
        else:
            task_indecies[task] = [idx]

    tasks.sort()
    workers = []
    for worker in range(k):
        workers.append([task_indecies[tasks.pop(0)].pop(0), task_indecies[tasks.pop()].pop(0)])

    return workers


# case [k, tasks, expected]
cases = [
    [3, [1, 3, 5, 3, 1, 4], [[4, 2], [0, 5], [3, 1]]],
    [4, [1, 2, 3, 4, 5, 6, 7, 8], [[0, 7], [1, 6], [2, 5], [3, 4]]],
    [5, [1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [[9, 8], [7, 6], [5, 4], [3, 2], [1, 0]]],
    [1, [3, 5], [[0, 1]]],
    [7, [2, 1, 3, 4, 5, 13, 12, 9, 11, 10, 6, 7, 14, 8], [[1, 12], [0, 5], [2, 6], [3, 8], [4, 9], [10, 7], [11, 13]]],
    [5, [3, 7, 5, 4, 4, 3, 6, 8, 3, 3], [[9, 7], [8, 1], [5, 6], [0, 2], [4, 3]]],
    [10, [5, 6, 2, 3, 15, 15, 16, 19, 2, 10, 10, 3, 3, 32, 12, 1, 23, 32, 9, 2], [[15, 17], [19, 13], [8, 16], [2, 7], [12, 6], [11, 5], [3, 4], [0, 14], [1, 10], [18, 9]]],
    [4, [1, 2, 2, 1, 3, 4, 4, 4], [[3, 7], [0, 6], [2, 5], [1, 4]]],
    [3, [87, 65, 43, 32, 31, 320], [[4, 5], [3, 0], [2, 1]]],
    [2, [3, 4, 5, 3], [[3, 2], [0, 1]]],
    [3, [5, 2, 1, 6, 4, 4], [[2, 3], [1, 0], [5, 4]]],
    [2, [1, 8, 9, 10], [[0, 3], [1, 2]]]
]

@pytest.mark.parametrize("k, tasks, expected", cases)
def test_taskAssignment(k, tasks, expected):
    tasks_dumb = list(tasks)
    maxProcessed = max([tasks_dumb[one]+tasks_dumb[two] for one,two in taskAssignment(k, tasks)])
    maxExpected = max([tasks_dumb[one]+tasks_dumb[two] for one,two in expected])
    assert maxProcessed == maxExpected

