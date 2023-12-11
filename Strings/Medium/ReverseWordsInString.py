"""
  DESCRIPTION

  Write a function that takes in a string of words separated by one or more     
  whitespaces and returns a string that has these words in reverse order. For   
  example, given the string "tim is great", your function should
  return "great is tim".


  For this problem, a word can contain special characters, punctuation, and     
  numbers. The words in the string will be separated by one or more whitespaces,
  and the reversed string must contain the same whitespaces as the original     
  string. For example, given the string
  "whitespaces    4" you would be expected to return
  "4    whitespaces".


  Note that you're not allowed to to use any built-in
  split or reverse methods/functions. However, you
  are allowed to use a built-in join method/function.

Also note that the input string isn't guaranteed to always contain words.       


  Time complexity O(n) n - string length
  Space complexity O(n)
"""
import pytest


def reverseWordsInString(string):
    words = []
    start, end = 0, 0
    word_ends = string[0] == ' '
    while end < len(string):
        if string[end] == ' ' and not word_ends:
            words.insert(0,string[start: end])
            word_ends = True
            start = end
        if string[end] != ' ' and word_ends:
            words.insert(0,string[start: end])
            start = end
            word_ends = False
        end += 1

    words.insert(0,string[start: end])

    return ''.join(words)


# case [string, expected]
cases = [
    ['AlgoExpert is the best!', 'best! the is AlgoExpert'],
    ['Reverse These Words', 'Words These Reverse'],
    ['..H,, hello 678', '678 hello ..H,,'],
    ['this this words this this this words this', 'this words this this this words this this'],
    ['1 12 23 34 56', '56 34 23 12 1'],
    ['APPLE PEAR PLUM ORANGE', 'ORANGE PLUM PEAR APPLE'],
    ['this-is-one-word', 'this-is-one-word'],
    ['a', 'a'],
    ['ab', 'ab'],
    ['algoexpert is the best platform to use to prepare for coding interviews!', 'interviews! coding for prepare to use to platform best the is algoexpert'],
    ['words, separated, by, commas', 'commas by, separated, words,'],
    ['this      string     has a     lot of   whitespace', 'whitespace   of lot     a has     string      this'],
    ['a ab a', 'a ab a'],
    ['test        ', '        test'],
    [' ', ' ']
]

@pytest.mark.parametrize("string, expected", cases)
def test_reverseWordsInString(string, expected):
    assert reverseWordsInString(string)==expected
