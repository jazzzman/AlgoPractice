"""
  DESCRIPTION

    You're given a binary expression tree. Write a function to evaluate
    this tree mathematically and return a single resulting integer.
 
    All leaf nodes in the tree represent operands, which will always be positive
    integers. All of the other nodes represent operators. There are 4 operators
    supported, each of which is represented by a negative integer:
 
      -1: Addition operator, adding the left and right subtrees.
      -2: Subtraction operator, subtracting the right subtree from the left subtree.
      -3: Division operator, dividing the left subtree by the right subtree.
          If the result is a decimal, it should be rounded towards zero.
      -4: Multiplication operator, multiplying the left and right subtrees.
 
    You can assume the tree will always be a valid expression tree. Each
    operator also works as a grouping symbol, meaning the bottom of the tree is
    always evaluated first, regardless of the operator.
     

  Time complexity O(n) - count of nodes
  Space complexity O(h) - height of tree
"""
import pytest


class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

def evaluateExpressionTree(root):
    if root.value>0:
        return root.value
    elif root.value==-1:
        return evaluateExpressionTree(root.left) + evaluateExpressionTree(root.right)
    elif root.value==-2:
        return evaluateExpressionTree(root.left) - evaluateExpressionTree(root.right)
    elif root.value==-3:
        return int(evaluateExpressionTree(root.left)/evaluateExpressionTree(root.right))
    elif root.value==-4:
        return evaluateExpressionTree(root.left)*evaluateExpressionTree(root.right)

# case [root, expected]
cases = [
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 5],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -2}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, -1],
    [{'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': -2}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 1],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -3}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 0],
    [{'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': -3}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 1],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -4}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, 6],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'right': '5', 'value': -2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '1'}, 1],
    [{'nodes': [{'id': '1', 'left': '10', 'right': '3', 'value': -3}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '3', 'left': '4', 'right': '6', 'value': -2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, -5],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '3', 'value': -3}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '3', 'left': '4', 'right': '6', 'value': -2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, -4],
    [{'nodes': [{'id': '1', 'left': '9', 'right': '3', 'value': -3}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '3', 'left': '6', 'right': '4', 'value': -2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, 4],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -2}, {'id': '2', 'left': '4', 'right': '5', 'value': -1}, {'id': '3', 'left': '6', 'right': '7', 'value': -3}, {'id': '4', 'left': None, 'right': None, 'value': 7}, {'id': '5', 'left': None, 'right': None, 'value': 10}, {'id': '6', 'left': None, 'right': None, 'value': 12}, {'id': '7', 'left': '8', 'right': '9', 'value': -4}, {'id': '8', 'left': None, 'right': None, 'value': 1}, {'id': '9', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, 14],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -1}, {'id': '2', 'left': '4', 'right': '5', 'value': -2}, {'id': '3', 'left': '6', 'right': '7', 'value': -4}, {'id': '4', 'left': None, 'right': None, 'value': 7}, {'id': '5', 'left': None, 'right': None, 'value': 10}, {'id': '6', 'left': None, 'right': None, 'value': 12}, {'id': '7', 'left': '8', 'right': '9', 'value': -3}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, 21],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -1}, {'id': '2', 'left': '4', 'right': '5', 'value': -1}, {'id': '3', 'left': '6', 'right': '7', 'value': -1}, {'id': '4', 'left': None, 'right': None, 'value': 7}, {'id': '5', 'left': None, 'right': None, 'value': 10}, {'id': '6', 'left': None, 'right': None, 'value': 12}, {'id': '7', 'left': '8', 'right': '9', 'value': -1}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, 41],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -2}, {'id': '2', 'left': '4', 'right': '5', 'value': -2}, {'id': '3', 'left': '6', 'right': '7', 'value': -2}, {'id': '4', 'left': None, 'right': None, 'value': 7}, {'id': '5', 'left': None, 'right': None, 'value': 10}, {'id': '6', 'left': None, 'right': None, 'value': 12}, {'id': '7', 'left': '8', 'right': '9', 'value': -2}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, -11],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -3}, {'id': '2', 'left': '4', 'right': '5', 'value': -3}, {'id': '3', 'left': '6', 'right': '7', 'value': -3}, {'id': '4', 'left': None, 'right': None, 'value': 100}, {'id': '5', 'left': None, 'right': None, 'value': 10}, {'id': '6', 'left': None, 'right': None, 'value': 4}, {'id': '7', 'left': '8', 'right': '9', 'value': -3}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, 5],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': -4}, {'id': '2', 'left': '4', 'right': '5', 'value': -4}, {'id': '3', 'left': '6', 'right': '7', 'value': -4}, {'id': '4', 'left': None, 'right': None, 'value': 2}, {'id': '5', 'left': None, 'right': None, 'value': 1}, {'id': '6', 'left': None, 'right': None, 'value': 7}, {'id': '7', 'left': '8', 'right': '9', 'value': -4}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, 224],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '9', 'value': -4}, {'id': '2', 'left': '4', 'right': '3', 'value': -1}, {'id': '3', 'left': None, 'right': None, 'value': 8}, {'id': '4', 'left': '5', 'right' : '6', 'value': -1}, {'id': '5', 'left': None, 'right': None, 'value': 7}, {'id': '6', 'left': '7', 'right': '8', 'value': -2}, {'id': '7', 'left': None, 'right': None, 'value': 22}, {'id': '8', 'left': None, 'right': None, 'value': 5}, {'id': '9', 'left': '10', 'right': '11', 'value': -3}, {'id': '10', 'left': None, 'right': None, 'value': 100}, {'id': '11', 'left': '12', 'right': '13', 'value': -2}, {'id': '12', 'left': None, 'right': None, 'value': 42}, {'id': '13', 'left': '14', 'right': '15', 'value': -3}, {'id': '14', 'left': '16', 'right': '17', 'value': -4}, {'id': '15', 'left': None, 'right': None, 'value': 2}, {'id': '16', 'left': None, 'right': None, 'value': 3}, {'id': '17', 'left': None, 'right': None, 'value': 9}], 'root': '1'}, 96]
]

@pytest.mark.parametrize("root, expected", cases)
def test_evaluateExpressionTree(root, expected):
    nodes = {}
    for node_json in root['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in root['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None

    assert evaluateExpressionTree(nodes[root['root']])==expected

