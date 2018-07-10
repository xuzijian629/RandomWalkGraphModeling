from src.vectorize.walk2vecJoe import walk2vecJoe
import matplotlib.pyplot as plt
import numpy as np

def visualizeDists(s, j1: walk2vecJoe, j2: walk2vecJoe):
    fig = plt.figure(figsize=(s * 4, 2 * 4))
    res1 = []
    res2 = []
    for i in range(s):
        res1.append(j1.getDist(i + 1))
        res2.append(j2.getDist(i + 1))
    print("Calculation finished")
    for i in range(s):
        j1d, minmax1 = res1[i]
        j2d, minmax2 = res2[i]
        minLevel = min(minmax1[0], minmax2[0])
        maxLevel = max(minmax1[1], minmax2[1])
        diff = maxLevel - minLevel
        ax = fig.add_subplot(2, s, i + 1)
        ax.contourf(range(j1.g.n), range(j1.g.n), j1d, levels=np.arange(minLevel, maxLevel, diff / 100))
        ax = fig.add_subplot(2, s, i + 1 + s)
        ax.contourf(range(j2.g.n), range(j2.g.n), j2d, levels=np.arange(minLevel, maxLevel, diff / 100))
    plt.savefig('data/dists.0.8.png', dpi=100)

    j1Sum = np.zeros((j1.g.n, j1.g.n))
    j2Sum = np.zeros((j2.g.n, j2.g.n))
    minLevel = 0
    maxLevel = 0
    for i in range(s):
        j1d, minmax1 = res1[i]
        j2d, minmax2 = res2[i]
        j1Sum += j1d
        j2Sum += j2d
        minLevel += min(minmax1[0], minmax2[0])
        maxLevel += max(minmax1[1], minmax2[1])
    diff = maxLevel - minLevel
    fig = plt.figure(figsize=(8, 8))
    ax = fig.add_subplot(2, 2, 1)
    ax.contourf(range(j1.g.n), range(j1.g.n), j1Sum, levels=np.arange(minLevel, maxLevel, diff / 100))
    ax = fig.add_subplot(2, 2, 2)
    ax.contourf(range(j2.g.n), range(j2.g.n), j2Sum, levels=np.arange(minLevel, maxLevel, diff / 100))

    bins=50
    j1Sum_ = []
    j2Sum_ = []
    for i in range(j1.g.n):
        for j in range(i + 1, j1.g.n):
            j1Sum_.append(j1Sum[i, j])
            j2Sum_.append(j2Sum[i, j])
    y1, binedges1 = np.histogram(j1Sum_, bins=bins)
    y2, binedges2 = np.histogram(j2Sum_, bins=bins)
    y1 = np.cumsum(y1)
    y2 = np.cumsum(y2)

    bincenters1 = (binedges1[1:] + binedges1[:-1]) / 2
    bincenters2 = (binedges2[1:] + binedges2[:-1]) / 2
    ax = fig.add_subplot(2, 2, 3)
    ax.plot(bincenters1, y1, 'r-')
    ax.plot(bincenters2, y2, 'b-')
    ax = fig.add_subplot(2, 2, 4)
    ax.plot(bincenters1[:bins // 10], y1[:bins // 10], 'r-')
    ax.plot(bincenters2[:bins // 10], y2[:bins // 10], 'b-')
    plt.savefig('data/distSum.0.8.png', dpi=100)
