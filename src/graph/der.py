from src.graph.directed import DirectedGraph
import random

class DER(DirectedGraph):
    def __init__(self, n, p):
        assert 0 < p <= 1, "invalid probability"
        super().__init__(n)
        for i in range(n):
            for j in range(n):
                if i != j:
                    if random.random() < p:
                        self.addArc(i, j)
