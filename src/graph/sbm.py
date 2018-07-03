from src.graph.graph import Graph
import random

class SBM(Graph):
    def __init__(self, n, pin, pout):
        assert 0 < pin < 1 and 0 < pout < 1 and pin + pout == 1, "invalid probability"
        assert pin > pout, "pin must be greater than pout"
        assert n % 2 == 0, "node number must be even in SBM"
        super().__init__(n)
        for i in range(n // 2):
            for j in range(i + 1, n // 2):
                if random.random() < pin:
                    self.addEdge(i, j)
        for i in range(n // 2, n):
            for j in range(i + 1, n):
                if random.random() < pin:
                    self.addEdge(i, j)
        for i in range(n // 2):
            for j in range(n // 2, n):
                if random.random() < pout:
                    self.addEdge(i, j)
