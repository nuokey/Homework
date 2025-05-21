t = int(input())
n = int(input())
graph = [[0] * (n + 1) for _ in range(n + 1)]
cards = [False] * (n + 1) 
for i in range(1, n):
    cards[int(input())] = True 
e = int(input())
for i in range(e):
    d = list(map(int, input().split()))
    graph[d[0]][d[1]] = True
    graph[d[1]][d[0]] = True

class Graph:

    def init(self, graph):
        self.graph = graph  
        self.ROW = len(graph)  # Количество вершин в графе

    def BFS(self, s, t, parent):
        visited = [False] * (self.ROW)
        cards = [False] * (n + 1) 
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
            path_flow = float("inf")
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
    
    
class Edge:
    def init(self, to, rev, capacity, cost):
        self.to = to
        self.rev = rev
        self.capacity = capacity
        self.cost = cost

class MinCostFlow:
    def init(self, N):
        self.N = N
        self.graph = [[] for _ in range(N)]
    
    def add_edge(self, fr, to, capacity, cost):
        forward = Edge(to, len(self.graph[to]), capacity, cost)
        backward = Edge(fr, len(self.graph[fr]), 0, -cost)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)
    
    def flow(self, s, t, maxf):
        N = self.N
        res = 0
        h = [0] * N
        prevv = [0] * N
        preve = [0] * N
        inf = 999999999999
        while maxf > 0:
            dist = [inf] * N
            inqueue = [False] * N
            dist[s] = 0
            q = []
            q.append(s)
            inqueue[s] = True
            while q:
                v = q.pop(0)
                inqueue[v] = False
                for i, e in enumerate(self.graph[v]):
                    if e.capacity > 0 and dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]:
                        dist[e.to] = dist[v] + e.cost + h[v] - h[e.to]
                        prevv[e.to] = v
                        preve[e.to] = i
                        if not inqueue[e.to]:
                            q.append(e.to)
                            inqueue[e.to] = True
            if dist[t] == inf:
                return -1
            for v in range(N):
                if dist[v] < inf:
                    h[v] += dist[v]
            d = maxf
            v = t
            while v != s:
                d = min(d, self.graph[prevv[v]][preve[v]].capacity)
                v = prevv[v]
            maxf -= d
            res += d * h[t]
            v = t
            while v != s:
                e = self.graph[prevv[v]][preve[v]]
                e.capacity -= d
                self.graph[v][e.rev].capacity += d
                v = prevv[v]
        return res

# Чтение входных данных
lines = []
while True:
    try:
        line = input().strip()
        if line:
            lines.append(line)
    except EOFError:
        break

ptr = 0
t = int(lines[ptr]) if ptr < len(lines) else 0
ptr += 1
for _ in range(t):
    if ptr >= len(lines):
        break
    n = int(lines[ptr])
    ptr += 1
    count = [0] * (n + 1)
    for _ in range(n):
        if ptr >= len(lines):
            card = 0
        else:
            card = int(lines[ptr])
        ptr += 1
        if 1 <= card <= n:
            count[card] += 1
    if ptr >= len(lines):
        e = 0
    else:
        e = int(lines[ptr])
    ptr += 1
    exchange_graph = [[] for _ in range(n + 1)]
    for _ in range(e):
        if ptr >= len(lines):
            x, y = 0, 0
        else:
            x, y = map(int, lines[ptr].split())
        ptr += 1
        exchange_graph[x].append(y)
        exchange_graph[y].append(x)
    
    excess = []
    deficit = []
    for i in range(1, n + 1):
        cnt = count[i]
        if cnt > 1:
            excess.append((i, cnt - 1))
        elif cnt < 1:
            deficit.append((i, 1 - cnt))
    
    dist = [[-1] * (n + 1) for _ in range(n + 1)]
    for start in range(1, n + 1):
        q = []
        q.append(start)
        dist[start][start] = 0
        while q:
            u = q.pop(0)
            for v in exchange_graph[u]:
                if dist[start][v] == -1:
                    dist[start][v] = dist[start][u] + 1
                    q.append(v)
    
    size = n + 2
    mcf = MinCostFlow(size)
    sum_excess = sum(cap for (_, cap) in excess)
    sum_deficit = sum(cap for (_, cap) in deficit)
    if sum_excess != sum_deficit:
        print(-1)
        continue
    
    for (card, cap) in excess:
        mcf.add_edge(0, card, cap, 0)
    for (card, cap) in deficit:
        mcf.add_edge(card, size - 1, cap, 0)
    
    inf = 10**18
    for (i, _) in excess:
        for (j, _) in deficit:
            if dist[i][j] != -1:
                mcf.add_edge(i, j, inf, dist[i][j])
    
    min_cost = mcf.flow(0, size - 1, sum_excess)
    print(min_cost)