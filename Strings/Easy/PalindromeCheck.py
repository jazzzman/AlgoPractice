"""
  DESCRIPTION

  Write a function that takes in a non-empty string and that returns a boolean
  representing whether the string is a palindrome.


  A palindrome is defined as a string that's written the same forward and     
  backward. Note that single-character strings are palindromes.



  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


def isPalindrome(string):
    left, right = 0, len(string)-1
    while left<=len(string)//2:
        if string[left]!=string[right]:
            return False
        left+=1
        right-=1
    return True


# case [string, expected]
cases = [
    ['abcdcba', True],
    ['a', True],
    ['ab', False],
    ['aba', True],
    ['abb', False],
    ['abba', True],
    ['abcdefghhgfedcba', True],
    ['abcdefghihgfedcba', True],
    ['abcdefghihgfeddcba', False]
]

@pytest.mark.parametrize("string, expected", cases)
def test_isPalindrome(string, expected):
    assert isPalindrome(string)==expected
