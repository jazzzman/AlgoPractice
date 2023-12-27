"""
  DESCRIPTION

  You're given a list of edges representing an unweighted, directed
  graph with at least one node. Write a function that returns a boolean
  representing whether the given graph contains a cycle.


  For the purpose of this question, a cycle is defined as any number of
  vertices, including just one vertex, that are connected in a closed chain. A  
  cycle can also be defined as a chain of at least one vertex in which the first
  vertex is the same as the last.


  The given list is what's called an adjacency list, and it represents a graph. 
  The number of vertices in the graph is equal to the length of
  edges, where each index i in
  edges contains vertex i's outbound edges, in no
  particular order. Each individual edge is represented by a positive integer   
  that denotes an index (a destination vertex) in the list that this vertex is  
  connected to. Note that these edges are directed, meaning that you can only   
  travel from a particular vertex to its destination, not the other way around  
  (unless the destination vertex itself has an outbound edge to the original    
  vertex).


  Also note that this graph may contain self-loops. A self-loop is an edge that 
  has the same destination and origin; in other words, it's an edge that        
  connects a vertex to itself. For the purpose of this question, a self-loop is 
  considered a cycle.


  For a more detailed explanation, please refer to the Conceptual Overview      
  section of this question's video explanation.



  Time complexity O(V+E) V - count of vertices, E - count of edges
  Space complexity O(V)
"""
import pytest

from icecream import ic


def cycleInGraph(edges):
    for idx in range(len(edges)):
        for edge in edges[idx]:
            visited = [0]*len(edges)
            visited[idx] = 1
            if dfs(edge, edges, visited):
                return True
    return False

def dfs(idx, edges, visited):
    if visited[idx] == 1:
        return True
    visited[idx] = 1
    for vertex in edges[idx]:
        result = dfs(vertex,edges, visited)
        if result:
            return result
    visited[idx] = 0
    return False


# case [edges, expected]
cases = [
    [[[1, 3], [2, 3, 4], [0], [], [2, 5], []], True],
    [[[1, 2], [2], []], False],
    [[[1, 2], [2], [1]], True],
    [[[1, 2], [2], [1, 3], [3]], True],
    [[[], [0, 2], [0, 3], [0, 4], [0, 5], [0]], False],
    [[[0]], True],
    [[[8], [0, 2], [0, 3], [0, 4], [0, 5], [0], [7], [8], [6]], True],
    [[[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], []], False],
    [[[1], [2, 3, 4, 5, 6, 7], [], [2, 7], [5], [], [4], [0]], True],
    [[[0], [1]], True],
    [[[1, 2], [2], []], False],
    [[[], [0, 3], [0], [1, 2]], True]
]

@pytest.mark.parametrize("edges, expected", cases)
def test_cycleInGraph(edges, expected):
    assert cycleInGraph(edges)==expected
