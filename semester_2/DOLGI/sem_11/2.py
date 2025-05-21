import heapq
import time

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

def prim_matrix(graph):
    V = len(graph)
    selected = [False] * V
    selected[0] = True
    edges = 0
    total = 0
    
    while edges < V - 1:
        min_edge = float('inf')
        x, y = -1, -1
        for i in range(V):
            if selected[i]:
                for j in range(V):
                    if not selected[j] and graph[i][j] > 0 and graph[i][j] < min_edge:
                        min_edge = graph[i][j]
                        x, y = i, j
        if x == -1:
            return None  # Граф несвязный
        selected[y] = True
        total += min_edge
        edges += 1
    return total

def kruskal(edges, n):
    edges_sorted = sorted(edges, key=lambda x: x[2])
    dsu = DSU(n)
    total = 0
    count = 0
    for u, v, w in edges_sorted:
        if dsu.find(u) != dsu.find(v):
            dsu.union(u, v)
            total += w
            count += 1
            if count == n - 1:
                break
    return total if count == n - 1 else None

# Генерация тестовых данных
import random
def generate_graph(V, density=0.5):
    graph = [[0]*V for _ in range(V)]
    edges = []
    for i in range(V):
        for j in range(i+1, V):
            if random.random() < density:
                w = random.randint(1, 100)
                graph[i][j] = w
                graph[j][i] = w
                edges.append((i, j, w))
    return graph, edges

# Тестирование
for test in range(10):
    V = random.randint(10, 20)
    density = random.uniform(0.3, 0.7)
    graph_matrix, edge_list = generate_graph(V, density)
    
    # Замер времени для Прима
    start = time.perf_counter()
    prim_res = prim_matrix(graph_matrix)
    prim_time = time.perf_counter() - start
    
    # Замер времени для Краскала
    start = time.perf_counter()
    kruskal_res = kruskal(edge_list, V)
    kruskal_time = time.perf_counter() - start
    
    print(f"Test {test+1}: V={V}, edges={len(edge_list)}")
    print(f"Prim: {prim_time:.6f}s, Kruskal: {kruskal_time:.6f}s")
    print(f"Results equal: {prim_res == kruskal_res}\n")

# Определение сложности
print("Сложность алгоритма Прима: O(V^2)")
print("Сложность алгоритма Краскала: O(E log E)")