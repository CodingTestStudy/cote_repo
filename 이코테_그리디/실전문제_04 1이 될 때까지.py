n, k = map(int, input().split())
count = 0
result = 0
x = 0
while n >= k:
  x = n % k    
  count += x  
  n -= x
  n //= k
  count += 1  

if n < k: count += (n - 1)

print(count)
