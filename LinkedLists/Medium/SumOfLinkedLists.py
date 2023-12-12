"""
  DESCRIPTION

  You're given two Linked Lists of potentially unequal length. Each Linked List
  represents a non-negative integer, where each node in the Linked List is a   
  digit of that integer, and the first node in each Linked List always
  represents the least significant digit of the integer. Write a function that 
  returns the head of a new Linked List that represents the sum of the integers
  represented by the two input Linked Lists.


  Each LinkedList node has an integer value as well as
  a next node pointing to the next node in the list or to
  None / null if it's the tail of the list. The
  value of each LinkedList node is always in the range
  of 0 - 9.


  Note: your function must create and return a new Linked List, and you're not 
  allowed to modify either of the input Linked Lists.




  Time complexity O(max(n,m)) n - length of LinkedList One, 
  Space complexity O(max(n,m)) m - length of LinkedList Two
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

def sumOfLinkedLists(linkedListOne, linkedListTwo):
    nodeOne, nodeTwo = linkedListOne, linkedListTwo
    add = 0

    outputNode = LinkedList('',0)
    currentNode = outputNode

    if not nodeOne:
        return nodeTwo
    if not nodeTwo:
        return nodeOne

    while nodeOne or nodeTwo or add!=0:
        one = nodeOne.value if nodeOne else 0
        two = nodeTwo.value if nodeTwo else 0

        current_sum = one + two + add

        add = current_sum//10
        currentNode.next = LinkedList('',current_sum%10)
        currentNode = currentNode.next

        nodeOne = nodeOne.next if nodeOne else None
        nodeTwo = nodeTwo.next if nodeTwo else None


    return outputNode.next





# case [linkedListOne, linkedListTwo, expected]
cases = [
    [{'head': '2', 'nodes': [{'id': '2', 'next': '4', 'value': 2}, {'id': '4', 'next': '7', 'value': 4}, {'id': '7', 'next': '1', 'value': 7}, {'id': '1', 'next': None, 'value': 1}]}, {'head': '9', 'nodes': [{'id': '9', 'next': '4', 'value': 9}, {'id': '4', 'next': '5', 'value': 4}, {'id': '5', 'next': None, 'value': 5}]}, {'head': '1', 'nodes': [{'id': '1', 'next': '9', 'value': 1}, {'id': '9', 'next': '2', 'value': 9}, {'id': '2', 'next': '2-2', 'value': 2}, {'id': '2-2', 'next': None, 'value': 2}]}],
    [{'head': '2', 'nodes': [{'id': '2', 'next': None, 'value': 2}]}, {'head': '9', 'nodes': [{'id': '9', 'next': None, 'value': 9}]}, {'head': '1', 'nodes': [{'id': '1', 'next': '1-2', 'value': 1}, {'id': '1 -2', 'next': None, 'value': 1}]}],
    [{'head': '0', 'nodes': [{'id': '0', 'next': '0-2', 'value': 0}, {'id': '0-2', 'next': '0-3', 'value': 0}, {'id': '0-3', 'next': '5', 'value': 0}, {'id': '5', 'next': None, 'value': 5}]}, {'head': '9', 'nodes': [{'id': '9', 'next': None, 'value': 9}]}, {'head': '9', 'nodes': [{'id': '9', 'next': '0', 'value': 9}, {'id': '0', 'next': '0-2', 'value': 0}, {'id': '0-2', 'next': '5', 'value': 0}, {'id': '5', 'next': None, 'value': 5}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '1-2', 'value': 1}, {'id': '1-2', 'next': '1-3', 'value': 1}, {'id': '1-3', 'next': None, 'value': 1}]}, {'head': '9', 'nodes': [{'id': '9', 'next': '9-2', 'value': 9}, {'id': '9-2', 'next': '9-3', 'value': 9}, {'id': '9-3', 'next': None, 'value': 9}]}, {'head': '0', 'nodes': [{'id': '0', 'next': '1', 'value': 0}, {'id': '1', 'next': '1-2', 'value': 1}, {'id': '1-2', 'next': '1-3', 'value': 1}, {'id': '1-3', 'next': None, 'value': 1}]}],
    [{'head': '1', 'nodes': [{'id': '1', 'next': '2', 'value': 1}, {'id': '2', 'next': '3', 'value': 2}, {'id': '3', 'next': None, 'value': 3}]}, {'head': '6', 'nodes': [{'id': '6', 'next': '7', 'value': 6}, {'id': '7', 'next': '9', 'value': 7}, {'id': '9', 'next': '1', 'value': 9}, {'id': '1', 'next': '8', 'value': 1}, {'id': '8', 'next': None, 'value': 8}]}, {'head': '7', 'nodes': [{'id': '7', 'next': '9', 'value': 7}, {'id': '9', 'next': '2', 'value': 9}, {'id': '2', 'next': '2-2', 'value': 2}, {'id': '2-2', 'next': '8', 'value': 2}, {'id': '8', 'next': None, 'value': 8}]}],
    [{'head': '0', 'nodes': [{'id': '0', 'next': None, 'value': 0}]}, {'head': '0', 'nodes': [{'id': '0', 'next': None, 'value': 0}]}, {'head': '0', 'nodes': [{'id': '0', 'next': None, 'value': 0}]}],
    [{'head': '0', 'nodes': [{'id': '0', 'next': None, 'value': 0}]}, {'head': '0', 'nodes': [{'id': '0', 'next': '0-2', 'value': 0}, {'id': '0-2', 'next': '0-3', 'value': 0}, {'id': '0-3', 'next': '0-4', 'value': 0}, {'id': '0-4', 'next': '0-5', 'value': 0}, {'id': '0-5', 'next': '8', 'value': 0}, {'id': '8', 'next': None, 'value': 8}]}, {'head': '0', 'nodes': [{'id': '0', 'next': '0-2', 'value': 0}, {'id': '0-2', 'next': '0-3', 'value': 0}, {'id': '0-3', 'next': '0-4', 'value': 0}, {'id': '0-4', 'next': '0-5', 'value': 0}, {'id': '0-5', 'next': '8', 'value': 0}, {'id': '8', 'next': None, 'value': 8}]}],
    [{'head': '4', 'nodes': [{'id': '4', 'next': '6', 'value': 4}, {'id': '6', 'next': '9', 'value': 6}, {'id': '9', 'next': '3', 'value': 9}, {'id': '3', 'next': '1', 'value': 3}, {'id': '1', 'next': None, 'value': 1}]}, {'head': '0', 'nodes': [{'id': '0', 'next': '0-2', 'value': 0}, {'id': '0-2', 'next': '0-3', 'value': 0}, {'id': '0-3', 'next': '0-4', 'value': 0}, {'id': '0-4', 'next': '2', 'value': 0}, {'id': '2', 'next': '7', 'value': 2}, {'id': '7', 'next': None, 'value': 7}]}, {'head': '4', 'nodes': [{'id': '4', 'next': '6', 'value': 4}, {'id': '6', 'next': '9', 'value': 6}, {'id': '9', 'next': '3', 'value': 9}, {'id': '3', 'next': '3-2', 'value': 3}, {'id': '3-2', 'next': '7', 'value': 3}, {'id': '7', 'next': None, 'value': 7}]}]
]

@pytest.mark.parametrize("linkedListOne, linkedListTwo, expected", cases)
def test_sumOfLinkedLists(linkedListOne, linkedListTwo, expected):
    nodesOne = {node['id']:LinkedList(node['id'],node['value']) for node in linkedListOne['nodes']}
    for node in linkedListOne['nodes']:
        nodesOne[node['id']].next = nodesOne.get(node['next'],None)

    nodesTwo = {node['id']:LinkedList(node['id'],node['value']) for node in linkedListTwo['nodes']}
    for node in linkedListTwo['nodes']:
        nodesTwo[node['id']].next = nodesTwo.get(node['next'],None)

    candidate = []
    node = sumOfLinkedLists(nodesOne[linkedListOne['head']],nodesTwo[linkedListTwo['head']])
    while node:
        candidate.append({
            'id': node.id,
            'next': node.next.id if node.next else None,
            'value': node.value
            })
        node = node.next
    ic(candidate)
    ic(expected['nodes'])
    assert [c['value'] for c in candidate]==[e['value'] for e in expected['nodes']]
