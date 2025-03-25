# Первая задача
# n, m = map(int, input().split())
# edges = [[] for _ in range(n + 1)]

# for _ in range(m):
#     a, b = map(int, input().split())
#     edges[a].append(b)
#     edges[b].append(a)

# is_ok = True
# color = [0] * (n + 1)

# for start in range(1, n + 1):
#     if color[start] != 0:
#         continue
    
#     queue = [start]
#     color[start] = 1
#     queue_pos = 0 
    
#     while queue_pos < len(queue) and is_ok:
#         current = queue[queue_pos]
#         queue_pos += 1
        
#         for neighbor in edges[current]:
#             if color[neighbor] == 0:
#                 color[neighbor] = 3 - color[current]
#                 queue.append(neighbor)
#             elif color[neighbor] == color[current]:
#                 is_ok = False
#                 break

# if is_ok:
#     print("Yes")
# else:
#     print("No")

# Вторая задача
# size = int(input())
# cost_matrix = [list(map(int, input().split())) for _ in range(size)]

# row_potential = [0] * (size + 1)
# col_potential = [0] * (size + 1)
# assignment = [0] * (size + 1)
# parent = [0] * (size + 1)

# for worker in range(1, size + 1):
#     assignment[0] = worker
#     min_values = [float('inf')] * (size + 1)
#     visited = [False] * (size + 1)
#     current_col = 0

#     while True:
#         visited[current_col] = True
#         current_row = assignment[current_col]
#         delta = float('inf')
#         next_col = 0

#         for col in range(1, size + 1):
#             if not visited[col]:
#                 current_cost = cost_matrix[current_row - 1][col - 1] - row_potential[current_row] - col_potential[col]
#                 if current_cost < min_values[col]:
#                     min_values[col] = current_cost
#                     parent[col] = current_col
#                 if min_values[col] < delta:
#                     delta = min_values[col]
#                     next_col = col

#         for col in range(size + 1):
#             if visited[col]:
#                 row_potential[assignment[col]] += delta
#                 col_potential[col] -= delta
#             else:
#                 min_values[col] -= delta

#         current_col = next_col
#         if assignment[current_col] == 0:
#             break

#     while current_col != 0:
#         prev_col = parent[current_col]
#         assignment[current_col] = assignment[prev_col]
#         current_col = prev_col

# print(-col_potential[0])

'''
Сколько полных паросочетаний содержится в полном графе из 6 вершин?
Есть 15 способов выбрать первую пару
6 способов выбрать вторую из 4 оставшихся
Делим на 3!, т. к. нет разницы в порядке выбора вершин: 15*6/3! = 15
Ответ: 15
'''

# def can_spell_word():
#     word = input().strip()
#     num_cubes = int(input())
#     cubes = [input().strip() for _ in range(num_cubes)]
    
#     if len(word) > num_cubes:
#         return "NO"
    
#     word_letters = {}
#     for char in word:
#         word_letters[char] = word_letters.get(char, 0) + 1
    
#     cube_letters = {}
#     for cube in cubes:
#         for char in set(cube):
#             cube_letters[char] = cube_letters.get(char, 0) + 1
    
#     for char, count in word_letters.items():
#         if cube_letters.get(char, 0) < count:
#             return "NO"
    
#     graph = []
#     for char in word:
#         matching_cubes = []
#         for cube_idx, cube in enumerate(cubes):
#             if char in cube:
#                 matching_cubes.append(cube_idx)
#         graph.append(matching_cubes)
    
#     cube_to_char = [-1] * num_cubes
    
#     def find_match(char_idx, visited):
#         for cube_idx in graph[char_idx]:
#             if not visited[cube_idx]:
#                 visited[cube_idx] = True
#                 if cube_to_char[cube_idx] == -1 or find_match(cube_to_char[cube_idx], visited):
#                     cube_to_char[cube_idx] = char_idx
#                     return True
#         return False
    
