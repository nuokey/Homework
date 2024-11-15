def nsqrt(n):
    if len(str(n)) != 1:
        return nsqrt(sum([int(i) for i in str(n)]))
    return n

def sort(l):
    a = l.copy()
    for i in range(len(l)-1):
        if l[i][1] > l[i+1][1]:
            l = l[:i] + [l[i+1]] + [l[i]] + l[i+2:]
        elif l[i][1] == l[i+1][1]:
            if l[i][0] > l[i+1][0]:
                l = l[:i] + [l[i+1]] + [l[i]] + l[i+2:]

    if l != a:
        return sort(l)
    return l

a = [int(i) for i in input().split()]

l = []


# print(nsqrt(int(input())))

for i in range(len(a)):
    l.append((a[i], nsqrt(a[i])))
s = ""


l = sort(l)

l = [l[i][0] for i in range(len(l))]

print(*l)

