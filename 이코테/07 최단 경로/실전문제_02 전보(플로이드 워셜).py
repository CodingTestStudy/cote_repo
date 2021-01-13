import sys
input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split()) # 도시, 간선, 시작도시
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
  graph[i][i] = 0

for _ in range(m):
  x, y, z = map(int, input().split()) # 특정 도시, 특정 도시, 거리
  graph[x][y] = z


for a in range(1, n + 1):
  for b in range(1, n + 1):
    for k in range(1, n + 1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


count = 0
max_dist = 0
for i in range(1, n + 1):
  if 0 < graph[c][i] < INF:
    count += 1
    max_dist = max(max_dist, graph[c][i])

print(count, max_dist)

