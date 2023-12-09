"""
  DESCRIPTION

    Write a function that takes in a non-empty list of non-empty strings and
    returns a list of characters that are common to all strings in the list,
    ignoring multiplicity.


    Note that the strings are not guaranteed to only contain alphanumeric characters. The list
    you return can be in any order.



  Time complexity O(n*m) n - count of strings, m - length of the longest string
  Space complexity O(m)
"""
import pytest


def commonCharacters(strings):
    commons = None
    for string in strings:
        if commons is None:
            commons = set(string)
        else:
            commons &= set(string)

    return list(commons)


# case [strings, expected]
cases = [
    [['abc', 'bcd', 'cbad'], ['b', 'c']],
    [['a'], ['a']],
    [['a', 'b', 'c'], []],
    [['aa', 'aa'], ['a']],
    [['aaaa', 'a'], ['a']],
    [['abcde', 'aa', 'foobar', 'foobaz', 'and this is a string', 'aaaaaaaa', 'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeea'], ['a']],
    [['abcdef', 'fedcba', 'abcefd', 'aefbcd', 'efadbc', 'effffffffffffbcda', 'eeeeeffffffbbbbbaaaaaccccdddd', '**************abdcef************'], ['a', 'b', 'c', 'd', 'e', 'f']],
    [['ab&cdef!', 'f!ed&cba', 'a&bce!d', 'ae&fb!cd', 'efa&!dbc', 'eff!&fff&fffffffbcda', 'eeee!efff&fffbbbbbaaaaaccccdddd', '*******!***&****abdcef************', '*******!***&****a***********f*', '*******!***&****b***********c*'], ['!', '&']],
    [['*abcd', 'def*', '******d*****'], ['*', 'd']],
    [['*abc!d', 'de!f*', '**!!!****d*****'], ['!', '*', 'd']]
]

@pytest.mark.parametrize("strings, expected", cases)
def test_commonCharacters(strings, expected):
    assert sorted(commonCharacters(strings))==sorted(expected)
