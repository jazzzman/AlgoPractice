"""
  DESCRIPTION

  Write a function that takes in a Binary Tree (where nodes have an additional
  pointer to their parent node) as well as a node contained in that tree and
  returns the given node's successor.

  A node's successor is the next node to be visited (immediately after the given
  node) when traversing its tree using the in-order tree-traversal technique. A
  node has no successor if it's the last node to be visited in the in-order
  traversal.

  If a node has no successor, your function should return None /
  null.

  Each BinaryTree node has an integer value, a
  parent node, a left child node, and a
  right child node. Children nodes can either be
  BinaryTree nodes themselves or None /
  null.


  Time complexity O(###)
  Space complexity O(###)
"""
import pytest




# Time Complexity O(n)
# Space Complexity O(n) 
def findSuccessor_v2(tree, node):
    stack = []
    bfs(tree,stack)
    idx = stack.index(node)
    if idx+1>=len(stack):
        return None

    successor = stack[idx+1]

    return {'nodeId': str(successor.value)}

def bfs(node,stack):
    if node:
        bfs(node.left, stack)
        stack.append(node)
        bfs(node.right, stack)

# case [tree, node, expected]
cases = [
    ['5', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'parent': '1', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'parent': '1', 'right': None, 'value': 3}, {'id': '4', 'left': '6', 'parent': '2', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'parent': '2', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'parent': '4', 'right': None, 'value': 6}], 'root': '1'}, {'nodeId': '1'}],
    ['5', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'parent': '1', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'parent': '1', 'right': None, 'value': 3}, {'id': '4', 'left': None, 'parent': '2', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'parent': '2', 'right': '7', 'value': 5}, {'id': '6', 'left': None, 'parent': '5', 'right': None, 'value': 6}, {'id': '7', 'left': '8', 'parent': '5', 'right': None, 'value': 7}, {'id': '8', 'left': None, 'parent': '7', 'right': None, 'value': 8}], 'root': '1'}, {'nodeId': '8'}],
    ['6', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'parent': '1', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'parent': '1', 'right': '7', 'value': 3}, {'id': '4', 'left': None, 'parent': '2', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'parent': '2', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'parent': '3', 'right': None, 'value': 6}, {'id': '7', 'left': None, 'parent': '3', 'right': None, 'value': 7}], 'root': '1'}, {'nodeId': '3'}],
    ['2', {'nodes': [{'id': '1', 'left': None, 'parent': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'parent': '1', 'right': None, 'value': 2}], 'root': '1'}, None],
    ['1', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'parent': '1', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'parent': '1', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'parent': '3', 'right': None, 'value': 4}, {'id': '5', 'left': '6', 'parent': '4', 'right': None, 'value': 5}, {'id': '6', 'left': '7', 'parent': '5', 'right': None, 'value': 6}, {'id': '7', 'left': None, 'parent': '6', 'right': None, 'value': 7}], 'root': '1'}, {'nodeId': '7'}],
    ['3', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': None, 'value': 1}, {'id': '2', 'left': '3', 'parent': '1', 'right': None, 'value': 2}, {'id': '3', 'left': '4', 'parent': '2', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'parent': '3', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'parent': '4', 'right': None, 'value': 5}], 'root': '1'}, {'nodeId': '2'}],
    ['2', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': None, 'value': 1}, {'id': '2', 'left': '3', 'parent': '1', 'right': '6', 'value': 2}, {'id': '3', 'left': '4', 'parent': '2', 'right': None, 'value': 3}, {'id': '4', 'left': '5', 'parent': '3', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'parent': '4', 'right': None, 'value': 5}, {'id': '6', 'left': '7', 'parent': '2', 'right': '8', 'value': 6}, {'id': '7', 'left': None, 'parent': '6', 'right': None, 'value': 7}, {'id': '8', 'left': None, 'parent': '6', 'right': None, 'value': 8}], 'root': '1'}, {'nodeId': '7'}], ['1', {'nodes': [{'id': '1', 'left': None, 'parent': None, 'right': None, 'value': 1}], 'root': '1'}, None],
    ['1', {'nodes': [{'id': '1', 'left': None, 'parent': None, 'right': '2', 'value': 1}, {'id': '2', 'left': None, 'parent': '1', 'right': None, 'value': 2}], 'root': '1'}, {'nodeId': '2'}],
    ['1', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': '5', 'value': 1}, {'id': '2', 'left': None, 'parent': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'parent': '2', 'right': '4', 'value': 3}, {'id': '4', 'left': None, 'parent': '3', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'parent': '1', 'right': '6', 'value': 5}, {'id': '6', 'left': '7', 'parent': '5', 'right': '8', 'value': 6}, {'id': '7', 'left': None, 'parent': '6', 'right': None, 'value': 7}, {'id': '8', 'left': None, 'parent': '6', 'right': None, 'value': 8}], 'root': '1'}, {'nodeId': '5'}],
    ['1', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': '5', 'value': 1}, {'id': '2', 'left': None, 'parent': '1', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'parent': '2', 'right': '4', 'value': 3}, {'id': '4', 'left': None, 'parent': '3', 'right': None, 'value': 4}, {'id': '5', 'left': '9', 'parent': '1', 'right': '6', 'value': 5}, {'id': '6', 'left': '7', 'parent': '5', 'right': '8', 'value': 6}, {'id': '7', 'left': None, 'parent': '6', 'right': None, 'value': 7}, {'id': '8', 'left': None, 'parent': '6', 'right': None, 'value': 8}, {'id': '9', 'left': '10', 'parent': '5', 'right': None, 'value': 9}, {'id': '10', 'left': '11', 'parent': '9', 'right': None, 'value': 10}, {'id': '11', 'left': None, 'parent': '10', 'right': None, 'value': 11}], 'root': '1'}, {'nodeId': '11'}],
    ['1', {'nodes': [{'id': '1', 'left': '2', 'parent': None, 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'parent': '1', 'right': '5', 'value': 2}, {'id': '3', 'left': None, 'parent': '1', 'right': '7', 'value': 3}, {'id': '4', 'left': '6', 'parent': '2', 'right': None, 'value': 4}, {'id': '5', 'left': None, 'parent': '2', 'right': None, 'value': 5}, {'id': '6', 'left': None, 'parent': '4', 'right': None, 'value': 6}, {'id': '7', 'left': None, 'parent': '3', 'right': '8', 'value': 7}, {'id': '8', 'left': None, 'parent': '7', 'right': None, 'value': 8}], 'root': '1'}, {'nodeId': '3'}]
]

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

    def __eq__(self,other):
        return self.value == other.value


@pytest.mark.parametrize("node, root, expected", cases)
def test_findSuccessor(node, root, expected):
    global stack
    stack = []
    nodes = {}
    for node_json in root['nodes']:
        nodes[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in root['nodes']:
        nodes[node_json['id']].left = nodes[node_json['left']] if node_json['left'] else None
        nodes[node_json['id']].right = nodes[node_json['right']] if node_json['right'] else None
        nodes[node_json['id']].parent = nodes[node_json['parent']] if node_json['parent'] else None

    node = [n for ids,n in nodes.items() if n.value == int(node)][0]

    assert findSuccessor(nodes[root['root']],node)==expected
