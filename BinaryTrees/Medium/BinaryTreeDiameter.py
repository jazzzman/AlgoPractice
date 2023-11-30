"""
  DESCRIPTION

  Write a function that takes in a Binary Tree and returns its diameter. The
  diameter of a binary tree is defined as the length of its longest path, even
  if that path doesn't pass through the root of the tree.

  A path is a collection of connected nodes in a tree, where no node is
  connected to more than two other nodes. The length of a path is the number of
  edges between the path's first node and its last node.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.

  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


MAX_DIAMETER = 0

def binaryTreeDiameter(root):
    global MAX_DIAMETER
    MAX_DIAMETER=0
    dfs(root)
    return MAX_DIAMETER

def dfs(node):
    global MAX_DIAMETER
    if node is None:
        return 0
    
    left_part = dfs(node.left)
    right_part = dfs(node.right)

    MAX_DIAMETER = max(MAX_DIAMETER,left_part+right_part)
    
    return max(right_part,left_part)+1


# case [root, expected]
cases = [
    [{'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '3', 'left': '7', 'right': '4', 'value': 3}, {'id': '7', 'left': '8', 'right': None, 'value': 7}, {'id': '8', 'left': '9', 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '4', 'left': None, 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, 6],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, 4],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, 2],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '-1', 'value': 1}, {'id': '-1', 'left': None, 'right': None, 'value': -1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, 2],
    [{'nodes': [{'id': '1', 'left': '-5', 'right': '3', 'value': 1}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '-5', 'left': '6', 'right': None, 'value': -5}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, 3],
    [{'nodes': [{'id': '1', 'left': '3', 'right': '9', 'value': 1}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '9', 'left': '14', 'right': '10', 'value': 9}, {'id': '10', 'left': None, 'right': '11', 'value': 10}, {'id': '11', 'left': None, 'right': '12', 'value': 11}, {'id': '12', 'left': None, 'right': '17', 'value': 12}, {'id': '17', 'left': None, 'right': None, 'value': 17}, {'id': '14', 'left': None, 'right': '19', 'value': 14}, {'id': '19', 'left': '25', 'right': None, 'value': 19}, {'id': '25', 'left': None, 'right': None, 'value': 25}], 'root': '1'}, 7],
    [{'nodes': [{'id': '1', 'left': '3', 'right': '5', 'value': 1}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '1'}, 2],
    [{'nodes': [{'id': '1', 'left': '5', 'right': None, 'value': 1}, {'id': '5', 'left': '7', 'right': '9', 'value': 5}, {'id': '9', 'left': None, 'right': '12', 'value': 9}, {'id': '12', 'left': None, 'right': None, 'value': 12}, {'id': '7', 'left': '8', 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '1'}, 4],
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, 0],
    [{'nodes': [{'id': '4', 'left': '2', 'right': None, 'value': 4}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '4'}, 1],
    [{'nodes': [{'id': '4', 'left': '2', 'right': None, 'value': 4}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '4'}, 2],
    [{'nodes': [{'id': '4', 'left': '2', 'right': None, 'value': 4}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': '3', 'value': 1}, {'id': '3', 'left': '19', 'right': None, 'value': 3}, {'id': '19', 'left': None, 'right': None, 'value': 19}], 'root': '4'}, 4],
    [{'nodes': [{'id': '6', 'left': None, 'right': '1', 'value': 6}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '6'}, 1],
    [{'nodes': [{'id': '3', 'left': None, 'right': '10', 'value': 3}, {'id': '10', 'left': '1', 'right': None, 'value': 10}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '3'}, 2],
    [{'nodes': [{'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': '3', 'right': None, 'value': 1}, {'id': '3', 'left': None, 'right': '5', 'value': 3}, {'id': '5', 'left': None, 'right': '10', 'value': 5}, {'id': '10', 'left': None, 'right': None, 'value': 10}], 'root': '2'}, 4]
]

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


@pytest.mark.parametrize("root, expected", cases)
def test_binaryTreeDiameter(root, expected):
    nodes = {}
    for node_json in root['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in root['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None

    assert binaryTreeDiameter(nodes[root['root']])==expected

