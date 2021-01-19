import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coin = []
idx = 0
for i in range(n):
    x = int(input())
    coin.append(x)
    if x < k: # 4200, 1000
        idx = i # idx가 k원을 만들 때 가장 큰 값의 index

count = 0
for i in range(idx, -1, -1):
    count += k // coin[i]
    k %= coin[i]
    if k == 0:
        break

print(count)


