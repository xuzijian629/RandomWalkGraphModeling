from src.graph.graph import Graph
import numpy as np

def isConnected(g: Graph):
    visited = np.zeros(g.n, dtype=np.int)
    def dfs(i):
        if visited[i]: return
        visited[i] = 1
        for j in range(g.n):
            if g.A[i,j]: dfs(j)
    dfs(0)
    return sum(visited) == g.n
