from src.graph.er import ER
import numpy as np

class PC(ER):
    def __init__(self, n, beta):
        assert 1.1 < beta < 2.1, "too small or too large beta"
        super().__init__(n, 0.5)
        k = int(np.ceil(beta * np.sqrt(n)))
        for i in range(k):
            for j in range(i + 1, k):
                if not self.A[i, j]:
                    self.addEdge(i, j)
