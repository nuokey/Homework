from collections import defaultdict
import sys

class Graph:
    def __init__(self):
        # Initialize the graph using defaultdict to store adjacency lists
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_edge(self, u, v):
        """Add a directed edge from vertex u to vertex v"""
        self.graph[u].append(v)
        self.vertices.add(u)
        self.vertices.add(v)
    
    def transpose(self):
        """Create a transpose graph by reversing all edges"""
        g_transpose = Graph()
        for u in self.graph:
            # For each edge u->v, add edge v->u in transposed graph
            for v in self.graph[u]:
                g_transpose.add_edge(v, u)
        return g_transpose
    
    def dfs_first_pass(self, vertex, visited, finishing_times):
        """First DFS pass to compute finishing times"""
        visited[vertex] = True
        
        # Recursively visit all adjacent vertices
        for adj_vertex in self.graph[vertex]:
            if not visited[adj_vertex]:
                self.dfs_first_pass(adj_vertex, visited, finishing_times)
        
        # Add vertex to finishing_times after exploring all its neighbors
        finishing_times.append(vertex)
    
    def dfs_second_pass(self, vertex, visited, scc):
        """Second DFS pass to find SCCs"""
        visited[vertex] = True
        scc.append(vertex)
        
        # Recursively visit all adjacent vertices
        for adj_vertex in self.graph[vertex]:
            if not visited[adj_vertex]:
                self.dfs_second_pass(adj_vertex, visited, scc)
    
    def find_sccs(self):
        """Main function to find strongly connected components"""
        # Step 1: First DFS pass on original graph
        visited = {vertex: False for vertex in self.vertices}
        finishing_times = []
        
        # Process all vertices in first DFS pass
        for vertex in self.vertices:
            if not visited[vertex]:
                self.dfs_first_pass(vertex, visited, finishing_times)
        
        # Step 2: Create transpose graph
        transposed_graph = self.transpose()
        
        # Step 3: Second DFS pass on transposed graph
        visited = {vertex: False for vertex in self.vertices}
        sccs = []
        
        # Process vertices in order of decreasing finishing time
        for vertex in reversed(finishing_times):
            if not visited[vertex]:
                current_scc = []
                transposed_graph.dfs_second_pass(vertex, visited, current_scc)
                sccs.append(current_scc)
        
        return sccs
    


# Пример
def example_usage():
    g = Graph()
    
    # Add edges to create a graph with multiple SCCs
    edges = [(1, 2), (2, 3), (3, 1),  # First SCC: 1-2-3
            (4, 5), (5, 6), (6, 4),  # Second SCC: 4-5-6
            (3, 4), (5, 7)]          # Additional edges
    
    for u, v in edges:
        g.add_edge(u, v)
    
    sccs = g.find_sccs()
    
    print("Strongly Connected Components:")
    for i, scc in enumerate(sccs, 1):
        print(f"SCC {i}: {scc}")



# print(find_social_clusters(10, [(0, 1), (1, 2), (2, 0), (3, 1), (3, 4), (4, 3), (4, 5), (5, 6), (6, 7), (7, 8), (8, 5)]))

def create_chessboard(n):
    edges = []
    for y in range(n):
        for x in range(n):
            if y - 2 >= 0 and x - 1 >= 0:
                edges.append((y * n + x, (y-2) * n + (x-1)))
            if y - 1 >= 0 and x - 2 >= 0:
                edges.append((y * n + x, (y-1) * n + (x-2)))
            if y - 2 >= 0 and x + 1 < n:
                edges.append((y * n + x, (y-2) * n + (x+1)))
            if y - 1 >= 0 and x + 2 < n:
                edges.append((y * n + x, (y-1) * n + (x+2)))
            if y + 2 < n and x + 1 < n:
                edges.append((y * n + x, (y+2) * n + (x+1)))
            if y + 1 < n and x + 2 < n:
                edges.append((y * n + x, (y+1) * n + (x+2)))
            if y + 2 < n and x - 1 >= 0:
                edges.append((y * n + x, (y+2) * n + (x-1)))
            if y + 1 < n and x - 2 >= 0:
                edges.append((y * n + x, (y+1) * n + (x-2)))

    return edges

# print(create_chessboard(3))


def all_vertex(graf):
    return list(graf.keys())

#возвращаем не менее красивым списочком всех соседей данной вершины
def vertex_neighbors(graf, vertex):
    return list(graf[vertex].keys())

#возвращаем длину ребра между двумя вершинами
def value(graf, vertex1, vertex2):
    return(graf[vertex1][vertex2])

def dijkstra(graf, start):
    unvisited_vertexes = all_vertex(graf)
    shortest_path = {}
    previous_vertex = {}

#по умолчанию расстояния между любыми двумя вершинами задаем равным бесконечности,
# а затем в цикле while переопределяем на минимально возможное 
    max_value = sys.maxsize
    for vertex in unvisited_vertexes:
        shortest_path[vertex] = max_value
    shortest_path[start] = 0

    while unvisited_vertexes:
        #ищем вершину с меньшей оценкой
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
                previous_vertex[neighbor] = current_min_vertex
        unvisited_vertexes.remove(current_min_vertex)
    return previous_vertex, shortest_path



def find_social_clusters(n, edges):
    g = Graph()
    for u, v in edges:
        g.add_edge(u, v)

    sccs = g.find_sccs()
    sccs = sorted(sccs)

    for i in range(len(sccs)):
        sccs[i] = sorted(sccs[i])

    for i in range(len(sccs)-1):
        for j in range(len(sccs)-1-i):
            if len(sccs[j]) < len(sccs[j+1]):
                sccs[j], sccs[j+1] = sccs[j+1], sccs[j]

    return sccs

def dijkstra_chess(n, s):
    g = Graph()
    # print(n)
    edges = create_chessboard(n)
    for u, v in edges:
            g.add_edge(u, v)
    graph = {}

    for i in g.graph:
        graph[i] = {}
        for q in g.graph[i]:
            graph[i][q] = 1

    return dijkstra(graph, s)[1]

def chess(n):
    for y in range(n):
        for x in range(n):
            print(dijkstra_chess(n, y*n + x))

chess(6)