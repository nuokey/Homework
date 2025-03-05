import sys

a = {
    0:[1],
    1:[0, 2, 5],
    2:[1, 3, 4],
    3:[2],
    4:[2],
    5:[1]
}

b = {
    0:[1],
    1:[2, 4],
    2:[1, 3],
    3:[2, 3],
    4:[1, 3]
}

# Для запуска задания раскомментировать код


# Первое задание
# n, m, s, f = list(map(int, input().split()))
# g = {}
# for i in range(m):
#     b = list(map(int, input().split()))
#     if b[0] not in g:
#         g[b[0]] = {}
#     if b[1] not in g:
#         g[b[1]] = {}
#     g[b[0]][b[1]] = b[2]
#     g[b[1]][b[0]] = b[2]
# print(g)

def all_vertex(graf):
    return list(graf.keys())

def vertex_neighbors(graf, vertex):
    return list(graf[vertex].keys())

def value(graf, vertex1, vertex2):
    return(graf[vertex1][vertex2])

def dijkstra(graf, start, k = 1):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

    max_value = sys.maxsize
    for vertex in unvisited_vertexes:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0

    while unvisited_vertexes:
        current_min_vertex = None
        for vertex in unvisited_vertexes:
            if current_min_vertex == None:
                current_min_vertex = vertex
            elif shortest_path[vertex] < shortest_path[current_min_vertex]:
                current_min_vertex = vertex
        neighbors = vertex_neighbors(graf, current_min_vertex)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_vertex] + value(graf, current_min_vertex, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                k += 1
                previous_vertex[neighbor] = current_min_vertex
        unvisited_vertexes.remove(current_min_vertex)
    return previous_vertex, shortest_path, k

# print(dijkstra(g, s)[2])

# Второе задание
visited = []
is_cycled = False
def isCycled(a, n, last_visited):
    global visited, is_cycled
    for i in range(len(a[n])):
        if a[n][i] in visited:
            if a[n][i] == last_visited:
                pass
            else:
                is_cycled = True
        else:
            visited.append(a[n][i])
            isCycled(a, a[n][i], n)

# isCycled(b, 0, -1)
# print(is_cycled)



# Третье задание
def max_meetings(starts, ends):
    meetings = sorted(zip(starts, ends), key=lambda x: x[1])
    count = 0
    last_end = -1
    for start, end in meetings:
        if start >= last_end:
            count += 1
            last_end = end
    return count

# z = int(input())
# starts = list(map(int, input().split()))
# ends = list(map(int, input().split()))
# print(max_meetings(starts, ends))



# Четвертое задание
from collections import defaultdict
import heapq

def dijkstra(graph, start, end):
    dist = {start: 0}
    heap = [(0, start)]
    while heap:
        current_dist, u = heapq.heappop(heap)
        if u == end:
            return current_dist
        for v, w in graph[u]:
            if v not in dist or dist[v] > current_dist + w:
                dist[v] = current_dist + w
                heapq.heappush(heap, (dist[v], v))
    return -1

# V, E, start, end = input().split()
# V, E = int(V), int(E)
# graph = defaultdict(list)
# for _ in range(E):
#     u, v, w = input().split()
#     w = int(w)
#     graph[u].append((v, w))
#     graph[v].append((u, w))
# print(dijkstra(graph, start, end))



# Пятое задание
from collections import deque, defaultdict

def bfs_distances(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    distances = [-1] * n
    distances[0] = 0
    queue = deque([0])
    
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if distances[v] == -1:
                distances[v] = distances[u] + 1
                queue.append(v)
    return distances

# n, m = map(int, input().split())
# edges = [tuple(map(int, input().split())) for i in range(m)]
# distances = bfs_distances(n, edges)
# for d in distances:
#     print(d)



# Шестое задание
def dfs(graph, visited, u):
    visited[u] = True
    for v in graph[u]:
        if not visited[v]:
            dfs(graph, visited, v)

def count_components(n, edges):
    graph = [[] for _ in range(n)]
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    
    visited = [False] * n
    count = 0
    for i in range(n):
        if not visited[i]:
            dfs(graph, visited, i)
            count += 1
    return count

# n = int(input())
# m = int(input())
# edges = [tuple(map(int, input().split())) for _ in range(m)]
# print(count_components(n, edges))