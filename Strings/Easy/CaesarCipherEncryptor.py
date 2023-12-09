"""
  DESCRIPTION

  Given a non-empty string of lowercase letters and a non-negative integer  
  representing a key, write a function that returns a new string obtained by
  shifting every letter in the input string by k positions in the alphabet, 
  where k is the key.


  Note that letters should "wrap" around the alphabet; in other words, the  
  letter z shifted by one returns the letter a.


  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def caesarCypherEncryptor(key, string):

    num = ord('z')-ord('a')+1
    return ''.join([chr( ord('a') + (ord(ch)+key - ord('a'))%num) for ch in string])

# case [key, string, expected]
cases = [
    [2, 'xyz', 'zab'],
    [0, 'abc', 'abc'],
    [3, 'abc', 'def'],
    [5, 'xyz', 'cde'],
    [26, 'abc', 'abc'],
    [52, 'abc', 'abc'],
    [57, 'abc', 'fgh'],
    [25, 'xyz', 'wxy'],
    [25, 'iwufqnkqkqoolxzzlzihqfm', 'hvtepmjpjpnnkwyykyhgpel'],
    [52, 'ovmqkwtujqmfkao', 'ovmqkwtujqmfkao'],
    [7, 'mvklahvjcnbwqvtutmfafkwiuagjkzmzwgf', 'tcrshocqjuidxcabatmhmrdpbhnqrgtgdnm'],
    [15, 'kjwmntauvjjnmsagwgawkagfuaugjhawgnawgjhawjgawbfawghesh', 'zylbcipjkyycbhpvlvplzpvujpjvywplvcplvywplyvplquplvwthw']
]

@pytest.mark.parametrize("key, string, expected", cases)
def test_caesarCypherEncryptor(key, string, expected):
    assert caesarCypherEncryptor(key, string)==expected
