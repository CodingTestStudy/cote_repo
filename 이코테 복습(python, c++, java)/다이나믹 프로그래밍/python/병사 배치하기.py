N = int(input())
data = list(map(int, input().split()))
data.reverse() # 순서를 뒤집어서 최장 증가 부분 수열(LIS) answpfh qusghks

dp = [1] * N

for i in range(1, N):
    for j in range(0, i):
        if data[j]<data[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - max(dp))