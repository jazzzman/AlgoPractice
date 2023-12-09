"""
  DESCRIPTION

  You're given a string of available characters and a string representing a    
  document that you need to generate. Write a function that determines if you  
  can generate the document using the available characters. If you can generate
  the document, your function should return true; otherwise, it
  should return false.


  You're only able to generate the document if the frequency of unique
  characters in the characters string is greater than or equal to the frequency
  of unique characters in the document string. For example, if you're given    
  characters = "abcabc" and document = "aabbccc" you
  cannot generate the document because you're missing one c.


  The document that you need to create may contain any characters, including   
  special characters, capital letters, numbers, and spaces.

Note: you can always generate the empty string ("").


  Time complexity O(n)
  Space complexity O(n)
"""
import pytest


def generateDocument(characters, document):
    ch_hist = histogram(characters)
    for ch in document:
        if ch in ch_hist and ch_hist[ch]>0:
            ch_hist[ch] -= 1
        else:
            return False
    return True

def histogram(characters):
    hist = {}
    for ch in characters:
        if ch in hist:
            hist[ch] += 1
        else:
            hist[ch] = 1
    return hist


# case [characters, document, expected]
cases = [
    ['Bste!hetsi ogEAxpelrt x ', 'AlgoExpert is the Best!', True],
    ['A', 'a', False],
    ['a', 'a', True],
    ['a hsgalhsa sanbjksbdkjba kjx', '', True],
    [' ', 'hello', False],
    ['     ', '     ', True],
    ['aheaollabbhb', 'hello', True],
    ['aheaolabbhb', 'hello', False],
    ['estssa', 'testing', False],
    ['Bste!hetsi ogEAxpert', 'AlgoExpert is the Best!', False],
    ['helloworld ', 'hello wOrld', False],
    ['helloworldO', 'hello wOrld', False],
    ['helloworldO ', 'hello wOrld', True],
    ['&*&you^a%^&8766 _=-09     docanCMakemthisdocument', 'Can you make this document &', True],
    ['abcabcabcacbcdaabc', 'bacaccadac', True]
]

@pytest.mark.parametrize("characters, document, expected", cases)
def test_generateDocument(characters, document, expected):
    assert generateDocument(characters, document)==expected
