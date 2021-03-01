N = int(input()) # 1 <= N <= 1,000
A = list(map(int, input().split()))
dp = [1 for _ in range(N)] # 존재 자체만으로 길이 1
max_value = -1
# 자기자신과 앞의 숫자들을 비교해가면서,
# 본인이 더 큰 경우는 해당 번째의 길이에서 1 증가시킨 값과
# 본인의 길이 중 더 큰 값으로 길이를 갱신해준다.
for i in range(1, N):
    for j in range(i):
        if A[j] < A[i]:
            dp[i] = max(dp[j] + 1, dp[i])
print(max(dp))
