# 굳이 배열은 안만들어도 된다!!
n, m = map(int, input().split())
result = 0
for i in range(n):
  card = list(map(int, input().split()))
  data = min(card)
  result = max(data, result)

print(result)