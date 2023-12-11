"""
  DESCRIPTION

    You're given two strings stringOne and stringTwo.
    Write a function that determines if these two strings can be made equal   
    using only one edit.


    There are 3 possible edits:

        Replace: One character in one string is swapped for a different
        character.
      
      
        Add: One character is added at any index in one string.
      
      
        Remove: One character is removed at any index in one string.


    Note that both strings will contain at least one character. If the strings
    are the same, your function should return true.



  Time complexity O(s) s - length of short word
  Space complexity O(1)
"""
import pytest


def oneEdit(stringOne, stringTwo):
    editions = 0
    shortWord = stringOne if len(stringOne) < len(stringTwo) else stringTwo
    longWord = stringOne if len(stringOne) >= len(stringTwo) else stringTwo
    ptShort, ptLong = 0, 0

    while ptShort<len(shortWord):
        if shortWord[ptShort] == longWord[ptLong]:
            ptLong += 1
            ptShort += 1
            continue

        editions += 1
        ptLong += 1

        if len(shortWord) == len(longWord):
            ptShort += 1

        if editions>1:
            return False



    return len(longWord)-ptLong<=1-editions


# case [stringOne, stringTwo, expected]
cases = [
    ['a', 'a', True],
    ['aaa', 'aaa', True],
    ['a', 'b', True],
    ['ab', 'b', True],
    ['abc', 'b', False],
    ['ab', 'a', True],
    ['b', 'ab', True],
    ['bb', 'a', False],
    ['a', 'ab', True],
    ['bb', 'ab', True],
    ['ab', 'bb', True],
    ['hello', 'helo', True],
    ['hello', 'heo', False],
    ['hello', 'heloo', True],
    ['hello', 'heloos', False],
    ['hello', 'heloos', False],
    ['hello', 'helllo', True],
    ['hello', 'helllos', False],
    ['hello', 'ello', True],
    ['hello', 'llo', False],
    ['hello', 'ellos', False],
    ['hello', 'elllos', False],
    ['helo', 'helle', False],
    ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', True],
    ['bcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', True],
    ['bcdefgijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyz', False],
    ['bcdefghijklmnopqrstuvwxyz', 'acdefghijklmnopqrstuvwxyz', True],
    ['bcdefghijklmnopqrstuvwxyz', 'abdefghijklmnopqrstuvwxyz', False],
    ['bcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxy', False],
    ['bcdefghijklmnopqrstuvwxyz', 'abcdefghijklmnopqrstuvwxyza', False],
    ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklnopqrstuvwxyz', True],
    ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklmmnopqrstuvwxyz', True],
    ['abcdefghijklmnopqrstuvwxyz', 'abcdefghijklnnopqrstuvwxyz', True]
]

@pytest.mark.parametrize("stringOne, stringTwo, expected", cases)
def test_oneEdit(stringOne, stringTwo, expected):
    assert oneEdit(stringOne, stringTwo)==expected
