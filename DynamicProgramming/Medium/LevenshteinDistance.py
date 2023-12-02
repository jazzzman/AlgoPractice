"""
  DESCRIPTION


  Write a function that takes in two strings and returns the minimum number of
  edit operations that need to be performed on the first string to obtain the
  second string.

  There are three edit operations: insertion of a character, deletion of a
  character, and substitution of a character for another.

  Time complexity O(n*m)
  Space complexity O(n*m) could be reduce to min(n,m)

  idea is to create table with substrings starting with 0 to i.
  header is substrings of str2 and index column is substrings of str1
  to each str1 and str2 add space character. Cell shows how many editions
  needs to turn substring of str1 to substring to str2. 
  table fills according to rule:
  if str1[r-1]==str2[c-1]: E[r][c] = E[r-1][c-1]
  else: E[r][c] = 1 + min([E[r-1][c],E[r][c-1],E[r-1][c-1]])
  Bottom right cell is an answer
"""
import pytest


def levenshteinDistance(str1, str2):
    E = [[float('inf')]*(len(str2)+1) for _ in range(len(str1)+1)]
    E[0] = list(range(len(str2)+1))
    for idx in range(len(E)):
        E[idx][0] = idx

    for row in range(1,len(E)):
        for column in range(1,len(E[0])):
            if str1[row-1]==str2[column-1]:
                E[row][column] = E[row-1][column-1]
            else:
                E[row][column] = 1 + min(E[row-1][column],E[row-1][column-1],E[row][column-1])
    return E[-1][-1]


# case [str1, str2, expected]
cases = [
    ['abc', 'yabd', 2],
    ['', '', 0],
    ['', 'abc', 3],
    ['abc', 'abc', 0],
    ['abc', 'abx', 1],
    ['abc', 'abcx', 1],
    ['abc', 'yabcx', 2],
    ['algoexpert', 'algozexpert', 1],
    ['abcdefghij', '1234567890', 10],
    ['abcdefghij', 'a234567890', 9],
    ['biting', 'mitten', 4],
    ['cereal', 'saturday', 6],
    ['cereal', 'saturdzz', 7],
    ['abbbbbbbbb', 'bbbbbbbbba', 2],
    ['xabc', 'abcx', 2],
    ['table', 'bal', 3],
    ['gumbo', 'gambol', 2]
]

@pytest.mark.parametrize("str1, str2, expected", cases)
def test_levenshteinDistance(str1, str2, expected):
    assert levenshteinDistance(str1, str2)==expected

