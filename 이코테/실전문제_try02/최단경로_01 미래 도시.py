# 미래 도시
# n : 전체 회사 개수 (1 <= n <= 100)
# m : 경로 개수 (1 <= m <= 100)
# x, k : (1 <= x, k <= 100)
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
INF = int(1e9)

graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

x, k = map(int, input().split())
distance = graph[1][k] + graph[k][x]

if distance >= INF:
  print(-1)
else:
  print(distance)