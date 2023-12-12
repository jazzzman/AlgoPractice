"""
  DESCRIPTION

  You're given the head of a Singly Linked List whose nodes are in sorted order 
  with respect to their values. Write a function that returns a modified version
  of the Linked List that doesn't contain any nodes with duplicate values. The  
  Linked List should be modified in place (i.e., you shouldn't create a brand   
  new list), and the modified Linked List should still have its nodes sorted    
  with respect to their values.


  Each LinkedList node has an integer value as well as
  a next node pointing to the next node in the list or to
  None / null if it's the tail of the list.



  Time complexity O(n)
  Space complexity O(1)
"""
import pytest

from icecream import ic


class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return f'value: {self.value}'

def removeDuplicatesFromLinkedList(linkedList):
    node = linkedList
    while node.next:
        if node.value == node.next.value:
            node.next = node.next.next
        else:
            node = node.next
    return linkedList


# case [linkedList, expected]
cases = [
    [{'head': '1', 
      'nodes': [
          {'id': '1', 'next': '1-2', 'value': 1}, 
          {'id': '1-2', 'next': '1-3', 'value': 1}, 
          {'id': '1-3', 'next': '2', 'value': 1}, 
          {'id': '2', 'next': '3', 'value': 3}, 
          {'id': '3', 'next': '3-2', 'value': 4}, 
          {'id': '3-2', 'next': '3-3', 'value': 4}, 
          {'id': '3-3', 'next': '4', 'value': 4}, 
          {'id': '4', 'next': '5', 'value': 5},
          {'id': '5', 'next': '5-2', 'value': 6},
          {'id': '5-2', 'next': None, 'value': 6}]}, 
     {'head': '1', 
      'nodes': [
          {'id': '1', 'next': '3', 'value': 1},
          {'id': '3', 'next': '4', 'value': 3},
          {'id': '4', 'next': '5', 'value': 4},
          {'id': '5', 'next': '6', 'value': 5},
          {'id': '6', 'next': None, 'value': 6}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '1-2', 'value': 1}, {'id': '1-2', 'next': '1-3', 'value': 1}, {'id': '1-3', 'next': '1-4', 'value': 1}, {'id': '1-4', 'next': '1-5', 'value': 1}, {'id': '1-5', 'next': '4', 'value': 1}, {'id': '4', 'next': '4-2', 'value': 4}, {'id': '4-2', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '6-2', 'value': 6}, {'id': '6-2', 'next': None, 'value': 6}]}, {'head': '1', 'nodes': [{'id': '1', 'next': '4', 'value': 1}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': None, 'value': 6}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '1-2', 'value': 1}, {'id': '1-2', 'next': '1-3', 'value': 1}, {'id': '1-3', 'next': '1-4', 'value': 1}, {'id': '1-4', 'next': '1-5', 'value': 1}, {'id': '1-5', 'next': '1-6', 'value': 1}, {'id': '1-6', 'next': '1-7', 'value': 1}, {'id': '1-7', 'next': None, 'value': 1}]}, {'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '9', 'value': 1}, {'id': '9', 'next': '11', 'value': 9}, {'id': '11', 'next': '15', 'value': 11}, {'id': '15', 'next': '15-2', 'value': 15}, {'id': '15-2', 'next': '16', 'value': 15}, {'id': '16', 'next': '17', 'value': 16}, {'id': '17', 'next': None, 'value': 17}]}, {'head': '1', 'nodes': [{'id': '1', 'next': '9', 'value': 1}, {'id': '9', 'next': '11', 'value': 9}, {'id': '11', 'next': '15', 'value': 11}, {'id': '15', 'next': '16', 'value': 15}, {'id': '16', 'next': '17', 'value': 16}, {'id': '17', 'next': None, 'value': 17}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}, {'head': '1', 'nodes': [{'id': '1', 'next': None, 'value': 1}]}],
    [{'head': '-5', 'nodes': [{'id': '-5', 'next': '-1', 'value': -5}, {'id': '-1', 'next': '-1-2', 'value': -1}, {'id': '-1-2', 'next': '-1-3', 'value': -1}, {'id': '-1-3', 'next': '5', 'value': -1}, {'id': '5', 'next': '5-2', 'value': 5}, {'id': '5-2', 'next': '5-3', 'value': 5}, {'id': '5-3', 'next': '8', 'value': 5}, {'id': '8', 'next': '8-2', 'value': 8}, {'id': '8-2', 'next': '9', 'value': 8}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': '11', 'value': 10}, {'id': '11', 'next': '11-2', 'value': 11}, {'id': '11-2', 'next': None, 'value': 11}]}, {'head': '-5', 'nodes': [{'id': '-5', 'next': '-1', 'value': -5}, {'id': '-1', 'next': '5', 'value': -1}, {'id': '5', 'next': '8', 'value': 5}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': '11', 'value': 10}, {'id': '11', 'next': None, 'value': 11}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': '11', 'value': 10}, {'id': '11', 'next': '12', 'value': 11}, {'id': '12', 'next': '12-2', 'value': 12}, {'id': '12-2', 'next': None, 'value': 12}]}, {'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': '4', 'value': 3}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': '6', 'value': 5}, {'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '8', 'value': 7}, {'id': '8', 'next': '9', 'value': 8}, {'id': '9', 'next': '10', 'value': 9}, {'id': '10', 'next': '11', 'value': 10}, {'id': '11', 'next': '12', 'value': 11}, {'id': '12', 'next': None, 'value': 12}]}]
]

@pytest.mark.parametrize("linkedList, expected", cases)
def test_removeDuplicatesFromLinkedList(linkedList, expected):
    nodes = {node['id']:LinkedList(node['value']) for node in linkedList['nodes']}
    for node in linkedList['nodes']:
        nodes[node['id']].next = nodes.get(node['next'],None)

    candidate = []
    node = removeDuplicatesFromLinkedList(nodes[linkedList['head']])
    while node:
        candidate.append({
            'id': str(node.value),
            'next': str(node.next.value) if node.next else None,
            'value': node.value
            })
        node = node.next


    assert candidate==expected['nodes']
