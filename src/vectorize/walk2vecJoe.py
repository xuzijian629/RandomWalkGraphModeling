from src.graph.graph import Graph
import numpy as np

class walk2vecJoe:
    def __init__(self, g: Graph, s):
        self.g = g
        self.s = s

    def preprocess(self):
        self.I = np.diag(1 / np.sqrt(np.sum(self.g.A, axis=0)))
        self.W = [np.diag(1 / np.sum(self.g.A, axis=0)).dot(self.g.A)]
        for _ in range(self.s - 1):
            self.W.append(self.W[-1].dot(self.W[0]))
        self.IW = []
        for i in range(self.s):
            self.IW.append(np.transpose(self.I.dot(np.transpose(self.W[i]))))

    def getDist(self, t):
        v = self.getDistVector(t)
        v, minmax = normalizeVector(v)
        return vectorToMatrix(v), minmax

    def getDistVector(self, t):
        assert 1 <= t <= self.s, "invalid step number"
        ret = []
        for i in range(self.g.n):
            for j in range(i + 1, self.g.n):
                ret.append(np.linalg.norm(self.IW[t - 1][i] - self.IW[t - 1][j]))
        return np.array(ret)

    def encode(self, bins=50):
        ret = np.zeros(self.g.n * (self.g.n - 1) // 2)
        for i in range(self.s):
            v = self.getDistVector(1 + i)
            v, _ = normalizeVector(v)
            ret += v
        y, edges = np.histogram(ret, bins=bins)
        return y.tolist() + edges.tolist()

def normalizeVector(v):
    ave = np.average(v)
    v -= ave
    var = np.var(v)
    v /= np.sqrt(var)
    return v, (min(v), max(v))

def vectorToMatrix(v):
    s = len(v)
    n = int(np.sqrt(s))
    while s != n * (n - 1) / 2:
        n += 1
    ret = np.zeros((n, n)) - 1e9
    k = 0
    for i in range(n):
        for j in range(i + 1, n):
            ret[i, j] = v[k]
            ret[j, i] = v[k]
            k += 1
    assert k == s
    return ret
