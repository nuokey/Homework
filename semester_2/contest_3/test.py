n = int(input())
a = input().strip()
b = input().strip()


for i in range(len(a)):
    A = a * 2
    if A[i:i + len(a)] == b and A[i - 1] == '1':
        fl = 1
        print("Random") 
        break
