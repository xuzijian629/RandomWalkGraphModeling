from src.datasets.generator import *

# number of datasets
TIMES = 1000
# number of nodes
N = 100
# number of random walks
S = 15

if __name__ == '__main__':
    generateERwalk2vec(TIMES, N, 0.5, S)
    generateSBMwalk2vec(TIMES, N, 0.55, 0.45, S)
