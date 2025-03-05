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
    # print(n, a[n])
    
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

# print(isUnited(a))


# Второе задание
# def findOne(a, n, e):
#     global visited, found
#     # print(n, a[n])
    
#     for i in range(len(a[n])):
#         if a[n][i] in visited:
#             pass
#         elif a[n][i] == e:
#             found = True
#         else:
#             visited.append(a[n][i])
#             findOne(a, a[n][i], e)
# visited = [0]
# found = False
# findOne(a, 0, 4)
# print(found)

# Четвертое задание
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

isCycled(a, 0, -1)
print(is_cycled)

