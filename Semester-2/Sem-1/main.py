a = {
    0:[1],
    1:[0, 2, 5],
    2:[1, 3, 4],
    3:[2],
    4:[2],
    5:[1]
}
# print(a[0])


# Первое задание
def graphTraversal(a, n):
    global visited
    print(n, a[n])
    
    for i in range(len(a[n])):
        if a[n][i] in visited:
            pass
        else:
            visited.append(a[n][i])
            graphTraversal(a, a[n][i])

def isUnited(a):
    global visited
    visited = [0]
    graphTraversal(a, 0)
    if len(visited) == len(a):
        return True
    else:
        return False


print(isUnited(a))