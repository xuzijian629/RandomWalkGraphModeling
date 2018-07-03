import numpy as np

class Graph:
    def __init__(self, n):
        assert 100 <= n <= 1000, "too less or too many nodes to construct a graph"
        self.n = n
        self.A = np.zeros((n, n))
    def addEdge(self, i, j):
        assert 0 <= i < self.n and 0 <= j < self.n, "invalid node id when adding edge"
        assert self.A[i,j] == 0, "edge already exists"
        self.A[i,j] = 1
        self.A[j,i] = 1
