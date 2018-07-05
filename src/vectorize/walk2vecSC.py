from src.graph.graph import Graph
from src.vectorize.walk2vec import getM
import numpy as np

def getMs(g: Graph, s):
    assert 3 <= s <= 50, "too less or too many random walk steps"
    xs = []
    for i in range(g.n):
        xs.append(getM(g.A, np.eye(g.n)[i], s))
    return xs
