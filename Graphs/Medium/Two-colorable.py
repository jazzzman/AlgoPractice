"""
  DESCRIPTION

    You're given a list of edges representing a connected,
    unweighted, undirected graph with at least one node. Write a function that   
    returns a boolean representing whether the given graph is two-colorable.     


    A graph is two-colorable (also called bipartite) if all of the nodes can     
    be assigned one of two colors such that no nodes of the same color are       
    connected by an edge.


    The given list is what's called an adjacency list, and it represents a graph.
    The number of vertices in the graph is equal to the length of
    edges, where each index i in
    edges contains vertex i's siblings, in no
    particular order. Each individual edge is represented by a positive integer  
    that denotes an index in the list that this vertex is connected to. Note that
    this graph is undirected, meaning that if a vertex appears in the edge list  
    of another vertex, then the inverse will also be true.


    Also note that this graph may contain self-loops. A self-loop is an edge that
    has the same destination and origin; in other words, it's an edge that       
    connects a vertex to itself. Any self-loop should make a graph not
    2-colorable.


  Time complexity O(V+E)
  Space complexity O(V)
"""
import pytest

from icecream import ic


def twoColorable(matrix):
    visited = [0]*len(matrix)
    for idx in range(len(visited)
        if not helper(idx, visited, matrix):
            return False
    return True

def helper(idx, visited, matrix):
    color = visited[idx] if visited[idx]!=0 else 1
    
    for child in matrix[idx]:
        if child == idx or visited[child]==color:
            return False
        else:
            visited[child] = 1 if color == 2 else 2

    return True


# case [matrix, expected]
cases = [
    [[[1], [0]], True],
    [[[0]], False],
    [[[1, 2], [0, 2], [0, 1]], False],
    [[[1], [0, 2], [1]], True],
    [[[1, 2, 3], [0], [0], [0]], True],
    [[[1, 2, 3], [0, 2], [0, 1], [0]], False],
    [[[1, 2, 3], [0, 2, 3], [0, 1], [0, 1]], False],
    [[[2], [2, 3], [0, 1], [1]], True],
    [[[1, 2], [0, 2, 3], [0, 1, 3], [1, 2]], False],
    [[[1, 4], [0, 2, 3], [1, 3, 4], [1, 2], [0, 2]], False],
    [[[1, 4], [0, 2, 3], [1, 4], [1], [0, 2]], True]
]

@pytest.mark.parametrize("matrix, expected", cases)
def test_twoColorable(matrix, expected):
    assert twoColorable(matrix)==expected
