l = [int(i) for i in input().split()]

a = []



for i in range(len(l)):
    if i == 0:
        a.append(-1)
    else:
        m = -1
        for q in range(i):
            if l[q] >= l[i]:
                m = q
        
        if m == -1:
            a.append(-1)
        else:
            a.append(m)

print(*a)