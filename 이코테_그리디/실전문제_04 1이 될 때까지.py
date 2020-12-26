n, k = map(int, input().split())
count = 0
x = 0
while n >= k: # n 값이 나누고자하는 k 값보다 작아질 때까지 진행
  x = n % k # n값에서 k로 나누어 떨어지기 위한 값만큼 뺄셈을 해야하는 횟수를 나머지값으로 구한다.
  count += x  
  n -= x  
  n //= k # x값을 뺀 값은 k로 나누어 떨어진다
  count += 1  

if n < k: count += (n - 1)

print(count)
