l = [int(i) for i in input().split()]

a = []



for i in range(len(l)):
    if i == 0:
        a.append(-1)
    elif l[i] > l[i-1]:
        if a[i-1] == -1:
            a.append(-1)
        else:
            a.append(a[i-1])
    else:
        a.append(a[i-1])

print(a)