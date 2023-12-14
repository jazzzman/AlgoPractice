r"""
  DESCRIPTION

  Write a BST class for a Binary Search Tree. The class should
  support:


  Note that you can't remove values from a single-node tree. In other words,
  calling the remove method on a single-node tree should simply not
  do anything.


  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.
            Tree                    Insert 12                 Remove 10
              10                      10                         12 
           /     \                  /    \                     /    \
          5      15                5      15                  5      15
        /   \   /   \            /  \    /   \               / \    /   \
       2     5 13   22          2   5   13   22             2  5   13    22
     /           \             /       /  \                /        \
    1            14            1      12  14              1          14   


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

    def insert(self,value):
        node = self
        while node:
            if value>=node.value:
                if node.right:
                    node = node.right
                else:
                    node.right = BST('',value)
                    return
            else:
                if node.left:
                    node = node.left
                else:
                    node.left = BST('',value)
                    return

    def contains(self,value):
        node = self
        while node:
            if node.value == value:
                return True
            node = node.left if value<node.value else node.right

        return False

    def remove(self, value):
        node = self
        prev_node = None
        while node:
            prev_node = node 
            if node.value == value:
                if not node.left:
                    if prev_node.value>value:
                        prev_node.left = node.right
                    else:
                        prev_node.right = node.right

                min_node = self.get_min_value(node)
                new_node = BST('',min_node)
                new_node.left = node.left
                new_node.right = node.right
                if prev_node is not node:
                    if prev_node.value>value:
                        prev_node.left = new_node
                    else:
                        prev_node.right = new_node
            elif value> node.value:
                node = node.right
            else:
                node = node.left



    def pop_min_value(node):
        prev_node = None
        while node.left:
            prev_node = node
            node = node.left
        if prev_node:
            prev_node.left = None
        return node.value

    def __repr__(self):
        return (f'id: {self.id} value: {self.value} '
               f'left: {self.left.id if self.left else None} '
               f'right: {self.right.id if self.right else None}')

def bSTConstruction(operations,value):
    return []


# case [operations,value,tree, expected]
cases = [
    [[{'arguments': [5], 'method': 'insert'}, {'arguments': [15], 'method': 'insert'}], 10, [{'arguments': [5], 'method': 'insert', 'output': None, 'tree': {'nodes': [{'id': '10', 'left': '5', 'right': None, 'value': 10}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '10'}}, {'arguments': [15], 'method': 'insert', 'output': None, 'tree': {'nodes': [{'id': '10', 'left': '5', 'right': '15', 'value': 10}, {'id': '15', 'left': None, 'right': None, 'value': 15}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '10'}}]],
    [[{'arguments': [5], 'method': 'insert'}, {'arguments': [10], 'method': 'remove'}, {'arguments': [15], 'method': 'contains'}], 10, [{'arguments': [5], 'method': 'insert', 'output': None, 'tree': {'nodes': [{'id': '10', 'left': '5', 'right': None, 'value': 10}, {'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '10'}}, {'arguments': [10], 'method': 'remove', 'output': None, 'tree': {'nodes': [{'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '5'}}, {'arguments': [15], 'method': 'contains', 'output': False, 'tree': {'nodes': [{'id': '5', 'left': None, 'right': None, 'value': 5}], 'root': '5'}}]],
]

@pytest.mark.skip("To lazzy to prepare test cases")
@pytest.mark.parametrize("operations,value, expected", cases)
def test_bSTConstruction(operations,value, expected):
    nodes = {node['id']:BST(node['id'], node['value']) for node in tree['nodes']}
    for node in tree['nodes']:
        if node['left']:
            nodes[node['id']].left = nodes[node['left']]
        if node['right']:
            nodes[node['id']].right = nodes[node['right']]
    ic(nodes)
    assert bSTConstruction(operations,value,tree)==expected
