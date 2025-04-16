n, m, p = list(map(int, input().split()))
#n - вершины, m - ребра, p - небезопасные вершины
notsafe = set(map(int, input().split())) #зачем-то повторные небезопасные
safe = list(set(range(1, n + 1)) - set(notsafe))
pos = 1

g = [[0] * (n + 1) for i in range(n + 1)]
for i in range(m):
    b = list(map(int, input().split()))
    g[b[0]][b[1]] = b[2]
    g[b[1]][b[0]] = b[2]
#print(g)

visited = [False] * (n + 1)
inf = 9999999999999999
d = [inf] * (n + 1)
d[safe[0]] = 0
h = 0
for i in range(len(safe)):
    c = inf
    u = -1
    for v in safe:
        if not visited[v] and d[v] < c:
            c = d[v]
            u = v
            #print(u)
    #print(u)
    if u == -1:
        #print("#1")
        pos = -1
        break
    visited[u] = True
    h += c

    for v in safe:
        if not visited[v] and g[u][v] > 0 and g[u][v] < d[v]:
            d[v] = g[u][v]
            #print(v, d[v])
for v in safe:
    if not visited[v]:
        #print("#2")
        pos = -1
        break


h_un = 0
for u in notsafe:
    o = inf
    for v in safe:
        if g[u][v] > 0:
            o = min(o, g[u][v])
    if o == inf:
        #print("#3")
        pos = -1
        break
    h_un += o
if pos == 1:
    print(h + h_un)
else:
    print("impossible")