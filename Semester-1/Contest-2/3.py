A = [int(x) for x in input().split()]
K = []
for i in range(len(A)):
    p = [A[i]]
    for j in range(i + 1, len(A)):
        if A[j] > p[-1]:
            p.append(A[j])
    K.append(len(p)-1)
print(*K)