from __future__ import print_function
import sys

class Graph:
    def __init__(self, nodes):
        self.numVertices = nodes
        self.edges = []
        self.vertices = []

    def populateEdges(self, u, v, dist):
        self.edges.append([u, v, dist])

    def populateVertices(self, v):
        if v not in self.vertices:
            self.vertices.append(v)


    def BF(self, s):
        temp = {}
        dist_dict = {}
        prev_dict = {}

        for v in self.vertices:
            if (s == v):
                dist_dict[s] = 0
            else:
                dist_dict[v] = sys.maxsize/2
            prev_dict[v] = sys.maxsize/2

        for k in range(1, self.numVertices+1):
            for v in self.vertices:
                for item in self.edges:
                    if item[1] == v:
                        u = item[0]
                        if (dist_dict[v] > dist_dict[u] + item[2]):
                            dist_dict[v] = dist_dict[u] + item[2]
                            prev_dict[v] = u
            if (temp == dist_dict):
                print("False")
                sys.exit()
            else:
                if (k == self.numVertices):
                    print("True")
                    sys.exit()
            temp = dist_dict.copy()


n, m, s = raw_input().split()
if (int(n) < 3):
    print("False")
    sys.exit()

edges = []

for i in range (int(m)):
    edges.append(map(int, raw_input().split()))

g = Graph(int(n))

for edge in edges:
    u, v, dist = [edge[i] for i in (0, 1, 2)]
    g.populateEdges(u, v, dist)
    g.populateVertices(u)
    g.populateVertices(v)

g.BF(int(s))
