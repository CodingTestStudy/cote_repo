# 개미 전사
# n : 식량창고 개수 (3 <= n <= 100)
# k : 각 식량창고의 식량 개수 (0 <= k <= 1,000)
n = int(input())
k = list(map(int, input().split()))
d = [0] * (n + 1)
d[0] = k[0]
d[1] = max(d[0], k[1])
for i in range(2, n):
  d[i] = max(d[i -1], d[i - 2] + k[i])

print(d[n - 1])