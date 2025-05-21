l = [[0, -1, {}]]
last, size = 0, 1
for c in input():
    l.append([0, -1, {}])
    cur, n = last, size
    size += 1
    l[n][0] = l[last][0] + 1
    a = last
    while c not in l[a][2] and a != -1:
        l[a][2][c] = n
        a = l[a][1]

    if a == -1:
        l[n][1] = 0
    else:
        q = l[a][2][c]
        if l[a][0] + 1 != l[q][0]:
            cl = size
            l.append([0, -1, {}])
            l[cl][0] = l[a][0] + 1
            l[cl][1] = l[q][1]
            l[cl][2] = l[q][2].copy()
            size += 1
            while a != -1 and l[a][2][c] == q:
                l[a][2][c] = cl
                a = l[a][1]
            l[q][1] = cl
            l[n][1] = cl
        else:
            l[n][1] = q
    last = n

summ = 0
for s in l[1:]:
    summ += s[0] - l[s[1]][0]
print(summ)