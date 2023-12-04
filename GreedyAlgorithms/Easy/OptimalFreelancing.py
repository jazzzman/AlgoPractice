"""
  DESCRIPTION

    You recently started freelance software development and have been offered    
    a variety of job opportunities. Each job has a deadline, meaning there is no 
    value in completing the work after the deadline. Additionally, each job      
    has an associated payment representing the profit for completing that job.   
    Given this information, write a function that returns the maximum profit that
    can be obtained in a 7-day period.


    Each job will take 1 full day to complete, and the deadline will be given    
    as the number of days left to complete the job. For example, if a job has a  
    deadline of 1, then it can only be completed if it is the first job worked   
    on. If a job has a deadline of 2, then it could be started on the first or   
    second day.


    Note: There is no requirement to complete all of the jobs. Only one job can  
    be worked on at a time, meaning that in some scenarios it will be impossible 
    to complete them all.


  Time complexity O(nlogn)
  Space complexity O(1)
"""
import pytest


def optimalFreelancing(jobs):
    if not jobs:
        return 0
    slot = {day:None for day in range(1,8)}
    jobs = sorted(jobs, key= lambda kvp: kvp['payment'], reverse=True)
    while jobs: 
        day = jobs.pop(0)
        day['deadline'] = min(7, day['deadline'])
        while day['deadline']>0 and slot[day['deadline']] is not None:
            day['deadline']-=1
        if day['deadline'] in slot:
            slot[day['deadline']] = day['payment']
        if all([v is not None for v in slot.values()]):
            break

    return sum([val for val in slot.values() if val is not None])


# case [jobs, expected]
cases = [
    [[], 0],
    [[{'deadline': 1, 'payment': 1}], 1],
    [[{'deadline': 1, 'payment': 2}, {'deadline': 1, 'payment': 1}], 2],
    [[{'deadline': 1, 'payment': 1}, {'deadline': 1, 'payment': 2}], 2],
    [[{'deadline': 1, 'payment': 1}, {'deadline': 2, 'payment': 1}], 2],
    [[{'deadline': 1, 'payment': 1}, {'deadline': 2, 'payment': 2}, {'deadline': 2, 'payment': 1}], 3],
    [[{'deadline': 8, 'payment': 3}, {'deadline': 1, 'payment': 1}, {'deadline': 1, 'payment': 2}], 5],
    [[{'deadline': 2, 'payment': 2}, {'deadline': 4, 'payment': 3}, {'deadline': 5, 'payment': 1}, {'deadline': 7, 'payment': 2}, {'deadline': 3, 'payment': 1}, {'deadline': 3, 'payment': 2}, {'deadline': 1, 'payment': 3}], 13],
    [[{'deadline': 2, 'payment': 1}, {'deadline': 2, 'payment': 2}, {'deadline': 2, 'payment': 3}, {'deadline': 2, 'payment': 4}, {'deadline': 2, 'payment': 5}, {'deadline': 2, 'payment': 6}, {'deadline': 2, 'payment': 7}], 13],
    [[{'deadline': 8, 'payment': 1}, {'deadline': 6, 'payment': 4}, {'deadline': 1, 'payment': 2}, {'deadline': 1, 'payment': 3}, {'deadline': 2, 'payment': 3}, {'deadline': 5, 'payment': 2}], 13],
    [[{'deadline': 2, 'payment': 1}, {'deadline': 1, 'payment': 4}, {'deadline': 3, 'payment': 2}, {'deadline': 1, 'payment': 3}, {'deadline': 4, 'payment': 3}, {'deadline': 4, 'payment': 2}, {'deadline': 4, 'payment': 1}, {'deadline': 5, 'payment': 4}, {'deadline': 8, 'payment': 1}], 16],
    [[{'deadline': 10, 'payment': 1}], 1],
    [[{'deadline': 1, 'payment': 1}, {'deadline': 2, 'payment': 1}, {'deadline': 3, 'payment': 1}, {'deadline': 4, 'payment': 1}, {'deadline': 5, 'payment': 1}, {'deadline': 6, 'payment': 1}, {'deadline': 7, 'payment': 1}, {'deadline': 8, 'payment': 1}, {'deadline': 9, 'payment': 1}, {'deadline': 10, 'payment': 1}], 7]
]

@pytest.mark.parametrize("jobs, expected", cases)
def test_optimalFreelancing(jobs, expected):
    assert optimalFreelancing(jobs)==expected

