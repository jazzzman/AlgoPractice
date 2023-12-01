"""
  DESCRIPTION

  Write a function that takes in a Binary Tree with at least one node and
  checks if that Binary Tree can be split into two Binary Trees of equal sum by
  removing a single edge. If this split is possible, return the new sum of each
  Binary Tree, otherwise return 0. Note that you do not need to return the edge
  that was removed.

  The sum of a Binary Tree is the sum of all values in that Binary Tree.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.

  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


isSplitable = False
def splitBinaryTree(tree):
    global isSplitable
    isSplitable = False
    if tree.left is None and tree.right is None:
        return 0
    total_sum = dfs(tree)

    dfs(tree, total_sum)

    return total_sum/2 if isSplitable else 0

def dfs(node, total_sum = None):
    global isSplitable
    if node:
        left_sum = dfs(node.left, total_sum)
        right_sum = dfs(node.right, total_sum)

        if (total_sum is not None and (left_sum == total_sum/2 or right_sum == total_sum/2)):
            isSplitable = True
        return left_sum + right_sum + node.value
    else:
        return 0


# case [tree, expected]
cases = [
    [{'nodes': [{'id': '0', 'left': None, 'right': None, 'value': 0}], 'root': '0'}, 0],
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, 0],
    [{'nodes': [{'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '2'}, 0],
    [{'nodes': [{'id': '-2', 'left': None, 'right': None, 'value': -2}], 'root': '-2'}, 0],
    [{'nodes': [{'id': '2', 'left': None, 'right': '2-2', 'value': 2}, {'id': '2-2', 'left': None, 'right': None, 'value': 2}], 'root': '2'}, 2],
    [{'nodes': [{'id': '1', 'left': None, 'right': '1-2', 'value': 1}, {'id': '1-2', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, 1],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 3],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '4', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '1-2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '1-2', 'left': None, 'right': '1-3', 'value': 1}, {'id': '1-3', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '1-2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '1-2', 'left': None, 'right': '2-2', 'value': 1}, {'id': '2-2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, 3],
    [{'nodes': [{'id': '1', 'left': '6', 'right': '3', 'value': 1}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '3', 'left': None, 'right': '2', 'value': 3}, {'id': '2', 'left': None, 'right' : None, 'value': 2}], 'root': '1'}, 6],
    [{'nodes': [{'id': '1', 'left': '6', 'right': '3', 'value': 1}, {'id': '6', 'left': '6-2', 'right': None, 'value': 6}, {'id': '3', 'left': None, 'right': '10', 'value': 3}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '6-2', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, 13],
    [{'nodes': [{'id': '1', 'left': '6', 'right': '3', 'value': 1}, {'id': '6', 'left': '6-2', 'right': None, 'value': 6}, {'id': '3', 'left': None, 'right': '8', 'value': 3}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '6-2', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, 12],
    [{'nodes': [{'id': '1', 'left': '6', 'right': '3', 'value': 1}, {'id': '6', 'left': '6-2', 'right': None, 'value': 6}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '6-2', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'right': '7', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}, 11],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '2', 'value': 1}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '2', 'left': '15', 'right': '10', 'value': 2}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '10', 'left': '100', 'right': '200', 'value': 10}, {'id': '100', 'left': None, 'right': None, 'value': 100}, {'id': '200', 'left': None, 'right': None, 'value': 200}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '20', 'value': 1}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '20', 'left': '30', 'right': '10', 'value': 20}, {'id': '30', 'left': None, 'right': None, 'value': 30}, {'id': '10', 'left': '35', 'right': '15', 'value': 10}, {'id': '35', 'left': None, 'right': None, 'value': 35}, {'id': '15', 'left': None, 'right': None, 'value': 15}], 'root': '1'}, 60],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '20', 'value': 1}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '20', 'left': '30', 'right': '10', 'value': 20}, {'id': '30', 'left': None, 'right': None, 'value': 30}, {'id': '10', 'left': '35', 'right': '25', 'value': 10}, {'id': '35', 'left': None, 'right': None, 'value': 35}, {'id': '25', 'left': None, 'right': None, 'value': 25}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '20', 'value': 1}, {'id': '9', 'left': '5', 'right': '2', 'value': 9}, {'id': '20', 'left': '30', 'right': '10', 'value': 20}, {'id': '30', 'left': None, 'right': None, 'value': 30}, {'id': '10', 'left': '35', 'right': '25', 'value': 10}, {'id': '35', 'left': None, 'right': None, 'value': 35}, {'id': '25', 'left': None, 'right': None, 'value': 25}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 70],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '20', 'value': 1}, {'id': '9', 'left': '5', 'right': '2', 'value': 9}, {'id': '20', 'left': '30', 'right': '10', 'value': 20}, {'id': '30', 'left': None, 'right': None, 'value': 30}, {'id': '10', 'left': '35', 'right': '25', 'value': 10}, {'id': '35', 'left': '3', 'right': None, 'value': 35}, {'id': '25', 'left': None, 'right': None, 'value': 25}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '20', 'value': 1}, {'id': '9', 'left': '5', 'right': '2', 'value': 9}, {'id': '20', 'left': '30', 'right': '10', 'value': 20}, {'id': '30', 'left': None, 'right': None, 'value': 30}, {'id': '10', 'left': '35', 'right': '25', 'value': 10}, {'id': '35', 'left': None, 'right': None, 'value': 35}, {'id': '25', 'left': None, 'right': None, 'value': 25}, {'id': '5', 'left': '102', 'right': None, 'value': 5}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '102', 'left': None, 'right': None, 'value': 102}], 'root': '1'}, 121],
    [{'nodes': [{'id': '1', 'left': '20', 'right': '9', 'value': 1}, {'id': '9', 'left': '5', 'right': '2', 'value': 9}, {'id': '20', 'left': '30', 'right': '10', 'value': 20}, {'id': '30', 'left': None, 'right': None, 'value': 30}, {'id': '10', 'left': '35', 'right': '25', 'value': 10}, {'id': '35', 'left': None, 'right': None, 'value': 35}, {'id': '25', 'left': None, 'right': None, 'value': 25}, {'id': '5', 'left': '102', 'right': None, 'value': 5}, {'id': '2', 'left': '3', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '102', 'left': None, 'right': None, 'value': 102}], 'root': '1'}, 121],
    [{'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '4', 'left': None, 'right' : '5', 'value': 4}, {'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '4', 'left': None, 'right' : '5', 'value': 4}, {'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '9', 'value': 6}, {'id': '9', 'left': None, 'right': None, 'value': 9}], 'root': '1'}, 15],
    [{'nodes': [{'id': '-2', 'left': None, 'right': '-2-2', 'value': -2}, {'id': '-2-2', 'left': None, 'right': None, 'value': -2}], 'root': '-2'}, -2],
    [{'nodes': [{'id': '-2', 'left': None, 'right': '0', 'value': -2}, {'id': '0', 'left': None, 'right': None, 'value': 0}], 'root': '-2'}, 0],
    [{'nodes': [{'id': '1', 'left': '1-1', 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': '-5', 'value': 2}, {'id': '1-1', 'left': '12', 'right': None, 'value': 1}, {'id': '12', 'left': None, 'right': '-21', 'value': 12}, {'id': '-21', 'left': None, 'right': None, 'value': -21}, {'id': '-5', 'left': None, 'right': None, 'value': -5}], 'root': '1'}, -5],
    [{'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': '-4', 'value': 3}, {'id': '-4', 'left': None, 'right': '5', 'value': -4}, {'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': '9', 'value': 6}, {'id': '9', 'left': None, 'right': None, 'value': 9}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': '-4', 'value': 3}, {'id': '-4', 'left': None, 'right': '9', 'value': -4}, {'id': '9', 'left': None, 'right': '5', 'value': 9}, {'id': '5', 'left': None, 'right': '6', 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, 11],
    [{'nodes': [{'id': '1', 'left': '-20', 'right': '9', 'value': 1},
                {'id': '9', 'left': '-13', 'right': '4', 'value': 9},
                {'id': '-20', 'left': '-30', 'right': '17', 'value': -20},
                {'id': '-30', 'left': '8' , 'right': None, 'value': -30},
                {'id': '17', 'left': '-26', 'right': '-17', 'value': 17}, 
                {'id': '-26', 'left': '19', 'right': None, 'value': -26}, 
                {'id': '-17', 'left': None, 'right': None, 'value': -17}, 
                {'id': '-13', 'left': '42', 'right': None, 'value': -13}, 
                {'id': '4', 'left': '3', 'right': '-11', 'value': 4},
                {'id': '3', 'left': None, 'right': None, 'value': 3},
                {'id': '42', 'left': None, 'right': None, 'value': 42},
                {'id': '19', 'left': None, 'right': None, 'value': 19},
                {'id': '8', 'left': None, 'right': None, 'value': 8}, 
                {'id': '-11', 'left': None, 'right': None, 'value': -11}], 'root': '1'}, -7]
]

@pytest.mark.parametrize("tree, expected", cases)
def test_splitBinaryTree(tree, expected):
    nodes = {}
    for node_json in tree['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in tree['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None

    assert splitBinaryTree(nodes[tree['root']])==expected

