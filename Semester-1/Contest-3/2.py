inp = input().split()
n = int(inp[1])

# l = map(int, input().split())
l = [int(i) for i in input().split()]
# print(l)

c = l[:n]
# print(c)
l = l[n:]

t = 0

while sum(c) != 0 or len(l) != 0:
    # print(c)
    for i in range(len(c)):
        
        if c[i] == 0 and len(l) != 0:
            c[i] = l[0]
            l = l[1:]
            c[i] -= 1
        elif c[i] == 0 and len(l) == 0:
            pass
        else:
            c[i] -= 1
            
        # print(c[i])
        
            
        
    t += 1

print(t)