n = int(input().split()[1])

# l = input().split()

l = list(map(int, input().split()))


# l = [int(i) for i in input().split()]

a = sorted(l[0:n])
# print(a)

for i in range(n, len(l)):
    
    # print(a, l[i])
    if l[i] < a[-1]:
        a[-1] = l[i]
        a = sorted(a)
        
        

print(*sorted(a))

    