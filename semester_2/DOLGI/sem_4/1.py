from collections import defaultdict

class Graph:

    def __init__(self, graph):
        self.graph = graph  
        self.ROW = len(graph)  # Количество вершин в графе

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        queue = []
        queue.append(s)
        visited[s] = True
        while queue:
            u = queue.pop(0)
            # Перебираем все смежные вершины
            for ind, val in enumerate(self.graph[u]):
                # Если вершина не посещена и остаточная пропускная способность больше 0
                if visited[ind] == False and val > 0:
                    # Добавляем вершину в очередь и отмечаем как посещённую
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u  # Сохраняем текущую вершину как родительскую
                    # Если достигли стока, возвращаем True
                    if ind == t:
                        return True
        # Если сток не достигнут, возвращаем False
        return False

    def FordFulkerson(self, source, sink):
        # Массив для хранения пути, найденного BFS
        parent = [-1] * (self.ROW)
        max_flow = 0  
        while self.BFS(source, sink, parent):
            # Находим минимальную остаточную пропускную способность на пути
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
            max_flow += path_flow
            # Обновляем остаточные пропускные способности рёбер и обратных рёбер
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow  
                self.graph[v][u] += path_flow  
                v = parent[v]
        return max_flow

n = input()
while n != "0":
    n = int(n)

    graph = []
    for i in range(n):
        graph.append(n*[0])
    # print(graph)
    s, t, c = map(int, input().strip().split())
    for i in range(c):
        u, v, m = map(int, input().strip().split())
        graph[u-1][v-1] = m
        graph[v-1][u-1] = m

    # print(graph)
    g = Graph(graph)
    print("Максимальный возможный поток равен %d" % g.FordFulkerson(s-1, t-1))
    n = input()