# 1이 될 때까지
# 2 <= n <= 100,000
# 2 <= k <= 100,000
# n이 1이 될 때까지
# ① n에서 1을 빼거나
# ② n을 k로 나눈다.
# 연산 최소 횟수 출력
n, k = map(int, input().split())
count = 0
while True:  
  if n < k:
    count += (n - 1)
    break
  x = n % k
  n -= x
  count += x
  
  n //= k
  count += 1

print(count)


