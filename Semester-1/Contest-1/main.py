import sys
# sys.setrecursionlimit = 100000000

n = int(input())

s = []

def minilen(n, l):
    if n == 1:
        return l
    elif n < 1 or int(n) != n:
        return None
    else:
        b = l
        b.append(n)
        return [minilen(n-1, b), minilen(n/2, b), minilen(n/3, b)]
    
print(minilen(n, []))