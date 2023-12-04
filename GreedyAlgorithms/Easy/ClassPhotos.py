"""
  DESCRIPTION

  It's photo day at the local school, and you're the photographer assigned to   
  take class photos. The class that you'll be photographing has an even number  
  of students, and all these students are wearing red or blue shirts. In fact,  
  exactly half of the class is wearing red shirts, and the other half is wearing
  blue shirts. You're responsible for arranging the students in two rows before 
  taking the photo. Each row should contain the same number of the students and 
  should adhere to the following guidelines:

    All students wearing red shirts must be in the same row.
    All students wearing blue shirts must be in the same row.
  
    Each student in the back row must be strictly taller than the student
    directly in front of them in the front row.

  You're given two input arrays: one containing the heights of all the students 
  with red shirts and another one containing the heights of all the students    
  with blue shirts. These arrays will always have the same length, and each     
  height will be a positive integer. Write a function that returns whether or   
  not a class photo that follows the stated guidelines can be taken.

  Note: you can assume that each class has at least 2 students.


  Time complexity O(nlogn)
  Space complexity O(n)
"""
import pytest


def classPhotos(blueShirtsHeights, redShirtsHeights):
    blueShirtsHeights.sort()
    redShirtsHeights.sort()
    
    return (all([red>blue for red, blue in zip(redShirtsHeights, blueShirtsHeights)]) or
            all([blue>red for red, blue in zip(redShirtsHeights, blueShirtsHeights)]))



# case [blueShirtsHeights, redShirtsHeights, expected]
cases = [
    [[6, 9, 2, 4, 5], [5, 8, 1, 3, 4], True],
    [[5, 8, 1, 3, 4], [6, 9, 2, 4, 5], True],
    [[5, 8, 1, 3, 4, 9], [6, 9, 2, 4, 5, 1], False],
    [[6], [6], False],
    [[125], [126], True],
    [[2, 3, 4, 5, 6], [1, 2, 3, 4, 5], True],
    [[5, 6, 7, 2, 3, 1, 2, 3], [1, 1, 1, 1, 1, 1, 1, 1], False],
    [[2, 2, 2, 2, 2, 2, 2, 2], [1, 1, 1, 1, 1, 1, 1, 1], True],
    [[126], [125], True],
    [[21, 5, 4, 4, 4, 4, 4, 4, 4], [19, 2, 4, 6, 2, 3, 1, 1, 4], False],
    [[20, 5, 4, 4, 4, 4, 4, 4], [19, 19, 21, 1, 1, 1, 1, 1], False],
    [[2, 4, 7, 5, 1], [3, 5, 6, 8, 2], True],
    [[2, 4, 7, 5, 1, 6], [3, 5, 6, 8, 2, 1], False],
    [[5, 4], [4, 5], False],
    [[5, 4], [5, 6], True]
]

@pytest.mark.parametrize("blueShirtsHeights, redShirtsHeights, expected", cases)
def test_classPhotos(blueShirtsHeights, redShirtsHeights, expected):
    assert classPhotos(blueShirtsHeights, redShirtsHeights)==expected

