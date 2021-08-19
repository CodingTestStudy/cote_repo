n, k = map(int, input().split())
cnt = 0

while True:
    target = (n // k) * k
    cnt += n - target
    n = target
    if n < k:
        cnt += n - 1
        break
    n //= k
    cnt += 1

print(cnt)
