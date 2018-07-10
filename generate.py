from src.datasets.generator import *
from src.learn.learner import *

# number of datasets
times = 500
# number of nodes
n = 100
# number of random walks
s = 15
# constant for sB graph
delta = 0.16
# constant for PC graph
beta = 1.8
# constant for sparse coding
atom, l = 100, 0.15

if __name__ == '__main__':
    generateDERwalk2vec(times, n, 0.5, s)
    generateDSBwalk2vec(times, n, delta, s)
    # generatePCwalk2vec(times, n, beta, s)
    generateDHMwalk2vec(times, n, s)
    # D = MiniBatchDictionaryLearning(n_components=atom, alpha=l)
    # ers = generateERvs(times, n, 0.5, s)
    # sbs = generateSBvs(times, n, delta, s)
    # D, ers, sbs = learnDictionary(D, ers, sbs)
    # generateWalk2vecSC(D, times, n, ers, l)
    # generateWalk2vecSC(D, times, n, sbs, l)
