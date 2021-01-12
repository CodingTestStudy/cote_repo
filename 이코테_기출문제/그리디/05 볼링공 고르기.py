# 볼링공 고르기
# n : 볼링공의 개수 (1 <= n <= 1,000)
# m : 공의 최대 무게 (1 <= m <= 10)
# 각 볼링공의 무게 k (1 <= k <= m)
n, m = map(int, input().split())
k = list(map(int, input().split()))
count = 0
for i in range(len(k) - 1):
  for j in range(i + 1, len(k)):
    if k[i] != k[j]:
      count += 1
    
print(count)