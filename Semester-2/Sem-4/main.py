class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []


    def add_edge(self, s, d, w):
        self.graph.append([s, d, w])


    def matrix_smezh(self, vert):
        A = [[float("Inf")] * vert for i in range(vert)]
        for _ in range(self.V):
            for s, d, w in self.graph:
                A[s][d] = w
                A[s][s] = 0
                A[d][d] = 0
        return(A)


    def print_solution(self, dist):
        for i in range(self.V - 1):
            print(i, 'до этой вершины расстояние', dist[i])

    def bellman_ford(self, src):

        dist = [float("Inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for s, d, w in self.graph:
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w


        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Граф имеет отрицательный цикл")
                return

        self.print_solution(dist)

def floyd(A, V):
    for j in range(V):
        for u in range(V):
            for v in range(V):
                distance = A[u][j] + A[j][v]
                if distance < A[u][v]:
                    A[u][v] = distance
    for i in range(V):
        for j in range(V):
            print(A[i][j], end='  ')
        print()
    return A




l = []

c = int(input())
for i in range(c):
    n, m = map(int, input().split())
    l.append(Graph())
    for q in range(m):
        x, y, t = map(int, input().split())
        l[i].add_edge(x, y, t)

    print(floyd(l[i].matrix_smezh(n), m))
