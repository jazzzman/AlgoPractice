"""
  DESCRIPTION

  If you open the keypad of your mobile phone, it'll likely look like this:       
   ----- ----- -----
  |     |     |     |
  |  1  |  2  |  3  |
  |     | abc | def |
   ----- ----- -----
  |     |     |     |
  |  4  |  5  |  6  |
  | ghi | jkl | mno |
   ----- ----- -----
  |     |     |     |
  |  7  |  8  |  9  |
  | pqrs| tuv | wxyz|
   ----- ----- -----
        |     |
        |  0  |
        |     |
         -----

  Almost every digit is associated with some letters in the alphabet; this      
  allows certain phone numbers to spell out actual words. For example, the phone
  number 8464747328 can be written as timisgreat;
  similarly, the phone number 2686463 can be written as
  antoine or as ant6463.


  It's important to note that a phone number doesn't represent a single sequence
  of letters, but rather multiple combinations of letters. For instance, the    
  digit 2 can represent three different letters (a, b, and c).


  A mnemonic is defined as a pattern of letters, ideas, or associations that    
  assist in remembering something. Companies oftentimes use a mnemonic for their
  phone number to make it easier to remember.


  Given a stringified phone number of any non-zero length, write a function that
  returns all mnemonics for this phone number, in any order.


  For this problem, a valid mnemonic may only contain letters and the digits    
  0 and 1. In other words, if a digit is able to be
  represented by a letter, then it must be. Digits 0 and
  1 are the only two digits that don't have letter representations
  on the keypad.


  Note that you should rely on the keypad illustrated above for digit-letter    
  associations.


  Time complexity O(4^n*n)
  Space complexity O(4^n*n)
"""
import pytest
from icecream import ic


DIG_CHR = {str(k+2):[chr(ord('a')+3*k+j) for j in range(0,3)] for k in range(0,5) }
DIG_CHR['7'] = list('pqrs')
DIG_CHR['8'] = list('tuv')
DIG_CHR['9'] = list('wxyz')
DIG_CHR['0'] = ['0']
DIG_CHR['1'] = ['1']


def phoneNumberMnemonics(phoneNumber):
    if len(phoneNumber)==0:
        return []
    elif len(phoneNumber)==1:
        return DIG_CHR[phoneNumber[0]]

    result = []
    for ch in DIG_CHR[phoneNumber[0]]:
        sub = phoneNumberMnemonics(phoneNumber[1:])
        result += [ch+s for s in sub]

    return result



# case [phoneNumber, expected]
cases = [
    ['1905', ['1w0j', '1w0k', '1w0l', '1x0j', '1x0k', '1x0l', '1y0j', '1y0k', '1y0l', '1z0j', '1z0k', '1z0l']],
    ['1111', ['1111']],
    ['002', ['00a', '00b', '00c']],
    ['444', ['ggg', 'ggh', 'ggi', 'ghg', 'ghh', 'ghi', 'gig', 'gih', 'gii', 'hgg', 'hgh', 'hgi', 'hhg', 'hhh', 'hhi', 'hig', 'hih', 'hii', 'igg', 'igh', 'igi', 'ihg', 'ihh', 'ihi', 'iig', 'iih', 'iii']],
    ['1', ['1']],
    ['0', ['0']],
    ['23', ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']],
    ['1212', ['1a1a', '1a1b', '1a1c', '1b1a', '1b1b', '1b1c', '1c1a', '1c1b', '1c1c']],
    ['97', ['wp', 'wq', 'wr', 'ws', 'xp', 'xq', 'xr', 'xs', 'yp', 'yq', 'yr', 'ys', 'zp', 'zq', 'zr', 'zs']],
    ['980016', ['wt001m', 'wt001n', 'wt001o', 'wu001m', 'wu001n', 'wu001o', 'wv001m', 'wv001n', 'wv001o', 'xt001m', 'xt001n', 'xt001o', 'xu001m', 'xu001n', 'xu001o', 'xv001m', 'xv001n', 'xv001o', 'yt001m', 'yt001n', 'yt001o', 'yu001m', 'yu001n', 'yu001o', 'yv001m', 'yv001n', 'yv001o', 'zt001m', 'zt001n', 'zt001o', 'zu001m', 'zu001n', 'zu001o', 'zv001m', 'zv001n', 'zv001o']]
]

@pytest.mark.parametrize("phoneNumber, expected", cases)
def test_phoneNumberMnemonics(phoneNumber, expected):
    assert phoneNumberMnemonics(phoneNumber)==expected

