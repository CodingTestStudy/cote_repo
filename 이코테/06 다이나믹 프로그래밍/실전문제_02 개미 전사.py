# 나의 코드는 i번째 코드를 무조건 포함하는 조건이기 때문에 오답이다.
# ***************** 오답 *****************
# n = int(input())
# k = list(map(int, input().split()))
# d = [0] * 30001
# d[1] = k[1]
# d[2] = k[2]
# for i in range(3, n):
#   d[i] = k[i] + max(d[i - 2], d[i - 3])  
# print(d[n - 1])
# ***************** 오답  *****************

n = int(input())
k = list(map(int, input().split()))

d = [0] * 100
d[0] = k[0]
d[1] = max(k[0], k[1])
# d[i] -> i번째까지 더했을 때, 최대값

for i in range(2, n):
  # 이전까지 더한값과, 현재값과 이전전까지 더한 값중 더 큰값
  d[i] = max(d[i - 1], d[i - 2] + k[i])

print(d[n - 1])  