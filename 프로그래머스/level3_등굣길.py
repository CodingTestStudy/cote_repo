def solution(m, n, puddles):
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    dp[1][1] = 1  # 출발지점
    for r in range(1, n + 1):
        for c in range(1, m + 1):
            if r == 1 and c == 1:  # 출발지점
                continue
            if [c, r] in puddles: # 웅덩이면, 문제에서 m(열),n(행) 순으로 했기 때문
                dp[r][c] = 0
            else:
                dp[r][c] = dp[r - 1][c] + dp[r][c - 1]
    return dp[n][m] % 1000000007


print(solution(4, 3, [[2, 2]]))
