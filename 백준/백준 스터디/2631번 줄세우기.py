import sys
N = int(sys.stdin.readline().strip())
child = []
for _ in range(N):
    child.append(int(sys.stdin.readline().strip()))

dp = [1] * (N + 1)
for i in range(1, N):
    for j in range(i):
        if child[i] > child[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(N - max(dp))