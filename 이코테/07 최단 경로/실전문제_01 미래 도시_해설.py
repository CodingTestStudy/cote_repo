# 플로이드 워셜 알고리즘 사용
n, m = map(int, input().split())
INF = int(1e9)
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for i in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for i in range(1, n + 1):
  graph[i][i] = 0

x, k = map(int, input().split())

for a in range(1, n + 1):
  for b in range(1, n + 1):
    for c in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][c] + graph[c][b])

d1 = graph[1][k]
d2 = graph[k][x]
d3 = d1 + d2
if d3 >= INF:
  print(-1)
else:
  print(d3)
