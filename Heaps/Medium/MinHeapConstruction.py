"""
  DESCRIPTION


  Time complexity O(###)
  Space complexity O(###)
"""
import pytest


class MinHeap:
    def __init__(self, array):
        self.buildHeap(array)

    def buildHeap(self, array):
        self.heap = array
        parent = (len(array)-1)//2
        for idx in reversed(range(parent+1)):
            self.siftDown(idx)

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)


    def remove(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        removedValue = self.heap.pop()
        self.siftDown(0)
        return removedValue

    def siftUp(self, idx):
        parent = (idx-1)//2

        while idx>0 and self.heap[idx]<self.heap[parent]:
            self.heap[idx], self.heap[parent] = self.heap[parent], self.heap[idx]
            idx = parent
            parent = (idx-1)//2

    def siftDown(self, idx):
        heap = self.heap
        child1 = 2*idx+1
        while child1<len(heap):
            child2 = 2*idx+2 if 2*idx+2<len(heap) else -1
            idxToSwap = child2 if child2 != -1 and heap[child2]<heap[child1] else child1
            if heap[idx]>heap[idxToSwap]:
                heap[idx], heap[idxToSwap] = heap[idxToSwap], heap[idx]
                idx = idxToSwap
                child1 = 2*idx+1
            else:
                return



    
def minHeapConstruction(array, method, values):
    if method == 'buildHeap':
        return MinHeap(array).heap
    elif method == 'insert':
        minHeap = MinHeap(array)
        for value in values:
            minHeap.insert(value)
        return minHeap.heap
    elif method == 'remove':
        minHeap = MinHeap(array)
        for value in values:
            minHeap.remove()
        return minHeap.heap

    return []


# case [array, method, values, expected]
cases = [
    [[7,2,5,3,1,6,4],'buildHeap',[],[1,2,4,3,7,6,5]],
    [[7,2,5,3,1,6,4],'insert',[8],[1,2,4,3,7,6,5,8]],
    [[7,2,5,3,1,6,4],'insert',[0],[0,1,4,2,7,6,5,3]],
    [[7,2,5,3,1,6,4],'remove',[3],[2,3,4,5,7,6]],
]

@pytest.mark.parametrize("array, method, values, expected", cases)
def test_minHeapConstruction(array, method, values, expected):
    assert minHeapConstruction(array, method, values)==expected


