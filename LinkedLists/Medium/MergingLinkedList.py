"""
  DESCRIPTION

    You're given two Linked Lists of potentially unequal length. These Linked
    Lists potentially merge at a shared intersection node. Write a function  
    that returns the intersection node or returns None /
    null if there is no intersection.


    Each LinkedList node has an integer value as well as
    a next node pointing to the next node in the list or to
    None / null if it's the tail of the list.


    Note: Your function should return an existing node. It should not modify 
    either Linked List, and it should not create any new Linked Lists.       



  Time complexity O(n+m)
  Space complexity O(1)
"""
import pytest
from icecream import ic


class LinkedList:
    def __init__(self, id, value):
        self.id = id
        self.next = None
        self.value = value

    def __eq__(self, other):
        return self.value == other.value

# prettier way to do the same
def mergingLinkedList_v2(linkedListOne, linkedListTwo):
    currentOne, currentTwo = linkedListOne, linkedListTwo

    while currentOne!=currentTwo:
        currentOne = currentOne.next if currentOne else linkedListTwo
        currentTwo = currentTwo.next if currentTwo else linkedListOne

    return currentOne

def mergingLinkedList(linkedListOne, linkedListTwo):
    nodeOne = linkedListOne
    nodeTwo = linkedListTwo

    nodeOne, nodeTwo = reachEndAndSwap(nodeOne, nodeTwo, linkedListOne, linkedListTwo)
    nodeOne, nodeTwo = reachEndAndSwap(nodeOne, nodeTwo, linkedListOne, linkedListTwo)

    while nodeOne and nodeTwo:
        if nodeOne.value == nodeTwo.value:
            return nodeOne
        nodeOne = nodeOne.next
        nodeTwo = nodeTwo.next

    return None

def reachEndAndSwap(nodeOne, nodeTwo, linkedListOne, linkedListTwo):
    while nodeOne and nodeTwo:
        nodeOne = nodeOne.next
        nodeTwo = nodeTwo.next

    nodeOne = nodeOne if nodeOne else linkedListTwo
    nodeTwo = nodeTwo if nodeTwo else linkedListOne

    return nodeOne, nodeTwo



# case [linkedListOne, linkedListTwo, expected]
cases = [
    [{'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}, {'head': '2', 'nodes': [{'id': '2', 'next': None, 'value': 2}]}, {'head': None, 'nodes': []}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}, {'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}, {'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': None, 'value': 2}]}, {'head': '4', 'nodes': [{'id': '4', 'next': '2', 'value': 4}, {'id': '2', 'next': None, 'value': 2}] }, {'head': '2', 'nodes': [{'id': '2', 'next': None, 'value': 2}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': None, 'value': 3}]}, {'head': '4', 'nodes': [{'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '3', 'value': 5}, {'id': '3', 'next': None, 'value': 3}]}, {'head': '3', 'nodes': [{'id': '3', 'next': None, 'value': 3}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': None, 'value': 4}]}, {'head': '5', 'nodes': [{'id': '5', 'next': '3', 'value': 5}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': None, 'value': 4}]}, {'head': '3', 'nodes': [{'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': None, 'value': 4}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}, {'head': '2', 'nodes': [{'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '1', 'value': 4}, {'id': '1', 'next': None, 'value': 1}]}, {'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}],
    [{'head': '5', 'nodes': [{'id': '5', 'next': '12', 'value': 5}, {'id': '12', 'next': '14', 'value': 12}, {'id': '14', 'next': '2', 'value': 14}, {'id': '2', 'next': '13', 'value': 2}, {'id': '13', 'next': '21', 'value': 13}, {'id': '21', 'next': '33', 'value': 21}, {'id': '33', 'next': '9', 'value': 33}, {'id': '9', 'next': None, 'value': 9}]}, {'head': '10', 'nodes': [{'id': '10', 'next': '3', 'value': 10}, {'id': '3', 'next': '48', 'value': 3}, {'id': '48', 'next': '0', 'value': 48}, {'id': '0', 'next': '13', 'value': 0}, {'id': '13', 'next': '21', 'value': 13}, {'id': '21', 'next': '33', 'value': 21}, {'id': '33', 'next': '9', 'value': 33}, {'id': '9', 'next': None, 'value': 9}]}, {'head': '13', 'nodes': [{'id': '13', 'next': '21', 'value': 13}, {'id': '21', 'next': '33', 'value': 21}, {'id': '33', 'next': '9', 'value': 33}, {'id': '9', 'next': None, 'value': 9}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': None, 'value': 2}]}, {'head': '3', 'nodes': [{'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': None, 'value': 4}]}, {'head': None, 'nodes': []}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': None, 'value': 2}]}, {'head': '3', 'nodes': [{'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': None, 'value': 6}]}, {'head': None, 'nodes': []}]
]

@pytest.mark.parametrize("linkedListOne, linkedListTwo, expected", cases)
def test_mergingLinkedList(linkedListOne, linkedListTwo, expected):
    nodesOne = {node['id']:LinkedList(node['id'],node['value']) for node in linkedListOne['nodes']}
    for node in linkedListOne['nodes']:
        nodesOne[node['id']].next = nodesOne.get(node['next'],None)

    nodesTwo = {node['id']:LinkedList(node['id'],node['value']) for node in linkedListTwo['nodes']}
    for node in linkedListTwo['nodes']:
        nodesTwo[node['id']].next = nodesTwo.get(node['next'],None)

    candidate = []
    node = mergingLinkedList(nodesOne[linkedListOne['head']],nodesTwo[linkedListTwo['head']])
    while node:
        candidate.append({
            'id': node.id,
            'next': node.next.id if node.next else None,
            'value': node.value
            })
        node = node.next
    ic(candidate)
    ic(expected['nodes'])
    assert candidate == expected['nodes']
