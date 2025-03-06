INF = 999999999999999999999999999

def floyd_warshall(n, edges):
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0 

    for a, b, weight in edges:
        dist[a][b] = min(dist[a][b], weight)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

def has_negative_cycle(n, dist):
    for i in range(n):
        if dist[i][i] < 0:
            return True
    return False

c = int(input())
for _ in range(c):
    n, m = map(int, input().split())
    edges = []
    for _ in range(m):
        a, b, v = map(int, input().split())
        edges.append((a, b, v))

    
    dist = floyd_warshall(n, edges)

    if has_negative_cycle(n, dist):
        print("Можно")
    else:
        print("Нельзя")