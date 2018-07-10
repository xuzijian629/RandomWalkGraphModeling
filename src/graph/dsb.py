from src.graph.directed import DirectedGraph
import random

class DSB(DirectedGraph):
    def __init__(self, n, delta):
        assert 0 <= delta <= 1, "invalid delta"
        assert n % 2 == 0, "node number must be even in SB"
        super().__init__(n)
        for i in range(n // 2):
            for j in range(n // 2):
                if i != j:
                    if random.random() < 0.5 + delta / 2:
                        self.addArc(i, j)
        for i in range(n // 2, n):
            for j in range(n // 2, n):
                if i != j:
                    if random.random() < 0.5 + delta / 2:
                        self.addArc(i, j)
        for i in range(n // 2):
            for j in range(n // 2, n):
                if random.random() < 0.5 - delta / 2:
                    self.addArc(i, j)
                if random.random() < 0.5 - delta / 2:
                    self.addArc(j, i)
