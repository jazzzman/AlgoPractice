"""
  DESCRIPTION

  Write a function that takes in a non-empty sorted array of distinct integers,
  constructs a BST from the integers, and returns the root of the BST.


  The function should minimize the height of the BST.

  You've been provided with a BST class that you'll have to use to
  construct the BST.


  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.


  A BST is valid if and only if all of its nodes are valid
  BST nodes.


  Note that the BST class already has an insert method
  which you can use if you want.



  Time complexity O(nlogn)
  Space complexity O(n)
"""
import pytest

from icecream import ic


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

    def __repr__(self):
        return f'{self.value} {self.left.value if self.left else None} {self.right.value if self.right else None}'


def minHeightBST(array):
    value = array[proc_idx(0,len(array)-1)]
    root = BST(value)
    helper(0,len(array)-1,root, array)

    return root

def helper(start, end, node, array):
    mid = proc_idx(start, end)

    if start<mid:
        left_idx = proc_idx(start,mid-1) 
        node.insert(array[left_idx])
        helper(start,mid-1,node.left, array)

    if mid<end:
        right_idx = proc_idx(mid+1,end) 
        node.insert(array[right_idx])
        helper(mid+1,end,node.right, array)

def proc_idx(start, end)->int:
    return (end+start)//2



# case [array, expected]
cases = [
    [[1, 2, 5, 7, 10, 13, 14, 15, 22], {'nodes': [{'id': '10', 'left': '2', 'right': '14', 'value': 10} , {'id': '14', 'left': '13', 'right': '15', 'value': 14}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '13', 'left': None, 'right': None, 'value': 13}, {'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}],
    [[1], {'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}],
    [[1, 2], {'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}],
    [[1, 2, 5], {'nodes': [{'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}],
    [[1, 2, 5, 7], {'nodes': [{'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '2'}],
    [[1, 2, 5, 7, 10], {'nodes': [{'id': '5', 'left': '1', 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': '10', 'value': 7}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '5'}],
    [[1, 2, 5, 7, 10, 13], {'nodes': [{'id': '5', 'left': '1', 'right': '10', 'value': 5}, {'id': '10', 'left': '7', 'right': '13', 'value': 10}, {'id': '13', 'left': None, 'right': None, 'value': 13}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '5'}],
    [[1, 2, 5, 7, 10, 13, 14], {'nodes': [{'id': '7', 'left': '2', 'right': '13', 'value': 7}, {'id': '13', 'left': '10', 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '7'}],
    [[1, 2, 5, 7, 10, 13, 14, 15], {'nodes': [{'id': '7', 'left': '2', 'right': '13', 'value': 7}, {'id': '13', 'left': '10', 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': '15', 'value': 14}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '7'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22], {'nodes': [{'id': '10', 'left': '2', 'right': '14', 'value': 10}, {'id': '14', 'left': '13', 'right': '15', 'value': 14}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '13', 'left': None, 'right': None, 'value': 13}, {'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22, 28], {'nodes': [{'id': '10', 'left': '2', 'right': '15', 'value': 10}, {'id': '15', 'left': '13', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '28', 'value': 22}, {'id': '28', 'left': None, 'right': None, 'value': 28}, {'id': '13', 'left': None, 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32], {'nodes': [{'id': '13', 'left': '5', 'right': '22', 'value': 13}, {'id': '22', 'left': '14', 'right': '28', 'value': 22}, {'id': '28', 'left': None, 'right': '32', 'value': 28}, {'id': '32', 'left': None, 'right': None, 'value': 32}, {'id': '14', 'left': None, 'right': '15', 'value': 14}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '5', 'left': '1', 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': '10', 'value': 7}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '13'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36], {'nodes': [{'id': '13', 'left': '5', 'right': '22', 'value': 13}, {'id': '22', 'left': '14', 'right': '32', 'value': 22}, {'id': '32', 'left': '28', 'right': '36', 'value': 32}, {'id': '36', 'left': None, 'right': None, 'value': 36}, {'id': '28', 'left': None, 'right': None, 'value': 28}, {'id': '14', 'left': None, 'right': '15', 'value': 14}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '5', 'left': '1', 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': '10', 'value': 7}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '13'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89], {'nodes': [{'id': '14', 'left': '5', 'right': '28', 'value': 14}, {'id': '28', 'left': '15', 'right': '36', 'value': 28}, {'id': '36', 'left': '32', 'right': '89', 'value': 36}, {'id': '89', 'left': None, 'right': None, 'value': 89}, {'id': '32', 'left': None, 'right': None, 'value': 32}, {'id': '15', 'left': None, 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '5', 'left': '1', 'right': '10', 'value': 5}, {'id': '10', 'left': '7', 'right': '13', 'value': 10}, {'id': '13', 'left': None, 'right': None, 'value': 13}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '14'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92], {'nodes': [{'id': '14', 'left': '5', 'right': '32', 'value': 14}, {'id': '32', 'left': '22', 'right': '89', 'value': 32}, {'id': '89', 'left': '36', 'right': '92', 'value': 89}, {'id': '92', 'left': None, 'right': None, 'value': 92}, {'id': '36', 'left': None, 'right': None, 'value': 36}, {'id': '22', 'left': '15', 'right': '28', 'value': 22}, {'id': '28', 'left': None, 'right': None, 'value': 28}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '5', 'left': '1', 'right': '10', 'value': 5}, {'id': '10', 'left': '7', 'right': '13', 'value': 10}, {'id': '13', 'left': None, 'right': None, 'value': 13}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '14'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92, 9000], {'nodes': [{'id': '15', 'left': '7', 'right': '36', 'value': 15}, {'id': '36', 'left': '28', 'right': '92', 'value': 36}, {'id': '92', 'left': '89', 'right': '9000', 'value': 92}, {'id': '9000', 'left': None, 'right': None, 'value': 9000}, {'id': '89', 'left': None, 'right': None, 'value': 89}, {'id': '28', 'left': '22', 'right': '32', 'value': 28}, {'id': '32', 'left': None, 'right': None, 'value': 32}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '7', 'left': '2', 'right': '13', 'value': 7}, {'id': '13', 'left': '10', 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '15'}],
    [[1, 2, 5, 7, 10, 13, 14, 15, 22, 28, 32, 36, 89, 92, 9000, 9001], {'nodes': [{'id': '15', 'left': '7', 'right': '36', 'value': 15}, {'id': '36', 'left': '28', 'right': '92', 'value': 36}, {'id': '92', 'left': '89', 'right': '9000', 'value': 92}, {'id': '9000', 'left': None, 'right': '9001', 'value': 9000}, {'id': '9001', 'left': None, 'right': None, 'value': 9001}, {'id': '89', 'left': None, 'right': None, 'value': 89}, {'id': '28', 'left': '22', 'right': '32', 'value': 28}, {'id': '32', 'left': None, 'right': None, 'value': 32}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '7', 'left': '2', 'right': '13', 'value': 7}, {'id': '13', 'left': '10', 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '2', 'left': '1', 'right': '5', 'value': 2}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '15'}] 
]

def preOrderDFS(node, array):
    if node:
        ic(node)
        preOrderDFS(node.left, array)
        array.append(node.value)
        preOrderDFS(node.right, array)
    return array

@pytest.mark.parametrize("array, expected", cases)
def test_minHeightBST(array, expected):
    nodes = {node['id']:BST(node['value']) for node in expected['nodes']}
    for node in expected['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    ic(nodes)
    root = minHeightBST(array)

    assert preOrderDFS(root,[])==preOrderDFS(nodes[expected['root']],[])

