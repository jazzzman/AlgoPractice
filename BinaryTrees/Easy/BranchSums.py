"""
  DESCRIPTION

  Write a function that takes in a Binary Tree and returns a list of its branch
  sums ordered from leftmost branch sum to rightmost branch sum.

  A branch sum is the sum of all values in a Binary Tree branch. A Binary Tree
  branch is a path of nodes in a tree that starts at the root node and ends at
  any leaf node.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.

  Time complexity O(###)
  Space complexity O(###)
"""
import pytest

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def branchSum(root):
    output = []
    dfs(root,0,output)
    return output

def dfs(node,branchSum,output):
    if node.left is None and node.right is None:
        output.append(branchSum+node.value)
    else:
        branchSum += node.value
        if node.left:
            dfs(node.left,branchSum,output)
        if node.right:
            dfs(node.right,branchSum,output)

# case [root, expected]
cases = [
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1},
                {'id': '2', 'left': '4', 'right': '5', 'value': 2}, 
                {'id': '3', 'left': '6', 'right': '7', 'value': 3}, 
                {'id': '4', 'left': '8', 'right': '9', 'value': 4}, 
                {'id': '5', 'left': '10', 'right': None, 'value': 5}, 
                {'id': '6', 'left': None, 'right': None, 'value': 6}, 
                {'id': '7', 'left': None, 'right': None, 'value': 7}, 
                {'id': '8', 'left': None, 'right': None, 'value': 8}, 
                {'id': '9', 'left': None, 'right': None, 'value': 9}, 
                {'id': '10', 'left': None, 'right': None, 'value': 10}], 
      'root': '1'}, 
     [15, 16, 18, 10, 11]],
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, [1]],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, [3]],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, [3, 4]],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '1'}, [7, 8, 4]],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': '10', 'right': '1-2', 'value': 5}, {'id': '6', 'left': '1-3', 'right': '1-4', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '1-2', 'left': None, 'right': None, 'value': 1}, {'id': '1-3', 'left': None, 'right': None, 'value': 1}, {'id': '1-4', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, [15, 16, 18, 9, 11, 11, 11]],
    [{'nodes': [{'id': '0', 'left': '1', 'right': None, 'value': 0}, {'id': '1', 'left': '10', 'right': None, 'value': 1}, {'id': '10', 'left': '100', 'right': None, 'value': 10}, {'id': '100', 'left': None, 'right': None, 'value': 100}], 'root': '0'}, [111]],
    [{'nodes': [{'id': '0', 'left': None, 'right': '1', 'value': 0}, {'id': '1', 'left': None, 'right': '10', 'value': 1}, {'id': '10', 'left': None, 'right': '100', 'value': 10}, {'id': '100', 'left': None, 'right': None, 'value': 100}], 'root': '0'}, [111]],
    [{'nodes': [{'id': '0', 'left': '9', 'right': '1', 'value': 0}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '1', 'left': '15', 'right': '10', 'value': 1}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '10', 'left': '100', 'right': '200', 'value': 10}, {'id': '100', 'left': None, 'right': None, 'value': 100}, {'id': '200', 'left': None, 'right': None, 'value': 200}], 'root': '0'}, [9, 16, 111, 211]]
]

@pytest.mark.parametrize("root, expected", cases)
def test_branchSum(root, expected):
    nodes = {}
    for node_json in root['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in root['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None

    assert branchSum(nodes[root['root']])==expected

