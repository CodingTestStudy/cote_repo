import sys
A = sys.stdin.readline().strip()
B = sys.stdin.readline().strip()

# 각 문자열의 해당 문자까지 검사했을 때의 겹치는 문자열의 최대 길이를 나타내는 dp 리스트
dp = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

# 해당 index에서의 dp값을 갱신하기 위해 이전 index의 dp값을 참고해야하므로,
# 1 ~ len(A, B) + 1 의 범위로 반복문을 사용함
for i in range(1, len(B) + 1):
    for j in range(1, len(A) + 1):
        if B[i - 1] == A[j - 1]: # 겹치는 문자를 발견했을 경우
            dp[i][j] = dp[i - 1][j - 1] + 1
        else: # 겹치지 않은 경우, 이전의 값들 중 큰값으로 갱신
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

# 마지막 문자가 겹치지 않았을지라도 이전의 index값들 중 최대값을 갱신해왔기 때문에
# 마지막 문자를 검사한 결과가 최대값
print(dp[-1][-1])
