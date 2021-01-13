n, m = map(int, input().split())

result = 0

for i in range(n):
  card = list(map(int, input().split()))
  min_value = 1001
  for x in card:
    min_value = min(x, min_value)
  result = max(result, min_value)

print(result)