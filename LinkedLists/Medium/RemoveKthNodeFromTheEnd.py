"""
  DESCRIPTION

  Write a function that takes in the head of a Singly Linked List and an integer
  k and removes the kth node from the end of the list.


  The removal should be done in place, meaning that the original data structure 
  should be mutated (no new structure should be created).


  Furthermore, the input head of the linked list should remain the head of the  
  linked list after the removal is done, even if the head is the node that's    
  supposed to be removed. In other words, if the head is the node that's        
  supposed to be removed, your function should simply mutate its
  value and next pointer.

Note that your function doesn't need to return anything.

  You can assume that the input Linked List will always have at least two nodes
  and, more specifically, at least k nodes.


  Each LinkedList node has an integer value as well as
  a next node pointing to the next node in the list or to
  None / null if it's the tail of the list.



  Time complexity O(n)
  Space complexity O(1)
"""
import pytest

from icecream import ic


class LinkedList:
    def __init__(self, id, value):
        self.id = id
        self.next = None
        self.value = value

    def __repr__(self):
        return f'id: {self.id} value:{self.value} next:{self.next.id if self.next else None}'

def removeKthNodeFromEnd(k, linkedList):
    counter = 1
    seek_node = linkedList
    prev_node = None
    node = linkedList

    while seek_node:
        seek_node = seek_node.next
        if counter>k:
            prev_node = node
            node = node.next
        counter += 1

    if prev_node:
        prev_node.next = node.next
    else:
        linkedList = node.next
            

    return linkedList


# case [k, linkedList, expected]
cases = [
    [4, {'head': '0', 'nodes': [
        {'id': '0', 'next': '1', 'value': 0},
        {'id': '1', 'next': '2', 'value': 1},
        {'id': '2', 'next': '3', 'value': 2},
        {'id': '3', 'next': '4', 'value': 3},
        {'id': '4', 'next': '5', 'value': 4},
        {'id': '5', 'next': '6', 'value': 5},
        {'id': '6', 'next': '7', 'value': 6},
        {'id': '7', 'next': '8', 'value': 7},
        {'id': '8', 'next': '9', 'value': 8},
        {'id': '9', 'next': None, 'value': 9}] }, 
        {'head': '0', 'nodes': [
        {'id': '0', 'next': '1', 'value': 0},
        {'id': '1', 'next': '2', 'value': 1},
        {'id': '2', 'next': '3', 'value': 2},
        {'id': '3', 'next': '4', 'value': 3},
        {'id': '4', 'next': '5', 'value': 4},
        {'id': '5', 'next': '7', 'value': 5},
        {'id': '7', 'next': '8', 'value': 7},
        {'id': '8', 'next': '9', 'value': 8},
        {'id': '9', 'next': None, 'value': 9}]}],
    [1, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': None, 'value': 8}]}],
    [2, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '9', 'value': 7}, {'id': '9', 'next': None, 'value': 9}]}],
    [3, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '8', 'value': 6}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}],
    [5, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '6', 'value': 4}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}],
    [6, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '5', 'value': 3}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}],
    [7, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '4', 'value': 2}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}],
    [8, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '3', 'value': 1}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}],
    [9, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}] }, {'head': '0', 'nodes': [{'id': '0', 'next': '2', 'value': 0}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}],
    [10, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5' , 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9} ]}, {'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': None, 'value': 9}]}]
]

@pytest.mark.parametrize("k, linkedList, expected", cases)
def test_removeKthNodeFromEnd(k, linkedList, expected):
    nodes = {node['id']:LinkedList(node['id'],node['value']) for node in linkedList['nodes']}
    for node in linkedList['nodes']:
        nodes[node['id']].next = nodes.get(node['next'],None)

    candidate = []
    node = removeKthNodeFromEnd(k,nodes[linkedList['head']])
    while node:
        candidate.append({
            'id': node.id,
            'next': node.next.id if node.next else None,
            'value': node.value
            })
        node = node.next
    assert candidate==expected['nodes']
