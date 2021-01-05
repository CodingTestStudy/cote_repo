import heapq
import sys
import time
INF = int(1e9)
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append((b, 1))
  graph[b].append((a, 1))

x, k = map(int, input().split())

start = time.time()
def dijkstra(start):
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start))
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(1)
d1 = distance[k]
dijkstra(k)
d2 = distance[x]
sum_d = d1 + d2
if sum_d >= INF:
  print(-1)
else:
  print(sum_d)

print(time.time() - time.time())
