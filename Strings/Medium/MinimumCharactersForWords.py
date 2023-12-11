"""
  DESCRIPTION

  Write a function that takes in an array of words and returns the smallest     
  array of characters needed to form all of the words. The characters don't need
  to be in any particular order.


  For example, the characters ["y", "r", "o", "u"] are needed to
  form the words ["your", "you", "or", "yo"].


  Note: the input words won't contain any spaces; however, they might contain   
  punctuation and/or special characters.


  Time complexity O(n*m) n - count of words, m - count chars in the longest word
  Space complexity O(c) c - count of unique characters
"""
import pytest


def minimumCharactersForWords(words):
    output_dict = {}
    for word in words:
        hist = histogram(word)
        for ch, value in hist.items():
            output_dict[ch] = max(output_dict.get(ch,0),value)
    return [ch for ch, value in output_dict.items() for _ in range(value)]

def histogram(word):
    hist = {}
    for ch in word:
        hist[ch] = hist.get(ch,0)+1
    return hist


# case [words, expected]
cases = [
    [['this', 'that', 'did', 'deed', 'them!', 'a'], ['!', 'a', 'd', 'd', 'e', 'e', 'h', 'i', 'm', 's', 't', 't']],
    [['a', 'abc', 'ab', 'boo'], ['a', 'b', 'c', 'o', 'o']],
    [['a'], ['a']],
    [['abc', 'ab', 'b', 'bac', 'c'], ['a', 'b', 'c']],
    [['!!!2', '234', '222', '432'], ['!', '!', '!', '2', '2', '2', '3', '4']],
    [['this', 'that', 'they', 'them', 'their', 'there', 'time', 'is'], ['a', 'e', 'e', 'h', 'i', 'm', 'r', 's', 't', 't', 'y']],
    [['tim', 'is', 'great'], ['a', 'e', 'g', 'i', 'm', 'r', 's', 't']],
    [['abc', 'bavcc', 'aaaa', 'cde', 'efg', 'gead'], ['a', 'a', 'a', 'a', 'b', 'c', 'c', 'd', 'e', 'f', 'g', 'v']],
    [['a', 'a', 'a'], ['a']],
    [['them', 'they', 'that', 'that', 'yes', 'yo', 'no', 'boo', 'you', 'okay', 'too'], ['a', 'b', 'e', 'h', 'k', 'm', 'n', 'o', 'o', 's', 't', 't', 'u', 'y']],
    [['cta', 'cat', 'tca', 'tac', 'a', 'c', 't'], ['a', 'c', 't']],
    [['my', 'coding', 'skills', 'are', 'great'], ['a', 'c', 'd', 'e', 'g', 'i', 'k', 'l', 'l', 'm', 'n', 'o', 'r', 's', 's', 't', 'y']],
    [[], []],
    [['168712hn3;nlsdjhahjdksaxa097918@#$RT%T^&*()_'], ['#', '$', '%', '&', '(', ')', '*', '0', '1', '1', '1', '2', '3', '6', '7', '7', '8', '8', '9', '9', ';', '@', 'R', 'T', 'T', '^', '_', 'a', 'a', 'a', 'd', 'd', 'h', 'h', 'h', 'j', 'j', 'k', 'l', 'n', 'n', 's', 's', 'x']],
    [['cat', 'cAt', 'tAc', 'Act', 'Cat'], ['A', 'C', 'a', 'c', 't']],
    [['Abc', 'baVcc', 'aaaa', 'cdeE', 'efg', 'gead'], ['A', 'E', 'V', 'a', 'a', 'a', 'a', 'b', 'c', 'c', 'd', 'e', 'f', 'g']],
    [['mississippi', 'piper', 'icing', 'ice', 'pickle', 'piping', 'pie', 'pi', 'sassy', 'serpent', 'python', 'ascii', 'sister', 'mister'], ['a', 'c', 'e', 'e', 'g', 'h', 'i', 'i', 'i', 'i', 'k', 'l', 'm', 'n', 'o', 'p', 'p', 'r', 's', 's', 's', 's', 't', 'y']]
]

@pytest.mark.parametrize("words, expected", cases)
def test_minimumCharactersForWords(words, expected):
    assert sorted(minimumCharactersForWords(words))==sorted(expected)
