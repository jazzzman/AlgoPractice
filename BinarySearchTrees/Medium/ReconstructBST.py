"""
  DESCRIPTION

  The pre-order traversal of a Binary Tree is a traversal technique that starts
  at the tree's root node and visits nodes in the following order:

  Current node
  Left subtree
  Right subtree

  Given a non-empty array of integers representing the pre-order traversal of a
  Binary Search Tree (BST), write a function that creates the relevant BST and 
  returns its root node.


  The input array will contain the values of BST nodes in the order in which   
  these nodes would be visited with a pre-order traversal.


  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.



  Time complexity O(n)
  Space complexity O(n)
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

def reconstrunctBST(array):
    bounds = [float('-inf'), float('inf')]
    value = array.pop(0)
    root = BST(str(value), value)
    
    helper(array,root,bounds)
    return root

def helper(array,node, bounds):
    if array and array[0]<node.value and array[0]>=bounds[0]:
        value = array.pop(0)
        node.left = BST(str(value), value)
        helper(array,node.left,[bounds[0],node.value])
    if array and array[0]>=node.value and array[0]<bounds[1]:
        value = array.pop(0)
        node.right = BST(str(value),value)
        helper(array,node.right,[node.value,bounds[1]])


# case [array, expected]
cases = [
    [[10, 4, 2, 1, 5, 17, 19, 18], {'nodes': [{'id': '10', 'left': '4', 'right': '17', 'value': 10}, {'id': '17', 'left': None, 'right': '19', 'value': 17}, {'id': '19', 'left': '18', 'right': None, 'value': 19}, {'id': '18', 'left': None, 'right': None, 'value': 18}, {'id': '4', 'left': '2', 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}],
    [[100], {'nodes': [{'id': '100', 'left': None, 'right': None, 'value': 100}], 'root': '100'}],
    [[10, 9, 8, 7, 6, 5], {'nodes': [{'id': '10', 'left': '9', 'right': None, 'value': 10}, {'id': '9', 'left': '8', 'right': None, 'value': 9}, {'id': '8', 'left': '7', 'right': None, 'value': 8}, {'id': '7', 'left': '6', 'right': None, 'value': 7}, {'id': '6', 'left': '5', 'right': None, 'value': 6}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '10'}],
    [[5, 6, 7, 8], {'nodes': [{'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': '8', 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '5'}],
    [[5, -10, -5, 6, 9, 7], {'nodes': [{'id': '5', 'left': '-10', 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '9', 'value': 6}, {'id': '9', 'left': '7', 'right': None, 'value': 9}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '-10', 'left': None, 'right': '-5', 'value': -10}, {'id': '-5', 'left': None, 'right': None, 'value': -5}], 'root': '5'}],
    [[10, 4, 2, 1, 3, 5, 6, 9, 7, 17, 19, 18], {'nodes': [{'id': '10', 'left': '4', 'right': '17', 'value': 10}, {'id': '17', 'left': None, 'right': '19', 'value': 17}, {'id': '19', 'left': '18', 'right': None, 'value': 19}, {'id': '18', 'left': None, 'right': None, 'value': 18}, {'id': '4', 'left': '2', 'right': '5', 'value': 4}, {'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '9', 'value': 6}, {'id': '9', 'left': '7', 'right': None, 'value': 9}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}],
    [[1, 0, 2], {'nodes': [{'id': '1', 'left': '0', 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '0', 'left': None, 'right': None, 'value': 0}], 'root': '1'}],
    [[2, 0, 1], {'nodes': [{'id': '2', 'left': '0', 'right': None, 'value': 2}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}],
    [[2, 0, 1, 4, 3], {'nodes': [{'id': '2', 'left': '0', 'right': '4', 'value': 2}, {'id': '4', 'left': '3', 'right': None, 'value': 4}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}],
    [[2, 0, 1, 4, 3, 3], {'nodes': [{'id': '2', 'left': '0', 'right': '4', 'value': 2}, {'id': '4', 'left': '3', 'right': None, 'value': 4}, {'id': '3', 'left': None, 'right': '3-2', 'value': 3}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}],
    [[2, 0, 1, 3, 4, 3], {'nodes': [{'id': '2', 'left': '0', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '4', 'left': '3-2', 'right': None, 'value': 4}, {'id': '3-2', 'left': None, 'right': None, 'value': 3}, {'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}],
]

def preOreder(node,array):
    if node:
        preOreder(node.left, array)
        array.append(node.value)
        preOreder(node.right, array)

@pytest.mark.parametrize("array, expected", cases)
def test_reconstrunctBST(array, expected):
    nodes = {node['id']:BST(node['id'], node['value']) for node in expected['nodes']}
    for node in expected['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    ic(nodes)
    expArray = []
    preOreder(nodes[expected['root']], expArray)

    resultArray = []
    preOreder(reconstrunctBST(array),resultArray)

    assert resultArray == expArray
