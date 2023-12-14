r"""
  DESCRIPTION

  Write a function that takes in a potentially invalid Binary Search Tree (BST)
  and returns a boolean representing whether the BST is valid.


  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.


  A BST is valid if and only if all of its nodes are valid
  BST nodes.
        Valid Tree         
              10        
           /     \     
          5      15   
        /   \   /   \
       2     5 13   22   
     /           \      
    1            14    


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

def validateBST(tree, boundaries=None):
    node = tree
    boundaries = [float('-inf'),float('inf')] if not boundaries else boundaries
    if node:
        if boundaries[0]<=node.value<boundaries[1]:
            left = validateBST(node.left,[boundaries[0],node.value])
            right = validateBST(node.right,[node.value,boundaries[1]])
            if not left or not right:
                return False
        else:
            return False

    return True


# case [tree, expected]
cases = [
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': '13', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '13', 'left': None, 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}, True],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': '-5', 'right': None, 'value': 1}, {'id': '-5', 'left': '-15', 'right': '-5-2', 'value': -5}, {'id': '-5-2', 'left': None, 'right': '-2', 'value': -5}, {'id': '-2', 'left': None, 'right': '-1', 'value': -2}, {'id': '-1', 'left': None, 'right': None, 'value': -1}, {'id': '-15', 'left': '-22', 'right': None, 'value': -15}, {'id': '-22', 'left': None, 'right': None, 'value': -22}], 'root': '10'}, True],
    [{'nodes': [{'id': '10', 'left': None, 'right': None, 'value': 10}], 'root': '10'}, True],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '500', 'value': 22}, {'id': '500', 'left': '50', 'right': '1500', 'value': 500}, {'id': '1500', 'left': None, 'right': '10000', 'value': 1500}, {'id': '10000', 'left': '2200', 'right': None, 'value': 10000}, {'id': '2200', 'left': None, 'right': None, 'value': 2200}, {'id': '50', 'left': None, 'right': '200', 'value': 50}, {'id': '200', 'left': None, 'right': None, 'value': 200}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}, True],
    [{'nodes': [{'id': '5000', 'left': '5', 'right': '55000', 'value': 5000}, {'id': '55000', 'left': None, 'right': None, 'value': 55000}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '502', 'value': 22}, {'id': '502', 'left': '204', 'right': None, 'value': 502}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}], 'root': '5000'}, True],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': '11', 'value': 5}, {'id': '11', 'left': None, 'right': None, 'value': 11}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}, False],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': '-5', 'right': None, 'value': 1}, {'id': '-5', 'left': '-15', 'right': '-5-2', 'value': -5}, {'id': '-5-2', 'left': None, 'right': '-2', 'value': -5}, {'id': '-2', 'left': None, 'right': '-1', 'value': -2}, {'id': '-1', 'left': None, 'right': None, 'value': -1}, {'id': '-15', 'left': '-22', 'right': None, 'value': -15}, {'id': '-22', 'left': '11', 'right': None, 'value': -22}, {'id': '11', 'left': None, 'right': None, 'value': 11}], 'root': '10'}, False],
    [{'nodes': [{'id': '10', 'left': '11', 'right': '12', 'value': 10}, {'id': '12', 'left': None, 'right': None, 'value': 12}, {'id': '11', 'left': None, 'right': None, 'value': 11}], 'root': '10'}, False],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '500', 'value': 22}, {'id': '500', 'left': '50', 'right': '1500', 'value': 500}, {'id': '1500', 'left': None, 'right': '10000', 'value': 1500}, {'id': '10000', 'left': '2200', 'right': '9999', 'value': 10000}, {'id': '9999', 'left': None, 'right': None, 'value': 9999}, {'id': '2200', 'left': None, 'right': None, 'value': 2200}, {'id': '50', 'left': None, 'right': '200', 'value': 50}, {'id': '200', 'left': None, 'right': None, 'value': 200}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}, False],
    [{'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': None, 'right': None, 'value': 55000}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': '300', 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '300', 'left': None, 'right': None, 'value': 300}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}], 'root': '100'}, False],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '5', 'left': None, 'right': '10-2', 'value': 5}, {'id': '10-2', 'left': None, 'right': None, 'value': 10}], 'root': '10'}, False],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': '13', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '13', 'left': None, 'right': '16', 'value': 13}, {'id': '16', 'left': None, 'right': None, 'value': 16}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}, False],
    [{'nodes': [
        {'id': '10', 'left': '5', 'right': '15', 'value': 10},
        {'id': '15', 'left': '13', 'right': '22', 'value': 15},
        {'id': '22', 'left': None, 'right': None, 'value': 22},
        {'id': '13', 'left': None, 'right': '14', 'value': 5},
        {'id': '14', 'left': None, 'right': None, 'value': 14},
        {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
        {'id': '5-2', 'left': None, 'right': None, 'value': 5},
        {'id': '2', 'left': '1', 'right': None, 'value': 2},
        {'id': '1', 'left': None, 'right': None, 'value': 1}]
      , 'root': '10'}, False]
]

@pytest.mark.parametrize("tree, expected", cases)
def test_validateBST(tree, expected):
    nodes = {node['id']:BST(node['id'], node['value']) for node in tree['nodes']}
    for node in tree['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    ic(nodes)
    assert validateBST(nodes[tree['root']])==expected
