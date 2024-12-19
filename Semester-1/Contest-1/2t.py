n = int(input("Введите число n: "))

def ways(n, count=0):
    if n == 1:
        return count

    if n % 3 == 0:
        return ways(n // 3, count + 1)

    if (n - 1) % 3 == 0 and n % 4 != 0 and ((n - 1) // 3 % 3 == 0 or (n - 1) // 3 % 2 == 0):
        return ways(n - 1, count + 1)

    if n % 2 == 0:
        return ways(n // 2, count + 1)

    return ways(n - 1, count + 1)

print(ways(n))