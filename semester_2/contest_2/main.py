def find_d(l, d):
    s_d = []
    s = []
    for i in l:
        if i[0] in d or i[1] in d:
            s_d.append(i)
        else:
            s.append(i)

    
    return s, s_d

n, m, p = map(int, input().split())

d = set(map(int, input().split()))

start_s = []
summ = 0

for i in range(m):
    x, y, l = map(int, input().split())
    start_s.append([x, y, l])

start_s = sorted(start_s, key = lambda x: x[2])
s, s_d = find_d(start_s.copy(), d)

final_s = []
groups = []

for i in range(n):
    if i+1 not in d:
        groups.append([i+1])

while len(groups) != 1:
    try:
        x_group = -1
        y_group = -1
        for i in range(len(groups)):
            if s[0][0] in groups[i]:
                x_group = i
            if s[0][1] in groups[i]:
                y_group = i
    except:
        summ = "impossible"

    if x_group != y_group:
        final_s.append(s[0])
        groups[x_group] += groups[y_group]
        groups.pop(y_group)
        s.pop(0)
    else:
        try:
            s.pop(0)
        except:
            summ = "impossible"
            break

for i in d:
    for q in s_d:
        # print(i, q)
        if (q[0] == i or q[1] == i) and q not in final_s:
            if not (q[0] in d and q[1] in d):
                final_s.append(q)
                break

p = []
for i in final_s:
    p.append(i[0])
    p.append(i[1])

p = set(p)
if p != set(range(1, n + 1)):
    summ = "impossible"

if summ != "impossible":
    summ = 0
    for i in final_s:
        summ += i[2]

print(summ)