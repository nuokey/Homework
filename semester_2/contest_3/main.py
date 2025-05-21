def z_func(string):
    n = len(string)
    zf = [-1] * n
    left, right = 0, 0
    for i in range(1, n):
        zf[i] = max(0, min(right - i, zf[i - left]))
        while i + zf[i] < n and string[zf[i]] == string[i + zf[i]]:
            zf[i] += 1
        if i + zf[i] > right:
            left = i
            right = i + zf[i]
    return zf

n = int(input())

l1 = input()
l2 = input()



print(z_func(l1+"#"+l2))