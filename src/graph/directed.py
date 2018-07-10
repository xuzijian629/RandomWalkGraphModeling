import numpy as np

class DirectedGraph:
    def __init__(self, n):
        assert 5 <= n <= 2000, "too less or too many nodes to construct a graph"
        self.n = n
        self.A = np.zeros((n, n), dtype=np.int)
    def addArc(self, i, j):
        assert 0 <= i < self.n and 0 <= j < self.n, "invalid node id when addingg arc"
        assert self.A[i, j] == 0, "arc already exists"
        assert i != j, "graph must not have self loop"
        self.A[i, j] = 1
