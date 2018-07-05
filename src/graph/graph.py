import numpy as np

class Graph:
    def __init__(self, n):
        assert 5 <= n <= 2000, "too less or too many nodes to construct a graph"
        self.n = n
        self.A = np.zeros((n, n), dtype=np.int)
    def addEdge(self, i, j):
        assert 0 <= i < self.n and 0 <= j < self.n, "invalid node id when adding edge"
        assert self.A[i, j] == 0, "edge already exists"
        assert i != j, "graph must not have self loop"
        self.A[i, j] = 1
        self.A[j, i] = 1