#     matched_chars = 0
#     for char_idx in range(len(word)):
#         visited = [False] * num_cubes
#         if find_match(char_idx, visited):
#             matched_chars += 1
    
#     if matched_chars == len(word):
#         result = [0] * len(word)
#         for cube_idx, char_idx in enumerate(cube_to_char):
#             if char_idx != -1:
#                 result[char_idx] = cube_idx + 1
#         return f"YES\n{' '.join(map(str, result))}"
#     else:
#         return "NO"

# print(can_spell_word())

# n = int(input())
# s = input().strip()
# cubes = [input().strip() for _ in range(n)]

# if len(s) > n:
#     print("NO")
# else:
#     letter_count = {}
#     for c in s:
#         if c in letter_count:
#             letter_count[c] += 1
#         else:
#             letter_count[c] = 1

#     available_letters = {}
#     for cube in cubes:
#         unique_chars = {}
#         for c in cube:
#             if c not in unique_chars:
#                 unique_chars[c] = True
#                 if c in available_letters:
#                     available_letters[c] += 1
#                 else:
#                     available_letters[c] = 1

#     possible = True
#     for c, cnt in letter_count.items():
#         if available_letters.get(c, 0) < cnt:
#             possible = False
#             break

#     if not possible:
#         print("NO")
#     else:
#         adjacency = []
#         for i in range(len(s)):
#             target_char = s[i]
#             available_cubes = []
#             for cube_idx in range(n):
#                 if target_char in cubes[cube_idx]:
#                     available_cubes.append(cube_idx)
#             adjacency.append(available_cubes)

#         m = len(s)
#         matching_right = [-1] * n

#         def dfs(u, visited):
#             for v in adjacency[u]:
#                 if not visited[v]:
#                     visited[v] = True
#                     if matching_right[v] == -1 or dfs(matching_right[v], visited):
#                         matching_right[v] = u
#                         return True
#             return False

#         result = 0
#         for u in range(m):
#             visited = [False] * n
#             if dfs(u, visited):
#                 result += 1

#         if result == m:
#             answer = [0] * m
#             for cube_idx in range(n):
#                 if matching_right[cube_idx] != -1:
#                     answer[matching_right[cube_idx]] = cube_idx + 1
#             print("YES")
#             print(' '.join(map(str, answer)))
#         else:
#             print("NO")

def main():
    n = int(input())
    target_word = input().strip()
    cubes = [input().strip() for _ in range(n)]
    
    if len(target_word) > n:
        print("NO")
        return
    
    required_letters = {}
    for char in target_word:
        required_letters[char] = required_letters.get(char, 0) + 1
    
    available_letters = {}
    for cube in cubes:
        unique_cube_letters = set(cube)
        for char in unique_cube_letters:
            available_letters[char] = available_letters.get(char, 0) + 1
    
    for char, count in required_letters.items():
        if available_letters.get(char, 0) < count:
            print("NO")
            return
    
    char_to_cubes = []
    for char in target_word:
        matching_cubes = [i for i, cube in enumerate(cubes) if char in cube]
        char_to_cubes.append(matching_cubes)
    
    cube_assignments = [-1] * n
    
    def find_matching(char_idx, visited_cubes):
        for cube_idx in char_to_cubes[char_idx]:
            if not visited_cubes[cube_idx]:
                visited_cubes[cube_idx] = True
                if cube_assignments[cube_idx] == -1 or find_matching(cube_assignments[cube_idx], visited_cubes):
                    cube_assignments[cube_idx] = char_idx
                    return True
        return False
    
    matched_chars = 0
    for char_idx in range(len(target_word)):
        visited = [False] * n
        if find_matching(char_idx, visited):
            matched_chars += 1
    
    if matched_chars == len(target_word):
        result = [0] * len(target_word)
        for cube_idx, char_idx in enumerate(cube_assignments):
            if char_idx != -1:
                result[char_idx] = cube_idx + 1
        print("YES")
        print(' '.join(map(str, result)))
    else:
        print("NO")

if __name__ == "__main__":
    main()