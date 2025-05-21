class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        if xroot == yroot:
            return False
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        else:
            self.parent[yroot] = xroot
            if self.rank[xroot] == self.rank[yroot]:
                self.rank[xroot] += 1
        return True

n, m = map(int, input().split())
edges = []
for i in range(m):
    u, v, w = map(int, input().split())
    edges.append( (w, u-1, v-1, i) )  # Convert to 0-based

edges_sorted = sorted(edges, key=lambda x: x[0])
dsu = DSU(n)
mst_sum = 0
mst_edges = []
in_mst = [False]*m

adj = [[] for _ in range(n)]
for e in edges_sorted:
    w, u, v, idx = e
    if dsu.find(u) != dsu.find(v):
        dsu.union(u, v)
        mst_sum += w
        mst_edges.append( (u, v, w, idx) )
        in_mst[idx] = True
        adj[u].append( (v, w) )
        adj[v].append( (u, w) )

LOG = 20
up = [[-1]*n for _ in range(LOG)]
max_edge = [[0]*n for _ in range(LOG)]
depth = [0]*n

from collections import deque
q = deque()
q.append(0)
up[0][0] = -1
while q:
    u = q.popleft()
    for v, w in adj[u]:
        if up[0][v] == -1 and v != 0:
            up[0][v] = u
            max_edge[0][v] = w
            depth[v] = depth[u] + 1
            q.append(v)

for k in range(1, LOG):
    for v in range(n):
        if up[k-1][v] != -1:
            up[k][v] = up[k-1][up[k-1][v]]
            max_edge[k][v] = max(max_edge[k-1][v], max_edge[k-1][up[k-1][v]])
        else:
            up[k][v] = -1
            max_edge[k][v] = 0

def get_max(u, v):
    if depth[u] < depth[v]:
        u, v = v, u
    res = 0
    for k in range(LOG-1, -1, -1):
        if depth[u] - (1<<k) >= depth[v]:
            res = max(res, max_edge[k][u])
            u = up[k][u]
    if u == v:
        return res
    for k in range(LOG-1, -1, -1):
        if up[k][u] != -1 and up[k][u] != up[k][v]:
            res = max(res, max_edge[k][u], max_edge[k][v])
            u = up[k][u]
            v = up[k][v]
    res = max(res, max_edge[0][u], max_edge[0][v])
    return res

edge_map = {}
for e in edges:
    w, u, v, idx = e
    edge_map[idx] = (u, v, w)

result = [0]*m
for i in range(m):
    if in_mst[i]:
        result[i] = mst_sum
    else:
        u, v, w = edge_map[i]
        max_w = get_max(u, v)
        result[i] = mst_sum - max_w + w

for val in result:
    print(val)