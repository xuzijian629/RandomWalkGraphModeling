from src.graph.graph import Graph
import numpy as np

def getMaxNode(g: Graph):
    degs = np.sum(g.A, axis=0)
    return np.argmax(degs)

def getMinNode(g: Graph):
    degs = np.sum(g.A, axis=0)
    return np.argmin(degs)

def getMedianNode(g: Graph):
    degs = np.sum(g.A, axis=0)
    median = np.median(degs)
    return np.argmin(np.abs(degs - median))

def getMeanNode(g: Graph):
    degs = np.sum(g.A, axis=0)
    mean = np.mean(degs)
    return np.argmin(np.abs(degs - mean))

def getM(A, p, s):
    I = np.diag(1 / np.sqrt(np.sum(A, axis=0)))
    W = np.diag(1 / np.sum(A, axis=0)).dot(A)
    ps = [p]
    for i in range(s):
        ps.append(np.transpose(W).dot(ps[-1]))
    ret = []
    for i in range(s):
        for j in range(i + 1, s):
            ret.append(np.linalg.norm(I.dot(ps[i]) - I.dot(ps[j])))
    return ret

def walk2vec(g: Graph, s):
    assert 3 <= s <= 50, "too less or too many random walk steps"
    pmax = np.eye(g.n)[getMaxNode(g)]
    pmin = np.eye(g.n)[getMinNode(g)]
    pmedian = np.eye(g.n)[getMedianNode(g)]
    pmean = np.eye(g.n)[getMeanNode(g)]
    ret = getM(g.A, pmax, s) + getM(g.A, pmin, s) + getM(g.A, pmedian, s) + getM(g.A, pmean, s)
    return ret
