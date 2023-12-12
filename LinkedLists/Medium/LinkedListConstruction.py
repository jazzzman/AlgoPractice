"""
  DESCRIPTION

  Write a DoublyLinkedList class that has a head and a
  tail, both of which point to either a linked list
  Node or None / null. The class should
  support:
  
    Setting the head and tail of the linked list.
  
  
    Inserting nodes before and after other nodes as well as at given positions
    (the position of the head node is 1).
  
    Removing given nodes and removing nodes with given values.
    
    Searching for nodes with given values.


  Note that the setHead, setTail,
  insertBefore, insertAfter,
  insertAtPosition, and remove methods all take in
  actual Nodes as input parameters—not integers (except for
  insertAtPosition, which also takes in an integer representing the
  position); this means that you don't need to create any new Nodes
  in these methods. The input nodes can be either stand-alone nodes or nodes
  that are already in the linked list. If they're nodes that are already in the
  linked list, the methods will effectively be moving the nodes within
  the linked list. You won't be told if the input nodes are already in the
  linked list, so your code will have to defensively handle this scenario.


  If you're doing this problem in an untyped language like Python or JavaScript,
  you may want to look at the various function signatures in a typed language
  like Java or TypeScript to get a better idea of what each input parameter is.


  Each Node has an integer value as well as a
  prev node and a next node, both of which can point
  to either another node or None / null.



  Time complexity O(###)
  Space complexity O(###)
"""
import pytest

# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        self.insertBefore(self.head, node)

    def setTail(self, node):
        if self.head is None:
            self.head = node
            self.tail = node

        self.insertAfter(self.tail, node)

    def insertBefore(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return

        self.remove(nodeToInsert)

        nodeToInsert.prev = node.prev
        nodeToInsert.next = node

        if node.prev is None:
            self.head = nodeToInsert
        else:
            node.prev.next = nodeToInsert

        node.prev = nodeToInsert

    def insertAfter(self, node, nodeToInsert):
        if nodeToInsert == self.head and nodeToInsert == self.tail:
            return
        self.remove(nodeToInsert)

        nodeToInsert.next = node.next
        nodeToInsert.prev = node

        if node.next is None:
            self.tail = nodeToInsert
        else:
            node.next.prev = nodeToInsert

        node.next = nodeToInsert

    def insertAtPosition(self, position, nodeToInsert):
        if position == 1:
            self.setHead(nodeToInsert)
            return

        node = self.head
        for i in range(1, position):
            if node.next is None:
                return
            else:
                node = node.next

        if node is not None:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)


    def removeNodesWithValue(self, value):
        node = self.head
        while node:
            nodeToRemove = node
            node = node.next
            if node.value == value:
                self.remove(node)
            
    def remove(self, node):
        if node == self.head:
            self.head = node.next
        if node == slef.tail:
            self.tail = node.prev

        self.removeBindings(node)
        return node

    def containsNodeWithValue(self, value):
        node = self.head
        while node:
            if node.value == value:
                return node
            node = node.next
        return None

    def removeBindings(self, node):
        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.prev = None
        node.next = None


def linkedListConstruction(operations, linkedList):
    return []


# case [linkedList, expected]
cases = [
    [[{'arguments': ['1'], 'method': 'setHead'}], 
     [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 
     [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}]],
    [[{'arguments': ['1'], 'method': 'setTail'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}], [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setTail', 'output': None}]],
    [[{'arguments': [1, '1'], 'method': 'insertAtPosition'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}], [{'arguments': [1, '1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'insertAtPosition', 'output': None}]],
    [[{'arguments': ['1'], 'method': 'setHead'}, {'arguments': ['2'], 'method': 'setTail'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}, {'id': '2', 'next': None, 'prev': None, 'value': 2}], [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}, {'arguments': ['2'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': '2', 'prev': None, 'value': 1}, {'id': '2', 'next': None, 'prev': '1', 'value': 2}], 'tail': '2'}, 'method': 'setTail', 'output': None}]],
    [[{'arguments': ['1'], 'method': 'setHead'}, {'arguments': ['2'], 'method': 'setHead'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}, {'id': '2', 'next': None, 'prev': None, 'value': 2}], [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}, {'arguments': ['2'], 'linkedList': {'head': '2', 'nodes': [{'id': '2', 'next': '1', 'prev': None, 'value': 2}, {'id': '1', 'next': None, 'prev': '2', 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}]],
    [[{'arguments': ['1'], 'method': 'setHead'}, {'arguments': ['1', '2'], 'method': 'insertAfter'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}, {'id': '2', 'next': None, 'prev': None, 'value': 2}], [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}, {'arguments': ['1', '2'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': '2', 'prev': None, 'value': 1}, {'id': '2', 'next': None, 'prev': '1', 'value': 2}], 'tail': '2'}, 'method': 'insertAfter', 'output': None}]],
    [[{'arguments': ['1'], 'method': 'setHead'}, {'arguments': ['1', '2'], 'method': 'insertBefore'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}, {'id': '2', 'next': None, 'prev': None, 'value': 2}], [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}, {'arguments': ['1', '2'], 'linkedList': {'head': '2', 'nodes': [{'id': '2', 'next': '1', 'prev': None, 'value': 2}, {'id': '1', 'next': None, 'prev': '2', 'value': 1}], 'tail': '1'}, 'method': 'insertBefore', 'output': None}]],
    [[{'arguments': ['1'], 'method': 'setHead'}, {'arguments': ['1'], 'method': 'remove'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}], [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}, {'arguments': ['1'], 'linkedList': {'head': None, 'nodes': [], 'tail': None}, 'method': 'remove', 'output': None}]],
    [[{'arguments': ['1'], 'method': 'setHead'}, {'arguments': [1], 'method': 'removeNodesWithValue'}], [{'id': '1', 'next': None, 'prev': None, 'value': 1}], [{'arguments': ['1'], 'linkedList': {'head': '1', 'nodes': [{'id': '1', 'next': None, 'prev': None, 'value': 1}], 'tail': '1'}, 'method': 'setHead', 'output': None}, {'arguments': [1], 'linkedList': {'head': None, 'nodes': [], 'tail': None}, 'method': 'removeNodesWithValue', 'output': None}]],
]

@pytest.mark.skip("Cases were not implemented")
@pytest.mark.parametrize("operations, linkedList, expected", cases)
def test_linkedListConstruction(operations, linkedList, expected):
    assert linkedListConstruction(linkedList)==expected
