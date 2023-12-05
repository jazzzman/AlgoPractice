"""
  DESCRIPTION

  Write a function that takes in an array of integers representing a stack,     
  recursively sorts the stack in place (i.e., doesn't create a brand new array),
  and returns it.


  The array must be treated as a stack, with the end of the array as the top of 
  the stack. Therefore, you're only allowed to
  
    Pop elements from the top of the stack by removing elements from the end of
    the array using the built-in .pop() method in your programming
    language of choice.
  
  
    Push elements to the top of the stack by appending elements to the end of
    the array using the built-in .append() method in your
    programming language of choice.
  
  
    Peek at the element on top of the stack by accessing the last element in the
    array.
  


  You're not allowed to perform any other operations on the input array,        
  including accessing elements (except for the last element), moving elements,  
  etc.. You're also not allowed to use any other data structures, and your      
  solution must be recursive.


  Time complexity O(n^2)
  Space complexity O(n)
"""
import pytest


def sortStack(stack):
    if len(stack) == 0:
        return stack

    top = stack.pop()
    sortStack(stack)

    insertSorted(stack, top)

    return stack

def insertSorted(stack, value):
    if len(stack)==0 or value>stack[-1]:
        stack.append(value)
        return
    
    top = stack.pop()
    insertSorted(stack,value)
    stack.append(top)


# case [stack, expected]
cases = [
    [[-5, 2, -2, 4, 3, 1], [-5, -2, 1, 2, 3, 4]],
    [[3, 4, 5, 1, 2], [1, 2, 3, 4, 5]],
    [[0, -2, 3, 4, 1, -9, 8], [-9, -2, 0, 1, 3, 4, 8]],
    [[2, 4, 22, 1, -9, 0, 6, 23, -2, 1], [-9, -2, 0, 1, 1, 2, 4, 6, 22, 23]],
    [[3, 4, 5, 1, 2], [1, 2, 3, 4, 5]],
    [[-1, 0, 2, 3, 4, 1, 1, 1], [-1, 0, 1, 1, 1, 2, 3, 4]],
    [[], []],
    [[1], [1]],
    [[10, 9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]],
    [[9, 2, 8, 1], [1, 2, 8, 9]],
    [[2, 33, 44, 2, -9, -7, -5, -2, -2, -2, 0], [-9, -7, -5, -2, -2, -2, 0, 2, 2, 33, 44]],
    [[3, 3, 3, 3, 3, 3], [3, 3, 3, 3, 3, 3]],
    [[0, 0], [0, 0]],
    [[2, 22, 222, 3, 33, 33, 9, 2, 3, 312, -9, -2, 3], [-9, -2, 2, 2, 3, 3, 3, 9, 22, 33, 33, 222, 312]],
    [[3, 4, 5, 1, 2, 2, 2, 1, 3, 4, 5, 3, 1, 3, -1, 2, 3], [-1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 5, 5]]
]

@pytest.mark.parametrize("stack, expected", cases)
def test_sortStack(stack, expected):
    assert sortStack(stack)==expected

