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

isCycled(b, 0, -1)
print(is_cycled)