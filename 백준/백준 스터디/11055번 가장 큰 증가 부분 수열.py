N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

dp[0] = A[0]
max_value = dp[0]
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += A[i]
    max_value = max(max_value, dp[i])

print(max_value)