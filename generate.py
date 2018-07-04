from src.datasets.generator import *

# number of datasets
TIMES = 1000
# number of nodes
N = 100
# number of random walks
S = 15
# constant for SB graph
delta = 0.05
# constant for PC graph
beta = 1.8

if __name__ == '__main__':
    # generateERwalk2vec(TIMES, N, 0.5, S)
    # generateSBwalk2vec(TIMES, N, delta, S)
    # generatePCwalk2vec(TIMES, N, beta, S)
    generateERwalk2vecSC(TIMES, N, 0.5, S)
    # generateSBwalk2vecSC(TIMES, N, delta, S)
    generatePCwalk2vecSC(TIMES, N, beta, S)
