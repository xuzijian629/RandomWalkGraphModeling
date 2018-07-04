from src.graph.graph import Graph
import random

class SB(Graph):
    def __init__(self, n, delta):
        assert 0 <= delta <= 1, "invalid delta"
        assert n % 2 == 0, "node number must be even in SB"
        super().__init__(n)
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                if random.random() < 0.5 + delta / 2:
                    self.addEdge(i, j)
        for i in range(n // 2, n):
            for j in range(i + 1, n):
                if random.random() < 0.5 + delta / 2:
                    self.addEdge(i, j)
        for i in range(n // 2):
            for j in range(n // 2, n):
                if random.random() < 0.5 - delta / 2:
                    self.addEdge(i, j)
