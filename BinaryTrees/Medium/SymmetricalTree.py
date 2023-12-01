"""
  DESCRIPTION

  Write a function that takes in a Binary Tree and returns if that tree is
  symmetrical. A tree is symmetrical if the left and right subtrees are
  mirror images of each other.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.


  Time complexity O(n)
  Space complexity O(h) - h height of the tree
"""
import pytest


class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def symmetricalTree(tree) -> bool:
    left = [tree.left]
    right = [tree.right]

    while left and right:
        left_node = left.pop(0)
        right_node = right.pop(0)

        if left_node is None and right_node is None:
            continue

        if left_node is None or right_node is None or left_node.value!=right_node.value:
            return False

        left.append(left_node.left)
        left.append(left_node.right)
        right.append(right_node.right)
        right.append(right_node.left)

    return True

# case [tree, expected]
cases = [
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '2-2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '2-2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': '3', 'right': '3-2', 'value': 2}, {'id': '2-2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': '3', 'right': '3-2', 'value': 2}, {'id': '2-2', 'left': '3-3', 'right': '3-4', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '3-3', 'left': None, 'right': None, 'value': 3}, {'id': '3-4', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': '3', 'right': '4', 'value': 2}, {'id': '2-2', 'left': '4-2', 'right': '3-2', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '4-2', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, True],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': '3', 'right': '4', 'value': 2}, {'id': '2-2', 'left': '3-2', 'right': '4-2', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '4-2', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '5', 'value': 1}, {'id': '2', 'left': '3', 'right': '4', 'value': 2}, {'id': '5', 'left': '4-2', 'right': '3-2', 'value': 5}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '4-2', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': '3', 'right': '4', 'value': 2}, {'id': '2-2', 'left': '4-2', 'right': '3-2', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '4-2', 'left': None, 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '1'}, False],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '2-2', 'value': 1}, {'id': '2', 'left': '3', 'right': '4', 'value': 2}, {'id': '2-2', 'left': '4-2', 'right': '3-2', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': '5-2', 'right': None, 'value': 4}, {'id': '4-2', 'left': None, 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}], 'root': '1'}, True]
]

@pytest.mark.parametrize("tree, expected", cases)
def test_symmetricalTree(tree, expected):
    nodes = {}
    for node_json in tree['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in tree['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None

    assert symmetricalTree(nodes[tree['root']])==expected

