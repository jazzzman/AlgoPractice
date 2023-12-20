r"""
  DESCRIPTION

  Write three functions that take in a Binary Search Tree (BST) and an empty    
  array, traverse the BST, add its nodes' values to the input array, and return 
  that array. The three functions should traverse the BST using the in-order,   
  pre-order, and post-order tree-traversal techniques, respectively.


  If you're unfamiliar with tree-traversal techniques, we recommend watching the
  Conceptual Overview section of this question's video explanation before       
  starting to code.


  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.

                      10
                   /     \
                  5      15
                /   \       \
               2     5       22
             /
            1


    inOrderTraverse: [1, 2, 5, 5, 10, 15, 22]
    preOrderTraverse: [10, 5, 2, 1, 5, 15, 22]
    postOrderTraverse: [1, 2, 5, 5, 22, 15, 10]

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

def bSTTraversal(tree, dict_orders):
    dict_orders['inOrderArray'] = inOrderTraverse(tree, [])
    dict_orders['preOrderArray'] = preOrderTraverse(tree, [])
    dict_orders['postOrderArray'] = postOrderTraverse(tree, [])
    return dict_orders

def inOrderTraverse(tree, array):
    if tree:
        inOrderTraverse(tree.left,array)
        array.append(tree.value)
        inOrderTraverse(tree.right,array)
    return array

def preOrderTraverse(tree, array):
    if tree:
        array.append(tree.value)
        preOrderTraverse(tree.left, array)
        preOrderTraverse(tree.right, array)
    return array

def postOrderTraverse(tree, array):
    if tree:
        postOrderTraverse(tree.left, array)
        postOrderTraverse(tree.right, array)
        array.append(tree.value)
    return array

# case [tree, array, expected]
cases = [
    [{'nodes': [
        {'id': '10', 'left': '5', 'right': '15', 'value': 10},
        {'id': '15', 'left': None, 'right': '22', 'value': 15},
        {'id': '22', 'left': None, 'right': None, 'value': 22},
        {'id': '5', 'left': '2', 'right': '5-2', 'value': 5},
        {'id': '5-2', 'left': None, 'right': None, 'value': 5},
        {'id': '2', 'left': '1', 'right': None, 'value': 2},
        {'id': '1', 'left': None, 'right': None, 'value': 1}], 
      'root': '10'},
     {'inOrderArray': [1, 2, 5, 5, 10, 15, 22], 
      'postOrderArray': [1, 2, 5, 5, 22, 15, 10], 
      'preOrderArray': [10, 5, 2, 1, 5, 15, 22]}],
    [{'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, {'inOrderArray': [-403, -51, 1, 1, 1, 1, 1, 2, 3, 5, 5, 15, 22, 57, 60, 100, 203, 204, 205, 206, 207, 208, 502, 1001, 4500, 55000], 'postOrderArray': [-403, -51, 1, 1, 1, 1, 1, 3, 2, 5, 60, 57, 22, 15, 5, 203, 206, 208, 207, 205, 204, 4500, 1001, 55000, 502, 100], 'preOrderArray': [100, 5, 2, 1, -51, -403, 1, 1, 1, 1, 3, 15, 5, 22, 57, 60, 502, 204, 203, 205, 207, 206, 208, 55000, 1001, 4500]}],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': '-5', 'right': None, 'value': 1}, {'id': '-5', 'left': '-15', 'right': '-5-2', 'value': -5}, {'id': '-5-2', 'left': None, 'right': '-2', 'value': -5}, {'id': '-2', 'left': None, 'right': '-1', 'value': -2}, {'id': '-1', 'left': None, 'right': None, 'value': -1}, {'id': '-15', 'left': '-22', 'right': None, 'value': -15}, {'id': '-22', 'left': None, 'right': None, 'value': -22}], 'root': '10'}, {'inOrderArray': [-22, -15, -5, -5, -2, -1, 1, 2, 5, 5, 10, 15, 22], 'postOrderArray': [-22, -15, -1, -2, -5, -5, 1, 2, 5, 5, 22, 15, 10], 'preOrderArray': [10, 5, 2, 1, -5, -15, -22, -5, -2, -1, 5, 15, 22]}],
    [{'nodes': [{'id': '10', 'left': None, 'right': None, 'value': 10}], 'root': '10'}, {'inOrderArray': [10], 'postOrderArray': [10], 'preOrderArray': [10]}],
    [{'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '500', 'value': 22}, {'id': '500', 'left': '50', 'right': '1500', 'value': 500}, {'id': '1500', 'left': None, 'right': '10000', 'value': 1500}, {'id': '10000', 'left': '2200', 'right': None, 'value': 10000}, {'id': '2200', 'left': None, 'right': None, 'value': 2200}, {'id': '50', 'left': None, 'right': '200', 'value': 50}, {'id': '200', 'left': None, 'right': None, 'value': 200}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}, {'inOrderArray': [1, 2, 5, 5, 10, 15, 22, 50, 200, 500, 1500, 2200, 10000], 'postOrderArray': [1, 2, 5, 5, 200, 50, 2200, 10000, 1500, 500, 22, 15, 10], 'preOrderArray': [10, 5, 2, 1, 5, 15, 22, 500, 50, 200, 1500, 10000, 2200]}],
    [{'nodes': [{'id': '5000', 'left': '5', 'right': '55000', 'value': 5000}, {'id': '55000', 'left': None, 'right': None, 'value': 55000}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '502', 'value': 22}, {'id': '502', 'left': '204', 'right': None, 'value': 502}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}], 'root': '5000'}, {'inOrderArray': [1, 1, 1, 1, 1, 2, 3, 5, 5, 15, 22, 203, 204, 205, 206, 207, 208, 502, 5000, 55000], 'postOrderArray': [1, 1, 1, 1, 1, 3, 2, 5, 203, 206, 208, 207, 205, 204, 502, 22, 15, 5, 55000, 5000], 'preOrderArray': [5000, 5, 2, 1, 1, 1, 1, 1, 3, 15, 5, 22, 502, 204, 203, 205, 207, 206, 208, 55000]}]
]

@pytest.mark.parametrize("tree, expected", cases)
def test_bSTTraversal(tree, expected):
    nodes = {node['id']:BST(node['id'], node['value']) for node in tree['nodes']}
    for node in tree['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    ic(nodes)
    dict_orders = {
        'inOrderArray':None,
        'postOrderArray':None,
        'preOrderArray':None
    }
    assert bSTTraversal(nodes[tree['root']], dict_orders)==expected
