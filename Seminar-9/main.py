s = input()

print(s)

l = []

n = "1234567890"

t = -1
for i in range(len(s)):
    print(s[i])
    
    if s[i] in n and t != 0:
        t = 0


