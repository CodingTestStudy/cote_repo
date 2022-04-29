import sys

input = sys.stdin.readline
str1 = input().strip()
str2 = input().strip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
result = 0
for r in range(1, len(str1) + 1):
    for c in range(1, len(str2) + 1):
        if str1[r - 1] == str2[c - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
            result = max(result, dp[r][c])
print(result)
