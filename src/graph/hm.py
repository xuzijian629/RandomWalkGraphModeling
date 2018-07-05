from src.graph.er import ER
import numpy as np

class HM(ER):
    def __init__(self, n):
        super().__init__(n, 0.5)
        for i in range(n):
            if not self.A[i, (i + 1) % n]:
                self.addEdge(i, (i + 1) % n)
