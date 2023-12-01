"""
  DESCRIPTION

    Write a function that takes in two Binary Trees, merges them, and returns
    the resulting tree. If two nodes overlap during the merge, the value of the
    merged node should be the sum of the overlapping nodes' values.
  
    Note that your solution can either mutate the input trees or return a new
    tree.
 
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
    def __init__(self, value):
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

def mergeBinaryTree(tree1, tree2):
    bfs(tree1, tree2)
    ttd =  treeToDict(tree1)
    ic(ttd)
    return ttd

# implementation through breadth first approach
def bfs(node1, node2):
    queue = []
    queue.append([node1,node2])
    while queue:
        node1, node2 = queue.pop(0)
        if node1 and node2:
            node1.value += node2.value
            if node1.left and node2.left:
                queue.append([node1.left, node2.left])
            if node1.right and node2.right:
                queue.append([node1.right, node2.right])

            if node1.left is None and node2.left is not None:
                node1.left = node2.left
                node2.left = None
            if node1.right is None and node2.right is not None:
                node1.right = node2.right
                node2.right =None

# implementation using recurssion
def dfs(node1,node2):
    if node1 and node2:
        node1.value += node2.value
        node1.left = dfs(node1.left, node2.left)
        node1.right = dfs(node1.right, node2.right)
        return node1
    elif node1 and node2 is None:
        return node1
    elif node2 and node1 is None:
        return node2
    else:
        return None



# case [tree1, tree2, expected]
cases = [
    [{'nodes': [{'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '7'}, {'nodes': [{'id': '2', 'left': '3', 'right': '6', 'value': 2}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '2'}, {'nodes': [{'id': '9', 'left': '3', 'right': '6', 'value': 9}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '9'}],
    [{'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '3', 'left': '5', 'right': None, 'value': 3}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, {'nodes': [{'id': '2', 'left': '3', 'right': '6', 'value': 2}, {'id': '3', 'left': None, 'right': '4', 'value': 3}, {'id': '6', 'left': None, 'right': '7', 'value': 6}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '2'}, {'nodes': [{'id': '3', 'left': '6', 'right': '8', 'value': 3}, {'id': '8', 'left': None, 'right': '7', 'value': 8}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '6', 'left': '5', 'right': '4', 'value': 6}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '3'}],
    [{'nodes': [{'id': '1', 'left': '3', 'right': '2', 'value': 1}, {'id': '3', 'left': '7', 'right': '4', 'value': 3}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '5', 'right': '9', 'value': 1}, {'id': '5', 'left': '2', 'right': None, 'value': 5}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '9', 'left': '7', 'right': '6', 'value': 9}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '1'}, {'nodes': [{'id': '2', 'left': '8', 'right': '11', 'value': 2}, {'id': '11', 'left': '7', 'right': '6', 'value': 11}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}, {'id': '8', 'left': '9', 'right': '4', 'value': 8}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '9', 'left': None, 'right': None, 'value': 9}], 'root': '2'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, {'nodes': [{'id': '4', 'left': '5', 'right': '6', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '4'}, {'nodes': [{'id': '5', 'left': '7', 'right': '9', 'value': 5}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '5'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, {'nodes': [{'id': '4', 'left': '5', 'right': '6', 'value': 4}, {'id': '5', 'left': '1', 'right': '8', 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '1', 'left': None, 'right': None, 'value': 1}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '4'}, {'nodes': [{'id': '5', 'left': '7', 'right': '9', 'value': 5}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '7', 'left': '1', 'right': '8', 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '5'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': None, 'right': None, 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, {'nodes': [{'id': '4', 'left': '5', 'right': '6', 'value': 4}, {'id': '5', 'left': '1', 'right': '8', 'value': 5}, {'id': '6', 'left': '10', 'right': '15', 'value': 6}, {'id': '1', 'left': None, 'right': None, 'value': 1} , {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '15', 'left': None, 'right': None, 'value': 15}], 'root': '4'}, {'nodes': [{'id': '5' , 'left': '7', 'right': '9', 'value': 5}, {'id': '9', 'left': '10', 'right': '15', 'value': 9}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '7', 'left': '1', 'right': '8', 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '5'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '5', 'right': '8', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '1'}, {'nodes': [{'id': '4', 'left': '5', 'right': '6', 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5} , {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '4'}, {'nodes': [{'id': '5', 'left': '7', 'right': '9', 'value': 5}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '7', 'left': '5-2', 'right': '8', 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '5-2', 'left': None, 'right': None, 'value': 5}], 'root': '5'}],
    [{'nodes': [{'id': '2', 'left': '4', 'right': '1', 'value': 2}, {'id': '4', 'left': '6', 'right': None, 'value': 4}, {'id': '1', 'left': None, 'right': None, 'value': 1}, {'id': '6', 'left': None, 'right' : None, 'value': 6}], 'root': '2'}, {'nodes': [{'id': '3', 'left': '1', 'right': '6', 'value': 3}, {'id': '1', 'left': None, 'right': '9', 'value': 1}, {'id': '6', 'left': None, 'right': '8', 'value': 6}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '3'}, {'nodes': [{'id': '5', 'left': '5-2', 'right': '7', 'value': 5}, {'id': '7', 'left': None, 'right': '8', 'value': 7}, {'id': '8', 'left': None, 'right': None, 'value': 8}, {'id': '5-2', 'left': '6', 'right': '9', 'value': 5}, {'id': '9', 'left': None, 'right': None, 'value': 9}, {'id': '6', 'left': None, 'right': None, 'value': 6}], 'root': '5'}],
    [{'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}, {'nodes': [{'id': '1', 'left': '2', 'right': '3', 'value': 1}, {'id': '2', 'left': '4', 'right': '5', 'value': 2}, {'id': '3', 'left': '6', 'right': '7', 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '5', 'left': None, 'right': None, 'value': 5}, {'id': '6', 'left': None, 'right': None, 'value': 6}, {'id': '7', 'left': None, 'right': None, 'value': 7}], 'root': '1'}, {'nodes': [{'id': '2', 'left': '4', 'right': '6', 'value': 2}, {'id': '6', 'left': '12', 'right': '14', 'value': 6}, {'id': '14', 'left': None, 'right': None, 'value': 14}, {'id': '12', 'left': None, 'right': None, 'value': 12}, {'id': '4', 'left': '8', 'right': '10', 'value': 4}, {'id': '10', 'left': None, 'right': None, 'value': 10}, {'id': '8', 'left': None, 'right': None, 'value': 8}], 'root': '2'}],
    [{'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, {'nodes': [{'id': '1', 'left': None, 'right': None, 'value': 1}], 'root': '1'}, {'nodes': [{'id': '2', 'left': None, 'right': None, 'value': 2}], 'root': '2'}],
    [{'nodes': [{'id': '1', 'left': '3', 'right': None, 'value': 1}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, {'nodes': [{'id': '1', 'left': None, 'right': '4', 'value': 1}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, {'nodes': [{'id': '2', 'left': '3', 'right': '4', 'value': 2}, {'id': '4', 'left': None, 'right': None, 'value': 4}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '2'}],
    [{'nodes': [{'id': '1', 'left': '4', 'right': None, 'value': 1}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '1'}, {'nodes': [{'id': '1', 'left': None, 'right': '3', 'value': 1}, {'id': '3', 'left': None, 'right': None, 'value': 3}], 'root': '1'}, {'nodes': [{'id': '2', 'left': '4', 'right': '3', 'value': 2}, {'id': '3', 'left': None, 'right': None, 'value': 3}, {'id': '4', 'left': None, 'right': None, 'value': 4}], 'root': '2'}]
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

@pytest.mark.parametrize("tree1, tree2, expected", cases)
def test_mergeBinaryTree(tree1, tree2, expected):
    nodes1 = {}
    for node_json in tree1['nodes']:
        nodes1[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in tree1['nodes']:
        nodes1[node_json['id']].left = nodes1[node_json['left']] if node_json['left'] else None
        nodes1[node_json['id']].right = nodes1[node_json['right']] if node_json['right'] else None

    nodes2 = {}
    for node_json in tree2['nodes']:
        nodes2[node_json['id']]=BinaryTree(node_json['value'])
    for node_json in tree2['nodes']:
        nodes2[node_json['id']].left = nodes2[node_json['left']] if node_json['left'] else None
        nodes2[node_json['id']].right = nodes2[node_json['right']] if node_json['right'] else None

    ic(expected)

    assert mergeBinaryTree(nodes1[tree1['root']], nodes2[tree2['root']])==expected

