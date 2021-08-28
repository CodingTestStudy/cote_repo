def solution(n, money):
    dp = [1] + [0] * n
    for mon in money:
        for m in range(mon, n + 1):
            dp[m] += dp[m - mon]
    print(dp)

    return dp[n] % 1000000007


print(solution(5, [1, 2, 5]))
