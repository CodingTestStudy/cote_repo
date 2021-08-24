N, M = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
dp = [1e9] * 10001
dp[0] = 0
for coin in coins:
    dp[coin] = 1
    for i in range(coin + 1, M + 1):
        if dp[i - coin] != 1e9:
            dp[i] = min(dp[i], dp[i - coin] + 1)
if dp[M] == 1e9:
    print(-1)
else:
    print(dp[M])

