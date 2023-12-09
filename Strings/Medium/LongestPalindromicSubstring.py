"""
  DESCRIPTION

  Write a function that, given a string, returns its longest palindromic 
  substring.


  A palindrome is defined as a string that's written the same forward and
  backward. Note that single-character strings are palindromes.

You can assume that there will only be one longest palindromic substring.

  Time complexity O(n^2)
  Space complexity O(1)
"""
import pytest


def longestPalindromicSubstring(string):
    max_dict = {}
    max_dict['max_len'] = 0
    max_dict['max_left_idx'] = 0
    max_dict['max_right_idx'] = 0
    for mid in range(len(string)):
        if mid+1<len(string) and string[mid] == string[mid+1]:
            run_checking(mid, mid+1, string, max_dict)
        if mid-1>=0 and mid+1<len(string) and string[mid-1]==string[mid+1]:
            run_checking(mid-1, mid+1, string, max_dict)


    return string[max_dict['max_left_idx']:max_dict['max_right_idx']+1]

def run_checking(left, right, string, max_dict):
    while left>=0 and right<len(string) and string[left]==string[right]:
        if max_dict['max_len'] < right-left+1:
            max_dict['max_len'] = right-left+1
            max_dict['max_left_idx'] = left
            max_dict['max_right_idx'] = right
        left -= 1
        right += 1

# case [string, expected]
cases = [
    ['abaxyzzyxf', 'xyzzyx'],
    ['a', 'a'],
    ["it's highnoon", 'noon'],
    ['noon high it is', 'noon'],
    ["abccbait's highnoon", 'abccba'],
    ['abcdefgfedcbazzzzzzzzzzzzzzzzzzzz', 'zzzzzzzzzzzzzzzzzzzz'],
    ['abcdefgfedcba', 'abcdefgfedcba'],
    ['abcdefghfedcbaa', 'aa'],
    ['abcdefggfedcba', 'abcdefggfedcba'],
    ['zzzzzzz2345abbbba5432zzbbababa', 'zz2345abbbba5432zz'],
    ['z234a5abbbba54a32z', '5abbbba5'],
    ['z234a5abbba54a32z', '5abbba5'],
    ['ab12365456321bb', 'b12365456321b'],
    ['aca', 'aca']
]

@pytest.mark.parametrize("string, expected", cases)
def test_longestPalindromicSubstring(string, expected):
    assert longestPalindromicSubstring(string)==expected
