from src.graph.der import DER
import numpy as np

class DHM(DER):
    def __init__(self, n):
        super().__init__(n, 0.5)
        for i in range(n):
            if not self.A[i, (i + 1) % n]:
                self.addArc(i, (i + 1) % n)
