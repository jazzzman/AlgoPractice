"""
  DESCRIPTION

  The distance between a node in a Binary Tree and the tree's root is called the
  node's depth.

  Write a function that takes in a Binary Tree and returns the sum of its nodes'
  depths.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.


  Time complexity O(n) - count of nodes
  Space complexity O(h) - height of tree
"""
import pytest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root,depth=0):
    if root is None:
        return 0
    return depth+ nodeDepths(root.left,depth+1)+nodeDepths(root.right,depth+1)


# case [root, expected]
cases = [
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}], 'root': '1'}, 16],
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, 1],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 2],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, 4],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}, 21],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '8', 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': '9', 'value': 8}, {'id': '9', 'left': None, 'right': '10', 'value': 9}, {'id': '10', 'left': None, 'right': '11', 'value': 10}, {'id': '11', 'left': None, 'right': '12', 'value': 11}, {'id': '12', 'left': '13', 'right': None, 'value': 12}, {'id': '13', 'left': None, 'right': None, 'value': 13}], 'root': '1'}, 42],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': '10', 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': '11', 'value': 10}, {'id': '11', 'left': '12', 'right': '13', 'value': 11}, {'id': '12', 'left': '14', 'right': None, 'value': 12}, {'id': '13', 'left': '15', 'right': '16', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '16', 'left': None, 'right': None, 'value': 16}], 'root': '1'}, 51],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'right': None, 'value': 5}, {'id': '6', 'left': '7', 'right': None, 'value': 6}, {'id': '7', 'left': '8', 'right': None, 'value': 7}, {'id': '8', 'left': '9', 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}], 'root': '1'}, 36]
]

@pytest.mark.parametrize("root, expected", cases)
def test_nodeDepths(root, expected):
    nodes = {}
    for node_json in root['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in root['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None

    assert nodeDepths(nodes[root['root']])==expected

