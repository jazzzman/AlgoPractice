"""
  DESCRIPTION

  Write a function that takes in a list of unique strings and returns a list of
  semordnilap pairs.


  A semordnilap pair is defined as a set of different strings where the reverse
  of one word is the same as the forward version of the other. For example the 
  words "diaper" and "repaid" are a semordnilap pair, as are the words
  "palindromes" and "semordnilap".


  The order of the returned pairs and the order of the strings within each pair
  does not matter.



  Time complexity O(n) n - count of words, m - length of the longest word
  Space complexity O(n*m)
"""
import pytest


def semordnilap(words):
    hist = {}
    for word in words:
        if word[::-1] in hist:
            hist[word[::-1]] = word
        else:
            hist[word] = None
    return [[key, value] for key,value in hist.items() if value is not None]


# case [words, expected]
cases = [
    [[], []],
    [['aaa', 'bbbb'], []],
    [['dog', 'god'], [['dog', 'god']]],
    [['dog', 'hello', 'god'], [['dog', 'god']]],
    [['dog', 'desserts', 'god', 'stressed'], [['dog', 'god'], ['desserts', 'stressed']]],
    [['dog', 'hello', 'desserts', 'test', 'god', 'stressed'], [['dog', 'god'], ['desserts', 'stressed']]],
    [['abcde', 'edcba', 'edbc', 'edb', 'cbde', 'abc'], [['abcde', 'edcba'], ['edbc', 'cbde']]],
    [['abcde', 'bcd', 'dcb', 'edcba', 'aaa'], [['abcde', 'edcba'], ['bcd', 'dcb']]],
    [['abcdefghijk', 'aaa', 'hello', 'racecar', 'kjihgfedcba'], [['abcdefghijk', 'kjihgfedcba']]],
    [['liver', 'dog', 'hello', 'desserts', 'evil', 'test', 'god', 'stressed', 'racecar', 'palindromes', 'semordnilap', 'abcd', 'live'], [['dog', 'god'], ['desserts', 'stressed'], ['evil', 'live'], ['palindromes', 'semordnilap']]]
]

@pytest.mark.parametrize("words, expected", cases)
def test_semordnilap(words, expected):
    assert semordnilap(words)==expected
