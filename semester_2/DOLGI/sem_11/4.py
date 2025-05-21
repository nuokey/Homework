import heapq

n, m, *centers = map(int, input().split())
roads = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    roads[u].append( (v, w) )
    roads[v].append( (u, w) )

INF = float('inf')
dist = [INF] * n
heap = []
for c in centers:
    dist[c] = 0
    heapq.heappush(heap, (0, c))

while heap:
    current_dist, u = heapq.heappop(heap)
    if current_dist > dist[u]:
        continue
    for v, w in roads[u]:
        if dist[v] > dist[u] + w:
            dist[v] = dist[u] + w
            heapq.heappush(heap, (dist[v], v))

total = sum(d for d in dist if d != INF)
print(total)