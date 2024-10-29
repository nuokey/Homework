n = int(input())

def ways(n, out = 0):
    if n - 1 == 0:
        return out
    
    if (n % 3 == 0):
        out += 1
        return ways(n / 3, out)
    
    if ((n - 1) % 3 == 0) and (n % 4 != 0) and ((((n - 1) / 3) % 3 == 0) or (((n - 1) / 3) % 2 == 0)):
        out += 1
        return ways(n - 1, out)
    
    if n % 2 == 0:
        out += 1
        return ways(n / 2, out)
    
    if n - 1 != 0:
        out += 1
        return ways(n - 1, out)
    
print(ways(n))