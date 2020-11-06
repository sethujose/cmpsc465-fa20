from __future__ import print_function
from collections import defaultdict
import sys

class G:
    def __init__ (self, vert_count):
        self.V = vert_count
        self.graph = [[0 for column in range(vert_count)] for rown in range (vert_count)]

    def insertEdge(self, u, v, dist):
        l = [v, dist]
        self.graph[u].append(l)

    def minDistance(self, dist, minDistPath):
        min_val = sys.maxint
        min_index = 0
        for v in range(self.V):
            if dist[v] < min_val and minDistPath[v] == False:
                min_val = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [sys.maxint] * self.V
        dist[src] = 0
        minDistPath = [False] * self.V

        for i in range(self.V):
            u = self.minDistance(dist, minDistPath)
            minDistPath[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and minDistPath[v] == False and dist[v] > dist[u] + self.graph[u][v]:
                    dist[v] = dist[u] + self.graph[u][v]

        for node in range(self.V):
            if (node == self.V - 1):
                print(dist[node], end='')
            else:
                print(dist[node])


n, m, s = raw_input().split()

edges = []
for i in range (int(m)):
    edges.append(list(map(int, raw_input().split())))

g = G(int(n))
edgeList = []

for edge in edges:
    u, v, dist = [edge[i] for i in (0, 1, 2)]
    edgeList.append([u, v])
    g.graph[u-1][v-1] = dist

g.dijkstra(int(s) - 1)
