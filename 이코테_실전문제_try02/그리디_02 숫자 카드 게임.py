# 숫자 카드 게임
# 1 <= n, m <= 100
n, m = map(int, input().split())
result = 0
for _ in range(n):
  input_data = list(map(int, input().split()))
  min_data = min(input_data)
  result = max(result, min_data)

print(result)