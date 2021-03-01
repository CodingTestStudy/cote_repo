N = int(input())
A = list(map(int, input().split()))
dp = [0 for _ in range(N)]

dp[0] = A[0]
max_value = dp[0]

# 자기자신과 앞의 숫자들을 비교해가면서,
# 본인이 더 큰 경우는 해당 번째에 축적된 dp 값과
# 본인의 dp의 축적된 값 중 큰 값을 dp 값으로 갱신한다.
# 위 과정을 통해 증가 부분 수열을 찾는 동시에 해당 값들을 축적하여
# dp에 저장된 값들 중 최대값을 찾아서 출력하면 된다.
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += A[i]
    max_value = max(max_value, dp[i])
print(max_value)
