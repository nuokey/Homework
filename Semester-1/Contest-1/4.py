def levenshtein(s1, s2):
    dp = [[0] * (len(s2) + 1) for k in range(len(s1) + 1)]
    for i in range(len(s1) + 1):
        dp[i][0] = i
    for j in range(len(s2) + 1):
        dp[0][j] = j
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,
                           dp[i][j - 1] + 1,
                           dp[i - 1][j - 1] + cost)
    return dp[len(s1)][len(s2)]
def find_ss(a, b, d):
    best_index = -1
    best_length = int()
    for i in range(len(a)):
        for c in range(i + 1, len(a) + 1):
            s = a[i:c]
            distance = levenshtein(s, b)
            if distance <= d:
                if (i < best_index) or (best_index == -1) or (len(s) < best_length):
                    best_index = i
                    best_length = len(s)
    return best_index, best_length
a = input()
b = input()
d = int(input())
index, length = find_ss(a, b, d)
print(index, length)