"""
  DESCRIPTION

  Write a function that takes in an array of strings and groups anagrams together.


  Anagrams are strings made up of exactly the same letters, where order doesn't   
  matter. For example, "cinema" and "iceman" are
  anagrams; similarly, "foo" and "ofo" are anagrams.


  Your function should return a list of anagram groups in no particular order.    


  Time complexity O(n*m*log(n)) n - word count, m - length of the maximum word
  Space complexity O(n*m)
"""
import pytest


def groupAnagrams(words):
    sets = {}
    output = []
    for word in words:
        hist = histogram(word)
        sorted_word = ''.join(sorted(word))
        if sorted_word in sets:
            output[sets[sorted_word]].append(word)
        else:
            output.append([word])
            sets[sorted_word] = len(output)-1

    return output

def histogram(word):
    hist = {}
    for ch in word:
        hist[ch] = hist.get(ch, 0) + 1 
    return hist

# case [words, expected]
cases = [
    [['yo', 'act', 'flop', 'tac', 'foo', 'cat', 'oy', 'olfp'], [['foo'], ['flop', 'olfp'], ['oy', 'yo'], ['act', 'cat', 'tac']]],
    [[], []],
    [['test'], [['test']]],
    [['abc', 'dabd', 'bca', 'cab', 'ddba'], [['dabd', 'ddba'], ['abc', 'bca', 'cab']]],
    [['abc', 'cba', 'bca'], [['abc', 'bca', 'cba']]],
    [['zxc', 'asd', 'weq', 'sda', 'qwe', 'xcz'], [['asd', 'sda'], ['qwe', 'weq'], ['xcz', 'zxc']]],
    [['cinema', 'a', 'flop', 'iceman', 'meacyne', 'lofp', 'olfp'], [['a'], ['meacyne'], ['cinema', 'iceman'], ['flop', 'lofp', 'olfp']]],
    [['abc', 'abe', 'abf', 'abg'], [['abc'], ['abe'], ['abf'], ['abg']]],
    [['aaa', 'a'], [['a'], ['aaa']]],
    [['bob', 'boo'], [['bob'], ['boo']]],
    [['ill', 'duh'], [['duh'], ['ill']]],
    [['yo', 'oy', 'zn'], [['zn'], ['oy', 'yo']]],
    [['yyo', 'yo'], [['yo'], ['yyo']]],
    [['aca', 'bba'], [['aca'], ['bba']]]
]

@pytest.mark.parametrize("words, expected", cases)
def test_groupAnagrams(words, expected):
    candidat = groupAnagrams(words)
    for idx in range(len(candidat)):
        candidat[idx] = sorted(candidat[idx])
    for idx in range(len(expected)):
        expected[idx] = sorted(expected[idx])
    assert sorted(candidat)==sorted(expected)
