n = int(input())
numbers = list(map(int, input().split()))

total_sum = sum(numbers)

if total_sum % 3 != 0:
    print(0)

else:
    print(1 if (total_sum // 3) >= n else 0)