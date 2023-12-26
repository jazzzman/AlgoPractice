r"""
  DESCRIPTION

  You're given three inputs, all of which are instances of an
  AncestralTree class that have an ancestor property
  pointing to their youngest ancestor. The first input is the top ancestor in an
  ancestral tree (i.e., the only instance that has no ancestor--its
  ancestor property points to None /
  null), and the other two inputs are descendants in the ancestral
  tree.


  Write a function that returns the youngest common ancestor to the two
  descendants.


  Note that a descendant is considered its own ancestor. So in the simple
  ancestral tree below, the youngest common ancestor to nodes A and B is node A.

    topAncestor = node A
    descendantOne = node E
    descendantTwo = node I
              A
           /     \
          B       C
        /   \   /   \
       D     E F     G
     /   \
    H     I
    
    Sample Output
    node B


  Time complexity O(V) - count of vertex of deepest descendant
  Space complexity O(V)
"""
import pytest

from icecream import ic


class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

    def __repr__(self):
        return f'name: {self.name} children: {self.ancestor.name if self.ancestor else None}'


def getYoungetsCommonAncestor(nodes, descendantOne, descendantTwo, topAncestor):
    pathOne = set()
    
    while descendantOne and descendantOne != topAncestor:
        pathOne.add(descendantOne)
        descendantOne = descendantOne.ancestor

    while descendantTwo and descendantTwo != topAncestor:
        if descendantTwo in pathOne:
            return descendantTwo
        descendantTwo = descendantTwo.ancestor

    return topAncestor


# case [nodes, descendantOne, descendantTwo, topAncestor, expected]
cases = [
    [{'nodes': [
        {'ancestor': None, 'id': 'A', 'name': 'A'},
        {'ancestor': 'A', 'id': 'B', 'name': 'B'},
        {'ancestor': 'A', 'id': 'C', 'name': 'C'},
        {'ancestor': 'B', 'id': 'D', 'name': 'D'},
        {'ancestor': 'B', 'id': 'E', 'name': 'E'},
        {'ancestor': 'C', 'id': 'F', 'name': 'F'},
        {'ancestor': 'C', 'id': 'G', 'name': 'G'},
        {'ancestor': 'D', 'id': 'H', 'name': 'H'},
        {'ancestor': 'D', 'id': 'I', 'name': 'I'}]
      },
     'E', 'I', 'A', 
     {'nodeId': 'B'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'A', 'B', 'A', {'nodeId': 'A'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'B', 'F', 'A', {'nodeId': 'A'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'G', 'M', 'A', {'nodeId': 'A'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'U', 'S', 'A', {'nodeId': 'A'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'Z', 'M', 'A', {'nodeId': 'A'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'O', 'I', 'A', {'nodeId': 'B'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'T', 'Z', 'A', {'nodeId': 'H'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'T', 'V', 'A', {'nodeId': 'H'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'T', 'H', 'A', {'nodeId': 'H'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'W', 'V', 'A', {'nodeId': 'V'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'Z', 'B', 'A', {'nodeId': 'B'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'Q', 'W', 'A', {'nodeId': 'H'}],
    [{'nodes': [{'ancestor': None, 'id': 'A', 'name': 'A'}, {'ancestor': 'A', 'id': 'B', 'name': 'B'}, {'ancestor': 'A', 'id': 'C', 'name': 'C'}, {'ancestor': 'A', 'id': 'D', 'name': 'D'}, {'ancestor': 'A', 'id': 'E', 'name': 'E'}, {'ancestor': 'A', 'id': 'F', 'name': 'F'}, {'ancestor': 'B', 'id': 'G', 'name': 'G'}, {'ancestor': 'B', 'id': 'H', 'name': 'H'}, {'ancestor': 'B', 'id': 'I', 'name': 'I'}, {'ancestor': 'C', 'id': 'J', 'name': 'J'}, {'ancestor': 'D', 'id': 'K', 'name': 'K'}, {'ancestor': 'D', 'id': 'L', 'name': 'L'}, {'ancestor': 'F', 'id': 'M', 'name': 'M'}, {'ancestor': 'F', 'id': 'N', 'name': 'N'}, {'ancestor': 'H', 'id': 'O', 'name': 'O'}, {'ancestor': 'H', 'id': 'P', 'name': 'P'}, {'ancestor': 'H', 'id': 'Q', 'name': 'Q'}, {'ancestor': 'H', 'id': 'R', 'name': 'R'}, {'ancestor': 'K', 'id': 'S', 'name': 'S'}, {'ancestor': 'P', 'id': 'T', 'name': 'T'}, {'ancestor': 'P', 'id': 'U', 'name': 'U'}, {'ancestor': 'R', 'id': 'V', 'name': 'V'}, {'ancestor': 'V', 'id': 'W', 'name': 'W'}, {'ancestor': 'V', 'id': 'X', 'name': 'X'}, {'ancestor': 'V', 'id': 'Y', 'name': 'Y'}, {'ancestor': 'X', 'id': 'Z', 'name': 'Z'}]}, 'A', 'Z', 'A', {'nodeId': 'A'}]
]

@pytest.mark.parametrize("nodes, descendantOne, descendantTwo, topAncestor, expected", cases)
def test_getYoungetsCommonAncestor(nodes, descendantOne, descendantTwo, topAncestor, expected):
    nodes_dict = {node['id']:AncestralTree(node['id']) for node in nodes['nodes']}
    for node in nodes['nodes']:
        nodes_dict[node['id']].ancestor = nodes_dict.get(node['ancestor'], None)

    assert getYoungetsCommonAncestor(nodes_dict, nodes_dict[descendantOne], nodes_dict[descendantTwo], nodes_dict[topAncestor]).name ==expected['nodeId']
