# 위에서 아래로
# n : 수열 안의 데이터 개수
# 1 <= n <= 500
# 1 <= m <= 100,000
n = int(input())
m = []
for _ in range(n):
  m.append(int(input()))

m.sort(reverse=True)

for i in range(n):
  print(m[i], end=' ')