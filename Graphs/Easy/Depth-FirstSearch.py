r"""
  DESCRIPTION

  You're given a Node class that has a name and an
  array of optional children nodes. When put together, nodes form
  an acyclic tree-like structure.


  Implement the depthFirstSearch method on the
  Node class, which takes in an empty array, traverses the tree
  using the Depth-first Search approach (specifically navigating the tree from  
  left to right), stores all of the nodes' names in the input array, and returns
  it.


  If you're unfamiliar with Depth-first Search, we recommend watching the       
  Conceptual Overview section of this question's video explanation before       
  starting to code.
        A
     /  |  \
    B   C   D
   / \     / \
  E   F   G   H
     / \   \
    I   J   K
    ["A", "B", "E", "F", "I", "J", "C", "D", "G", "K", "H"]

  Time complexity O(V+E)
  Space complexity O(V)
"""
import pytest

from icecream import ic


class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, node):
        self.children.append(node)
        return self

    def depthFirstSearch(self, array):
        array.append(self.name)
        for node in self.children:
            node.depthFirstSearch(array)
        return array

    def __repr__(self):
        return (f'name: {self.name} '
                f'children: {[child.name for child in self.children]}')



# case [graph, expected]
cases = [
    [{'nodes': [{'children': ['B', 'C', 'D'], 'id': 'A', 'value': 'A'}, {'children': ['E', 'F'], 'id': 'B', 'value': 'B'}, {'children': [], 'id': 'C', 'value': 'C'}, {'children': ['G', 'H'], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': ['I', 'J'], 'id': 'F', 'value': 'F'}, {'children': ['K'], 'id': 'G', 'value': 'G'}, {'children': [], 'id': 'H', 'value': 'H'}, {'children': [], 'id': 'I', 'value': 'I'}, {'children': [], 'id': 'J', 'value': 'J'}, {'children': [], 'id': 'K', 'value': 'K'}], 'startNode': 'A'}, ['A', 'B', 'E', 'F', 'I', 'J', 'C', 'D', 'G', 'K', 'H']],
    [{'nodes': [{'children': ['B', 'C'], 'id': 'A', 'value': 'A'}, {'children': ['D'], 'id': 'B', 'value': 'B'}, {'children': [], 'id': 'C', 'value': 'C'}, {'children': [], 'id': 'D', 'value': 'D'}], 'startNode': 'A'}, ['A', 'B', 'D', 'C']],
    [{'nodes': [{'children': ['B', 'C', 'D', 'E'], 'id': 'A', 'value': 'A'}, {'children': [], 'id': 'B', 'value': 'B'}, {'children': ['F'], 'id': 'C', 'value': 'C'}, {'children': [], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': [], 'id': 'F', 'value': 'F'}], 'startNode': 'A'}, ['A', 'B', 'C', 'F', 'D', 'E']],
    [{'nodes': [{'children': ['B'], 'id': 'A', 'value': 'A'}, {'children': ['C'], 'id': 'B', 'value': 'B'}, {'children': ['D', 'E'], 'id': 'C', 'value': 'C'}, {'children': ['F'], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': [], 'id': 'F', 'value': 'F'}], 'startNode': 'A'}, ['A', 'B', 'C', 'D', 'F', 'E']],
    [{'nodes': [{'children': ['B', 'C', 'D', 'E', 'F'], 'id': 'A', 'value': 'A'}, {'children': ['G', 'H', 'I'], 'id': 'B', 'value': 'B'}, {'children': ['J'], 'id': 'C', 'value': 'C'}, {'children': ['K', 'L'], 'id': 'D', 'value': 'D'}, {'children': [], 'id': 'E', 'value': 'E'}, {'children': ['M', 'N'], 'id': 'F', 'value': 'F'}, {'children': [], 'id': 'G', 'value': 'G'}, {'children': ['O', 'P', 'Q', 'R'], 'id': 'H', 'value': 'H'}, {'children': [], 'id': 'I', 'value': 'I'}, {'children': [], 'id': 'J', 'value': 'J'}, {'children': ['S'], 'id': 'K', 'value': 'K'}, {'children': [], 'id': 'L', 'value': 'L'}, {'children': [], 'id': 'M', 'value': 'M'}, {'children': [], 'id': 'N', 'value': 'N'}, {'children': [], 'id': 'O', 'value': 'O'}, {'children': ['T', 'U'], 'id': 'P', 'value': 'P'}, {'children': [], 'id': 'Q', 'value': 'Q'}, {'children': ['V'], 'id': 'R', 'value': 'R'}, {'children': [], 'id': 'S', 'value': 'S'}, {'children': [], 'id': 'T', 'value': 'T'}, {'children': [], 'id': 'U', 'value': 'U'}, {'children': ['W', 'X', 'Y'], 'id': 'V', 'value': 'V'}, {'children': [], 'id': 'W', 'value': 'W'}, {'children': ['Z'], 'id': 'X', 'value': 'X'}, {'children': [], 'id': 'Y', 'value': 'Y'}, {'children': [], 'id': 'Z', 'value': 'Z'}], 'startNode': 'A'}, ['A', 'B', 'G', 'H', 'O', 'P', 'T', 'U', 'Q', 'R', 'V', 'W', 'X', 'Z', 'Y', 'I', 'C', 'J', 'D', 'K', 'S', 'L', 'E', 'F', 'M', 'N']]
]

@pytest.mark.parametrize("graph, expected", cases)
def test_depthFirstSearch(graph, expected):
    nodes = {node['value']:Node(node['value']) for node in graph['nodes']}
    for node in graph['nodes']:
        for child in node['children']:
            nodes[node['value']].addChild(nodes[child])
            
    ic(nodes)
    assert nodes[graph['startNode']].depthFirstSearch([])==expected
