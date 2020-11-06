from collections import defaultdict

class Graph:
    def __init__(self, nodes):
        self.V = nodes
        self.graph = defaultdict(list)

    def insertEdge(self, u, v):
        self.graph[u].append(v)

    def explore(self, v, visited, stack):
        visited[v] = 1
        for i in self.graph[v]:
            if visited[i] == 0:
                self.explore(i, visited, stack)
        stack = stack.append(v)

    def getTranspose(self):
        gTemp = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                gTemp.insertEdge(j, i)
        return gTemp

    def DFS(self, v, visited):
        visited[v] = 1
        for i in self.graph[v]:
            if visited[i] == 0:
                self.DFS(i, visited)

    def getCC(self):
        stack = []
        visited = [0] * (self.V + 1)
        for i in range(1, self.V):
            if visited[i] == 0:
                self.explore(i, visited, stack)

        visited = [0] * (self.V + 1)
        gr = self.getTranspose()
        cc = 0
        while stack:
            i = stack.pop()
            if visited[i] == 0:
                gr.DFS(i, visited)
                cc = cc + 1
        return cc

n, m = raw_input().split()
edges = []

for i in range (int(m)):
    edges.append(map(int, raw_input().split()))


g = Graph(int(n))

for edge in edges:
    u, v = [edge[i] for i in (0, 1)]
    g.insertEdge(u, v)

num_cc = g.getCC()
print(str(num_cc)),
