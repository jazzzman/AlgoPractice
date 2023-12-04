"""
  DESCRIPTION

    In the game of Blackjack, the dealer must draw cards until the sum of the   
    values of their cards is greater than or equal to a
    target value minus 4. For example, traditional Blackjack uses a
    target value of 21, so the dealer must draw cards until their
    total is greater than or equal to 17, at which point they stop drawing cards
    (they "stand"). If the dealer draws a card that brings their total above the
    target (above 21 in traditional Blackjack), they lose (they
    "bust").


    Naturally, when a dealer is drawing cards, they can either end up standing  
    or busting, and this is entirely up to the luck of their draw.


    Write a function that takes in a target value as well as a
    dealer's startingHand value and returns the probability that
    the dealer will bust (go over the target value before
    standing). The target value will always be a positive integer,
    and the startingHand value will always be a positive integer
    that's smaller than or equal to the target value.


    For simplicity, you can assume that the dealer has an infinite deck of cards
    and that each card has a value between 1 and 10 inclusive. The likelihood of
    drawing a card of any value is always the same, regardless of previous      
    draws.


    Your solution should be rounded to 3 decimal places and to the nearest      
    value. For example, a probability of 0.314159 would be rounded
    to 0.314, while a probability of 0.1337 would be
    rounded to 0.134.


  Time complexity O(target-startingHand)
  Space complexity O(target-startingHand)
"""
import pytest


def blackjackProbability(startingHand, target):
    memo = {}
    return round(helper(startingHand, target, memo),3)

def helper(startingHand, target, memo):
    if startingHand>target:
        return 1
    if target-4<=startingHand<=target:
        return 0
    if startingHand in memo:
        return memo[startingHand]

    probability = 0
    for card in range(1,11):
        probability += 1/10*blackjackProbability(startingHand+card,target)

    memo[startingHand]=probability

    return probability


# case [target, startingHand, expected]
cases = [
    [16, 21, 0.5],
    [21, 21, 0],
    [20, 21, 0],
    [17, 21, 0],
    [15, 21, 0.45],
    [12, 21, 0.268],
    [5, 21, 0.295],
    [1, 21, 0.261],
    #[95, 100, 0.5],
    #[90, 100, 0.195],
    #[20, 100, 0.273],
    [100, 100, 0],
    [1, 10, 0.268],
    [3, 10, 0.395],
    #[3, 30, 0.271],
    [7, 30, 0.276],
    [15, 30, 0.314],
    [25, 30, 0.5]
]

@pytest.mark.parametrize("target, startingHand, expected", cases)
def test_blackjackProbability(target, startingHand, expected):
    assert blackjackProbability(target, startingHand)==expected

