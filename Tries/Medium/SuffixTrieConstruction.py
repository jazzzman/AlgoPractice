"""
  DESCRIPTION

  Write a SuffixTrie class for a Suffix-Trie-like data structure.        
  The class should have a root property set to be the root node of       
  the trie and should support:


  Note that every string added to the trie should end with the special   
  endSymbol character: "*".


  If you're unfamiliar with Suffix Tries, we recommend watching the      
  Conceptual Overview section of this question's video explanation before
  starting to code.

  Time and Space complexity are different for methods. Look at each method.
"""
import pytest

from icecream import ic


class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    # Time complexity O(n^2) n - length of string
    # Space complexity O(n^2)
    def populateSuffixTrieFrom(self, string):
        for suffix_start in range(len(string)):
            sub_dict = self.root
            current_idx = suffix_start
            while current_idx<len(string):
                if string[current_idx] not in sub_dict:
                    sub_dict[string[current_idx]] = {}

                sub_dict = sub_dict[string[current_idx]]
                current_idx += 1
            sub_dict[self.endSymbol] = True


    # Time complexity O(m)  m - length of searching string
    # Space complexity O(1)
    def contains(self, string):
        sub_dict = self.root
        for ch in string:
            if ch not in sub_dict:
                return False
            sub_dict = sub_dict[ch]
        return self.endSymbol in sub_dict


def suffixTrieConstruction(string, query):
    suffixTrie = SuffixTrie(string)
    return [suffixTrie.contains(q) for q in query], suffixTrie


# case [string, query, expected]
cases = [
    ['babc', ['abc'], {'output': [True], 'trie': {'a': {'b': {'c': {'*': True}}}, 'b': {'a': {'b': {'c': {'*': True}}}, 'c': {'*': True}}, 'c': {'*': True}}}],
    ['test', ['t', 'st', 'est', 'test', 'tes'],  {'output': [True, True, True, True, False], 'trie': {'e': {'s': {'t': {'*': True}}}, 's': {'t': {'*': True}}, 't': {'*': True, 'e': {'s': {'t': {'*': True}}}}}}]
]

@pytest.mark.parametrize("string, query, expected", cases)
def test_suffixTrieConstruction(string, query, expected):
    output, trie = suffixTrieConstruction(string, query)
    assert trie.root == expected['trie']
    assert output == expected['output']
