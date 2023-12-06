"""
  DESCRIPTION

    You're given a list of string tokens representing a mathematical
    expression using Reverse Polish Notation. Reverse Polish Notation is a    
    notation where operators come after operands, instead of between them. For
    example 2 4 + would evaluate to 6.


    Parenthesis are always implicit in Reverse Polish Notation, meaning an    
    expression is evaluated from left to right. All of the operators for this 
    problem take two operands, which will always be the two values immediately
    preceding the operator. For example, 18 4 - 7 / would
    evaluate to ((18 - 4) / 7) or 2.


    Write a function that takes this list of tokens and returns
    the result. Your function should support four operators: +,
    -, *, and / for addition,
    subtraction, multiplication, and division respectively.


    Division should always be treated as integer division, rounding towards   
    zero. For example, 3 / 2 evaluates to 1 and
    -3 / 2 evaluates to -1. You can assume the
    input will always be valid Reverse Polish Notation, and it will always    
    result in a valid number. Your code should not edit this input list.      



  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def reversePolishNotation(tokens):
    numbers = []
    while tokens:
        token = tokens.pop(0)
        if token == '*':
            result = numbers.pop() * numbers.pop()
        elif token == '/':
            den = numbers.pop()
            result = int(numbers.pop()/den)
        elif token == '+':
            result = numbers.pop() + numbers.pop()
        elif token == '-':
            result = -1*(numbers.pop() - numbers.pop())
        else:
            numbers.append(int(token))
            continue
        numbers.append(result)

    return numbers.pop()


# case [tokens, expected]
cases = [
    [['10'], 10],
    [['10', '5', '+'], 15],
    [['10', '5', '-'], 5],
    [['10', '5', '/'], 2],
    [['10', '5', '*'], 50],
    [['10', '-5', '*'], -50],
    [['-10', '5', '*'], -50],
    [['-10', '-5', '*'], 50],
    [['10', '-5', '/'], -2],
    [['-10', '5', '/'], -2],
    [['-10', '-5', '/'], 2],
    [['10', '3', '/'], 3],
    [['10', '-3', '/'], -3],
    [['10', '-5', '+'], 5],
    [['-10', '5', '+'], -5],
    [['-10', '-5', '+'], -15],
    [['10', '-5', '-'], 15],
    [['-10', '5', '-'], -15],
    [['-10', '-5', '-'], -5],
    [['3', '2', '+', '7', '*'], 35],
    [['4', '2', '/', '7', '-'], -5],
    [['3', '4', '+', '2', '/', '4', '-'], -1],
    [['4', '-7', '2', '6', '+', '10', '-', '/', '*', '2', '+', '3', '*'], 42],
    [['4', '-7', '2', '6', '+', '10', '-', '/', '*', '2', '+', '3', '*', '0', '*'], 0],
    [['50', '3', '17', '+', '2', '-', '/'], 2],
    [['0', '3', '17', '+', '2', '-', '/'], 0],
    [['0', '3', '17', '+', '2', '-', '/', '2', '-', '7', '10', '+', '*'], -34]
]

@pytest.mark.parametrize("tokens, expected", cases)
def test_reversePolishNotation(tokens, expected):
    assert reversePolishNotation(tokens)==expected

