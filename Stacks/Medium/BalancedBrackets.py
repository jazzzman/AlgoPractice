"""
  DESCRIPTION

  Write a function that takes in a string made up of brackets ((,
  [, {, ), ], and
  }) and other optional characters. The function should return a
  boolean representing whether the string is balanced with regards to brackets.


  A string is said to be balanced if it has as many opening brackets of a      
  certain type as it has closing brackets of that type and if no bracket is    
  unmatched. Note that an opening bracket can't match a corresponding closing  
  bracket that comes before it, and similarly, a closing bracket can't match a 
  corresponding opening bracket that comes after it. Also, brackets can't      
  overlap each other as in
  [(]).

  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


def balancedBrackets(string):
    bracket_stack = []
    brackets = {
        '}': '{',
        ']': '[',
        ')': '('
    }
    for ch in string:
        if ch in '([{':
            bracket_stack.append(ch)
        
        if ch in '}])':
            if len(bracket_stack)==0 or brackets[ch] != bracket_stack.pop():
                return False

    return len(bracket_stack) == 0


# case [string, expected]
cases = [
    ['([])(){}(())()()', True],
    ['()[]{}{', False],
    ['(((((({{{{{[[[[[([)])]]]]]}}}}}))))))', False],
    ['()()[{()})]', False],
    ['(()())((()()()))', True],
    ['{}()', True],
    ['()([])', True],
    ['((){{{{[]}}}})', True],
    ['((({})()))', True],
    ['(([]()()){})', True],
    ['(((((([[[[[[{{{{{{{{{{{{()}}}}}}}}}}}}]]]]]]))))))((([])({})[])[])[]([]){}(())', True],
    ['{[[[[({(}))]]]]}', False],
    ['[((([])([]){}){}){}([])[]((())', False],
    [')[]}', False],
    ['(a)', True],
    ['(a(', False],
    ['(141[])(){waga}((51afaw))()hh()', True],
    ['aafwgaga()[]a{}{gggg', False],
    ['(((((({{{{{safaf[[[[[([)]safsafsa)]]]]]}}}gawga}}))))))', False],
    ['()(agawg)[{()gawggaw})]', False],
    ['(()agwg())((()agwga()())gawgwgag)', True],
    ['{}gawgw()', True],
    ['(agwgg)([ghhheah%&@Q])', True]
]

@pytest.mark.parametrize("string, expected", cases)
def test_balancedBrackets(string, expected):
    assert balancedBrackets(string)==expected

