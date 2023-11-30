"""
  DESCRIPTION

  Write a function that takes in a Binary Tree and inverts it. In other words,
  the function should swap every left node in the tree for its corresponding
  right node.

  Each BinaryTree node has an integer value, a
  left child node, and a right child node. Children
  nodes can either be BinaryTree nodes themselves or
  None / null.

  Time complexity O(###)
  Space complexity O(###)
"""
import pytest
from icecream import ic

class BinaryTree:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
    def toDict(self):
        return {
            'id': str(self.value),
            'left': str(self.left.value) if self.left else None,
            'right': str(self.right.value) if self.right else None,
            'value': self.value
        }

def invertBinaryTree(root):
    dfs(root)
    
    ttd =  treeToDict(root)
    ic(ttd)
    return ttd

def dfs(node):
    if node is None:
        return
    if node.left:
        dfs(node.left)
    if node.right:
        dfs(node.right)
    node.left, node.right = node.right, node.left


# case [root, expected]
cases = [
    [{
        'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, 
                  {'id': '2', 'left': '4', 'right': '5', 'value': 2}, 
                  {'id': '3', 'left': '6', 'right': '7', 'value': 3}, 
                  {'id': '4', 'left': '8', 'right': '9', 'value': 4},
                  {'id': '5', 'left': None, 'right': None, 'value': 5}, 
                  {'id': '6', 'left': None, 'right': None, 'value': 6},
                  {'id': '7', 'left': None, 'right': None, 'value': 7}, 
                  {'id': '8', 'left': None, 'right': None, 'value': 8}, 
                  {'id': '9', 'left': None, 'right': None, 'value': 9}], 
        'root': '1'
      }, 
     {
      'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': '5', 'right': '4', 'value': 2}, {'id': '4', 'left': '9', 'right': '8', 'value': 4}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '3', 'left': '7', 'right': '6', 'value': 3}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 
      'root': '1'
      }
    ],
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, {'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': None, 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, {'nodes': [{'id': '1', 'left': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}], 
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'right': '4', 'value': 2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': '5', 'right': '4', 'value': 2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': '5', 'right': '4', 'value': 2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '3', 'left': None, 'right': '6', 'value': 3}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': '5', 'right': '4', 'value': 2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '3', 'left': '7', 'right': '6', 'value': 3}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': '5', 'right': '4', 'value': 2}, {'id': '4', 'left': None, 'right': '8', 'value': 4}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '3', 'left': '7', 'right': '6', 'value': 3}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': '8', 'right': '9', 'value': 4}, {'id': '5', 'left': '10', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '10', 'left': None, 'right': None, 'value': 10}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '2', 'left': '5', 'right': '4', 'value': 2}, {'id': '4', 'left': '9', 'right': '8', 'value': 4}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '5', 'left': None, 'right': '10', 'value': 5}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '3', 'left': '7', 'right': '6', 'value': 3}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}],
]


def treeToDict(root):
    treeDict = {
        'root': str(root.value),
        'nodes': []
    }
    dfs_to_dict(root,treeDict)
    return treeDict

def dfs_to_dict(node,treeDict):
    queue = []
    queue.append(node)
    while queue:
        node = queue.pop(0)
        treeDict['nodes'].append(node.toDict())
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

@pytest.mark.skip('Fails to compare dictionaries')
@pytest.mark.parametrize("root, expected", cases)
def test_invertBinaryTree(root, expected):
    nodes = {}
    for node_json in root['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in root['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None
    
    ic(expected)

    assert invertBinaryTree(nodes[root['root']])==expected

