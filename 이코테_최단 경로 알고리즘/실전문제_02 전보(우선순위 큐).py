# 우선순위 큐 사용
# 다익스트라 알고리즘
import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)
n, m, c = map(int, input().split()) # 도시 개수, 도로 개수, 시작 도시
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(start):
  distance[start] = 0
  q = []
  heapq.heappush(q, (0, start)) # 거리, 도시
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(c)
count = 0
max_dist = 0
for i in range(1, n + 1):
  if 0 < distance[i] < INF:
    count += 1
    max_dist = max(max_dist, distance[i])

print(count, max_dist)

  
