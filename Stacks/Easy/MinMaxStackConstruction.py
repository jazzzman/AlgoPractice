"""
  DESCRIPTION

  Write a MinMaxStack class for a Min Max Stack. The class should
  support:

    Pushing and popping values on and off the stack.
    
    Peeking at the value at the top of the stack.
  
    Getting both the minimum and the maximum values in the stack at any given
    point in time.
  

  All class methods, when considered independently, should run in constant time
  and with constant space.

  Time complexity O(n) - building, peek, pop, getMin, getMax O(1)
  Space complexity O(n)
"""
import pytest


class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.max_idx = []
        self.min_idx = []

    def peek(self):
        return self.stack[-1]

    def push(self, value):
        self.stack.append(value)
        if len(self.max_idx)==0 or value >= self.stack[self.max_idx[-1]]:
            self.max_idx.append(len(self.stack)-1)

        if len(self.min_idx)==0 or value <= self.stack[self.min_idx[-1]]:
            self.min_idx.append(len(self.stack)-1)

    def pop(self):
        if len(self.stack)-1==self.max_idx[-1]:
            self.max_idx.pop()
            return self.stack.pop()

        return self.stack.pop()

    def getMin(self):
        if self.min_idx:
            return self.stack[self.min_idx[-1]]
        return None

    def getMax(self):
        if self.max_idx:
            return self.stack[self.max_idx[-1]]
        return None





def constructMinMaxStack(data, procedures) -> MinMaxStack:
    minmaxStack = MinMaxStack()
    for value in data:
        minmaxStack.push(value)
    return minmaxStack


# case [data, procedures, expected]
cases = [
    [
        [0,1,2,4,5],
        [ {'pop': 5}, {'getMax': 4}, {'getMin': 0}, {'peek': 4}, {'push': 7}, {'push': -3}, {'peek': -3}, {'getMin': -3}, {'getMax': 7}],
        [5, 4, 0, 4, -3, -3, 7]
    ]
]

@pytest.mark.parametrize("data, procedures, expected", cases)
def test_constructMinMaxStack(data, procedures, expected):
    minMaxStack = constructMinMaxStack(data, procedures)
    for operation, exp_result in zip(procedures,expected):
        operation, oper_value = list(operation.items())[0]
        if operation == 'push':
            minMaxStack.push(oper_value)
        else:
            result = None
            if operation == 'pop':
                result = minMaxStack.pop()
            elif operation == 'peek':
                result = minMaxStack.peek()
            elif operation == 'getMax':
                result = minMaxStack.getMax()
            elif operation == 'getMin':
                result = minMaxStack.getMin()
            
            assert result == oper_value


