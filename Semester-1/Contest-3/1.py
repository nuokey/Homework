n = int(input().split()[1])

l = map(int, input().split())

l = sorted(l)

print(*l[:n])