n = int(input())
d = input().split()
m, l = map(int, input().split())
g = []
for _ in range(m):
    g.append(input().split())

def dfs(i, j, index, word, visited):
    if index == len(word):
        return True
    if i < 0 or i >= m or j < 0 or j >= l:
        return False
    if visited[i][j] or g[i][j] != word[index]:
        return False
    visited[i][j] = True
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1), (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    found = False
    for dx, dy in directions:
        ni, nj = i + dx, j + dy
        if dfs(ni, nj, index + 1, word, visited):
            found = True
            break
    visited[i][j] = False
    return found

result = []
for word in d:
    exist = False
    for i in range(m):
        for j in range(l):
            visited = [[False] * l for _ in range(m)]
            if dfs(i, j, 0, word, visited):
                exist = True
                break
        if exist:
            break
    if exist:
        result.append(word)

print(' '.join(sorted(result)))