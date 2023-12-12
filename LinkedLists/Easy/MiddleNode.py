"""
  DESCRIPTION

    You're given a Linked List with at least one node. Write a function     
    that returns the middle node of the Linked List. If there are two middle
    nodes (i.e. an even length list), your function should return the second
    of these nodes.


    Each LinkedList node has an integer value as well as
    a next node pointing to the next node in the list or to
    None / null if it's the tail of the list.



  Time complexity O(###)
  Space complexity O(###)
"""
import pytest

from icecream import ic


class LinkedList:
    def __init__(self,id, value):
        self.id = id
        self.value = value
        self.next = None

    def __repr__(self):
        return f'value: {self.value}'


# more neet way
def middleNode(linkedList):
    fastNode = linkedList
    slowNode = linkedList
    while fastNode and fastNode.next:
        slowNode = slowNode.next
        fastNode = fastNode.next.next

    return slowNode

def middleNode_ver2(linkedList):
    node_counts = 1
    node = linkedList
    while node.next:
        node_counts += 1
        node = node.next

    node = linkedList
    for i in range(node_counts//2):
        node = node.next
    return node


# case [linkedList, expected]
cases = [
    [{'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}, {'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}],
    [{'head': '1', 
      'nodes': [
          {'id': '1', 'next': '2', 'value': 1},
          {'id': '2', 'next': '3', 'value': 2},
          {'id': '3', 'next': None, 'value': 3}]}, 
     {'head': '2', 
      'nodes': [
          {'id': '2', 'next': '3', 'value': 2},
          {'id': '3', 'next': None, 'value': 3}]}],
    [{'head': '5', 'nodes': [{'id': '5', 'next': '7', 'value': 5}, {'id': '7', 'next': '9', 'value': 7}, {'id': '9', 'next': None, 'value': 9}]}, {'head': '7', 'nodes': [{'id': '7', 'next': '9', 'value': 7}, {'id': '9', 'next': None, 'value': 9}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': None, 'value': 4}]}, {'head': '3', 'nodes': [{'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': None, 'value': 4}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}, {'head': '5', 'nodes': [{'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': None, 'value': 10}]}, {'head': '6', 'nodes': [{'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': None, 'value': 10}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '3', 'value': 1}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '9', 'value': 5}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': None, 'value': 10}]}, {'head': '5', 'nodes': [{'id': '5', 'next': '9', 'value': 5}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': None, 'value': 10}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '1-2', 'value': 1}, {'id': '1-2', 'next': '1-3', 'value': 1}, {'id': '1-3', 'next': '3', 'value': 1}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '5-2', 'value': 5}, {'id': '5-2', 'next': '5-3', 'value': 5}, {'id': '5-3', 'next': '5-4', 'value': 5}, {'id': '5-4', 'next': '10', 'value': 5}, {'id': '10', 'next': None, 'value': 10}]}, {'head': '5', 'nodes': [{'id': '5', 'next': '5-2', 'value': 5}, {'id': '5-2', 'next': '5-3', 'value': 5}, {'id': '5-3', 'next': '5-4', 'value': 5}, {'id': '5-4', 'next': '10', 'value': 5}, {'id': '10', 'next': None, 'value': 10}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '1-2', 'value': 2}, {'id': '1-2', 'next': '4', 'value': 1}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '5-2', 'value': 5}, {'id': '5-2', 'next': '7', 'value': 5}, {'id': '7', 'next': '10', 'value': 7}, {'id': '10', 'next': None, 'value': 10}]}, {'head': '5', 'nodes': [{'id': '5', 'next': '5-2', 'value': 5}, {'id': '5-2', 'next': '7', 'value': 5}, {'id': '7', 'next': '10', 'value': 7}, {'id': '10', 'next': None, 'value': 10}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '1-2', 'value': 1}, {'id': '1-2', 'next': '1-3', 'value': 1}, {'id': '1-3', 'next': '1-4', 'value': 1}, {'id': '1-4', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '5-2', 'value': 5}, {'id': '5-2', 'next': '7', 'value': 5}, {'id': '7', 'next': '10', 'value': 7}, {'id': '10', 'next': None, 'value': 10}]}, {'head': '3', 'nodes': [{'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '5-2', 'value': 5}, {'id': '5-2', 'next': '7', 'value': 5}, {'id': '7', 'next': '10', 'value': 7}, {'id': '10', 'next': None, 'value': 10}]}]
]

@pytest.mark.parametrize("linkedList, expected", cases)
def test_middleNode(linkedList, expected):
    nodes = {node['id']:LinkedList(node['id'],node['value']) for node in linkedList['nodes']}
    for node in linkedList['nodes']:
        nodes[node['id']].next = nodes.get(node['next'],None)

    candidate = []
    node = middleNode(nodes[linkedList['head']])
    ic(node)
    while node:
        candidate.append({
            'id': node.id,
            'next': node.next.id if node.next else None,
            'value': node.value
            })
        node = node.next
    ic(candidate)
    ic(expected['nodes'])
    assert candidate==expected['nodes']
