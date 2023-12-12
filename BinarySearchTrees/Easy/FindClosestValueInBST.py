r"""
  DESCRIPTION

  Write a function that takes in a Binary Search Tree (BST) and a target integer
  value and returns the closest value to that target value contained in the BST.

  You can assume that there will only be one closest value.

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
        /   \   /   \
       2     5 13   22
     /           \
    1            14

  Time complexity O(logn)
  Space complexity O(1)
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


def findClosestValueInBST(target, tree):
    node = tree
    closest = float('inf')
    delta = float('inf')
    
    while node:
        diff = node.value - target
        if diff==0:
            return target

        if abs(diff)<delta:
            closest = node.value
            delta = abs(diff)
        if target>=node.value:
            node = node.right
        else:
            node = node.left

    return closest


# case [target, tree, expected]
cases = [
    [12, {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': '13', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': None, 'value': 22}, {'id': '13', 'left': None, 'right': '14', 'value': 13}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '5', 'left': '2', 'right': '5-2', 'value': 5}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': None, 'value': 2}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '10'}, 13],
    [100, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 100],
    [208, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 208],
    [4500, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 4500],
    [4501, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 4500],
    [-70, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, -51],
    [2000, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 1001],
    [6, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 5],
    [30000, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 55000],
    [-1, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 1],
    [29751, {'nodes': [{'id': '100', 'left': '5', 'right': '502', 'value': 100}, {'id': '502', 'left': '204', 'right': '55000', 'value': 502}, {'id': '55000', 'left': '1001', 'right': None, 'value': 55000}, {'id': '1001', 'left': None, 'right': '4500', 'value': 1001}, {'id': '4500', 'left': None, 'right': None, 'value': 4500}, {'id': '204', 'left': '203', 'right': '205', 'value': 204}, {'id': '205', 'left': None, 'right': '207', 'value': 205}, {'id': '207', 'left': '206', 'right': '208', 'value': 207}, {'id': '208', 'left': None, 'right': None, 'value': 208}, {'id': '206', 'left': None, 'right': None, 'value': 206}, {'id': '203', 'left': None, 'right': None, 'value': 203}, {'id': '5', 'left': '2', 'right': '15', 'value': 5}, {'id': '15', 'left': '5-2', 'right': '22', 'value': 15}, {'id': '22', 'left': None, 'right': '57', 'value': 22}, {'id': '57', 'left': None, 'right': '60', 'value': 57}, {'id': '60', 'left': None, 'right': None, 'value': 60}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1}, {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1}, {'id': '1-5', 'left': None, 'right': None, 'value': 1}, {'id': '-51', 'left': '-403', 'right': None, 'value': -51}, {'id': '-403', 'left': None, 'right': None, 'value': -403}], 'root': '100'}, 55000],
    [29749, {'nodes': [
                {'id': '100', 'left': '5', 'right': '502', 'value': 100},
                {'id': '502', 'left': '204', 'right': '55000', 'value': 502},
                {'id': '55000', 'left': '1001', 'right': None, 'value': 55000},
                {'id': '1001', 'left': None, 'right': '4500', 'value': 1001},
                {'id': '4500', 'left': None, 'right': None, 'value': 4500},
                {'id': '204', 'left': '203', 'right': '205', 'value': 204},
                {'id': '205', 'left': None, 'right': '207', 'value': 205},
                {'id': '207', 'left': '206', 'right': '208', 'value': 207},
                {'id': '208', 'left': None, 'right': None, 'value': 208},
                {'id': '206', 'left': None, 'right': None, 'value': 206},
                {'id': '203', 'left': None, 'right': None, 'value': 203},
                {'id': '5', 'left': '2', 'right': '15', 'value': 5},
                {'id': '15', 'left': '5-2', 'right': '22', 'value': 15},
                {'id': '22', 'left': None, 'right': '57', 'value': 22},
                {'id': '57', 'left': None, 'right': '60', 'value': 57},
                {'id': '60', 'left': None, 'right': None, 'value': 60},
                {'id': '5-2', 'left': None, 'right': None, 'value': 5},
                {'id': '2', 'left': '1', 'right': '3', 'value': 2},
                {'id': '3', 'left': None, 'right': None, 'value': 3},
                {'id': '1', 'left': '-51', 'right': '1-2', 'value': 1},
                {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1},
                {'id': '1-3', 'left': None, 'right': '1-4', 'value': 1},
                {'id': '1-4', 'left': None, 'right': '1-5', 'value': 1},
                {'id': '1-5', 'left': None, 'right': None, 'value': 1},
                {'id': '-51', 'left': '-403', 'right': None, 'value': -51},
                {'id': '-403', 'left': None, 'right': None, 'value': -403}], 
             'root': '100'}, 4500]
]

@pytest.mark.parametrize("target, tree, expected", cases)
def test_findClosestValueInBST(target, tree, expected):
    nodes = {node['id']:BST(node['id'], node['value']) for node in tree['nodes']}
    for node in tree['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    ic(nodes)
    assert findClosestValueInBST(target, nodes[tree['root']])==expected
