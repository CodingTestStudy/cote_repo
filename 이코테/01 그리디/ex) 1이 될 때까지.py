n, k = map(int, input().split())

result = 0

while True:
  # N이 K로 나누어 떨어지는 수가 될 때까지 빼기
  target = (n // k) * k
  result += n - target
  n = target
  # N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
  if n < k: break
  # K로 다시 나누기
  n //= k
  # 횟수 증가
  result += 1

# 1로 가기 위해
# 마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)