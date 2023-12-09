"""
  DESCRIPTION

  Write a function that takes in a string of lowercase English-alphabet letters
  and returns the index of the string's first non-repeating character.


  The first non-repeating character is the first character in a string that    
  occurs only once.


  If the input string doesn't have any non-repeating characters, your function 
  should return -1.


  Time complexity O(n)
  Space complexity O(1) 1 - thanks to only alphabet characters, which is only 26
"""
import pytest


def firstNonRepeatingCharacter(string):
    if not string:
        return -1
    chars = {}
    for i, ch in enumerate(string):
        if ch not in chars:
            chars[ch] = i
        else:
            chars[ch] = len(string)

    min_idx = min(chars.values())
    return min_idx if min_idx<len(string) else -1


# case [string, expected]
cases = [
    ['abcdcaf', 1],
    ['faadabcbbebdf', 6],
    ['a', 0],
    ['ab', 0],
    ['abc', 0],
    ['abac', 1],
    ['ababac', 5],
    ['ababacc', -1],
    ['lmnopqldsafmnopqsa', 7],
    ['abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy', 25],
    ['abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz', -1],
    ['', -1],
    ['ggyllaylacrhdzedddjsc', 10],
    ['aaaaaaaaaaaaaaaaaaaabbbbbbbbbbcccccccccccdddddddddddeeeeeeeeffghgh', -1],
    ['aabbccddeeff', -1]
]

@pytest.mark.parametrize("string, expected", cases)
def test_firstNonRepeatingCharacter(string, expected):
    assert firstNonRepeatingCharacter(string)==expected
