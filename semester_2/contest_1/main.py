INF = 9999999999

def digit_sum(n):
    s = 0
    n = str(n)
    for i in n:
        s += int(i)
    return s

def graph_build(n):
    g = {}
    for i in range(1, n+1):
        g[i] = []
        if i - 2 >= 1:
            g[i].append(i-2)
        if i * 3 <= n:
            g[i].append(i * 3)
        if i + digit_sum(i) <= n:
            g[i].append(i + digit_sum(i))

    return g

def bfs(graph, n, start, end):
    d = [INF] * (n+1)
    d[start] = 0
    q = []
    q.insert(0, start)
    while len(q) != 0:
        u = q.pop()
        for v in graph[u]:
            if v == end:
                return d[u] + 1
            if d[v] == INF:
                d[v] = d[u] + 1
                q.insert(0, v)
    
    return d[end]

n, m = map(int, input().split())
# print(graph_build(9999)[n])
print(bfs(graph_build(9999), 9999, n, m))