n = int(input()) # n kg (3 <= n <= 5000)
INF = int(1e9)
bong = [INF] * 5001
bong[3] = 1
bong[5] = 1
for i in range(3, n + 1):
    bong[i] = min(bong[i], bong[i - 3] + 1)
    bong[i] = min(bong[i], bong[i - 5] + 1)

if bong[n] == INF:
    print(-1)
else:
    print(bong[n])



