from src.graph.graph import Graph
import random

class ER(Graph):
    def __init__(self, n, p):
        assert 0 < p < 1, "invalid probability"
        super().__init__(n)
        for i in range(n):
            for j in range(i + 1, n):
                if random.random() < p:
                    self.addEdge(i, j)
