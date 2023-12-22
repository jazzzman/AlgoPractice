r"""
  DESCRIPTION

  Write a function that takes in a Binary Search Tree (BST) and a positive     
  integer k and returns the kth largest integer contained in the
  BST.


  You can assume that there will only be integer values in the BST and that    
  k is less than or equal to the number of nodes in the tree.


  Also, for the purpose of this question, duplicate integers will be treated as
  distinct values. In other words, the second largest value in a BST containing
  values {5, 7, 7} will be 7—not 5.


  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.

              15
           /     \
          5      20
        /   \   /   \
       2     5 17   22
     /   \         
    1     3       


  Time complexity O(###)
  Space complexity O(###)
"""
import pytest

from icecream import ic


class BST:
    def __init__(self, id, value):
        self.id = id
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return (f'id: {self.id} value: {self.value} '
               f'left: {self.left.id if self.left else None} '
               f'right: {self.right.id if self.right else None}')

def findKthLargestValueInBST(k, node):
    array = []
    helper(node, array)

    return array[-k]

def helper(node, array):
    if node:
        helper(node.left, array)
        array.append(node.value)
        helper(node.right, array)

# case [k, node, expected]
cases = [
    [3, {'nodes': [{'id': '15', 'left': '5', 'right': '20', 'value': 15}, {'id': '20', 'left': '17', 'right': '22', 'value': 20}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '17', 'left': None, 'right': None, 'value': 17}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '15'}, 17],
    [1, {'nodes': [{'id': '5', 'left': '4', 'right': '6', 'value': 5}, {'id': '4', 'left': '3', 'right': None, 'value': 4}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '5'}, 7],
    [1, {'nodes': [{'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '5'}, 5],
    [3, {'nodes': [{'id': '20', 'left': '15', 'right': '25', 'value': 20}, {'id': '15', 'left': '10', 'right': '19', 'value': 15}, {'id': '25', 'left': '21', 'right': '30', 'value': 25}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '19', 'left': None, 'right': None, 'value': 19}, {'id': '21', 'left': None, 'right': '22', 'value': 21}, {'id': '30', 'left': None, 'right': None, 'value': 30}, { 'id': '22', 'left': None, 'right': None, 'value': 22}], 'root': '20'}, 22],
    [5, {'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '4', 'left': None, 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '1'}, 1],
    [2, {'nodes': [{'id': '10', 'left': '8', 'right': None, 'value': 10}, {'id': '8', 'left': '6', 'right': None, 'value': 8}, {'id': '6', 'left': '4', 'right': None, 'value': 6}, {'id': '4', 'left': '2', 'right': None, 'value': 4}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '10'}, 8],
    [5, {'nodes': [{'id': '10', 'left': '8', 'right': None, 'value': 10}, {'id': '8', 'left': '6', 'right': '9', 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '6', 'left': '4', 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '4', 'left': '2', 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': None, 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '10'}, 6],
    [1, {'nodes': [{'id': '99727', 'left': '99', 'right': None, 'value': 99727}, {'id': '99', 'left': None, 'right': '727', 'value': 99}, {'id': '727', 'left': None, 'right': None, 'value': 727}], 'root': '99727'}, 99727],
    [7, {'nodes': [{'id': '15', 'left': '5', 'right': '20', 'value': 15}, {'id': '20', 'left': '17', 'right': '22', 'value': 20}, {'id': '22', 'left': None, 'right': '24', 'value': 22}, {'id': '24', 'left': '23', 'right': '25', 'value': 24}, {'id': '23', 'left': None, 'right': None, 'value': 23}, {'id': '25', 'left': None, 'right': None, 'value': 25}, {'id': '17', 'left': None, 'right': None, 'value': 17}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '15'}, 15],
    [5, {'nodes': [{'id': '15', 'left': '5', 'right': '20', 'value': 15}, {'id': '20', 'left': '17', 'right': '22', 'value': 20}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '17', 'left': None, 'right': None, 'value': 17}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '15'}, 5],
    [6, {'nodes': [{'id': '15', 'left': '5', 'right': '20', 'value': 15}, {'id': '20', 'left': '17', 'right': '22', 'value': 20}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '17', 'left': None, 'right': None, 'value': 17}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '15'}, 5]
]

@pytest.mark.parametrize("k, tree, expected", cases)
def test_findKthLargestValueInBST(k, tree, expected):
    nodes = {node['id']:BST(node['id'], node['value']) for node in tree['nodes']}
    for node in tree['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    ic(nodes)
    assert findKthLargestValueInBST(k, nodes[tree['root']])==expected
