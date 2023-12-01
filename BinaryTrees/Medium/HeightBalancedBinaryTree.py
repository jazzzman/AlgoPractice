"""
  DESCRIPTION

  You're given the root node of a Binary Tree. Write a function that returns
  true if this Binary Tree is height balanced and
  false if it isn't.

  A Binary Tree is height balanced if for each node in the tree, the difference
  between the height of its left subtree and the height of its right subtree is
  at most 1.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.


  Time complexity O(###)
  Space complexity O(###)
"""
import pytest

from typing import Optional


class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


def heightBalancedBinaryTree(tree):
    result = dfs(tree)
    return True if result is not None else False

def dfs(node) -> Optional[int]:
    if node:
        left_branch = dfs(node.left)
        right_branch = dfs(node.right)

        if left_branch is None or right_branch is None:
            return None

        if abs(left_branch-right_branch)>1:
            return None
        else:
            return max(left_branch,right_branch)+1
    return 0



# case [tree, expected]
cases = [
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'right': '6', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': '7', 'right': '8', 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'right': '6', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': '7', 'right': '8', 'value': 5}, {'id': '6', 'left': '9', 'right': '10', 'value': 6}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '11', 'right': '6', 'value': 3}, {'id': '11', 'left': None, 'right': None, 'value': 11}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': '7', 'right': '8', 'value': 5}, {'id': '6', 'left': '9', 'right': '10', 'value': 6}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': '5', 'value': 4}, {'id': '4', 'left': '6', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '7', 'value': 2}, {'id': '3', 'left': '8', 'right': '5', 'value': 4}, {'id': '4', 'left': '6', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': '9', 'right': '10', 'value': 5}, {'id': '6', 'left': '11', 'right': '12', 'value': 6}, {'id': '7', 'left': '13', 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '11', 'left': None, 'right': None, 'value': 11}, {'id': '12', 'left': None, 'right': None, 'value': 12}, {'id': '13', 'left': None, 'right': None, 'value': 13}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': '9', 'right': '10', 'value': 5}, {'id': '6', 'left': None, 'right': '12', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '11', 'left': None, 'right': None, 'value': 11}, {'id': '12', 'left': None, 'right': '13', 'value': 12}, {'id': '13', 'left': None, 'right': None, 'value': 13}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': None, 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': '4', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 2}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': None, 'value': 4}, {'id': '5', 'left': '12', 'right': None, 'value': 5}, {'id': '6', 'left': '9', 'right': '10', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': '11', 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '11', 'left': None, 'right': None, 'value': 11}, {'id': '12', 'left': None, 'right': None, 'value': 12}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': None, 'value': 4}, {'id': '5', 'left': '12', 'right': None, 'value': 5}, {'id': '6', 'left': '9', 'right': '10', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '12', 'left': None, 'right': None, 'value': 12}], 'root': '1'}, True]
]

@pytest.mark.parametrize("root, expected", cases)
def test_heightBalancedBinaryTree(root, expected):
    nodes = {}
    for node_json in root['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in root['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None

    assert heightBalancedBinaryTree(nodes[root['root']])==expected

