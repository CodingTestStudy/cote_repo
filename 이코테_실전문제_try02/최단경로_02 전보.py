# 전보
# n : 도시의 개수 (1 <= n <= 30,000)
# m : 통로의 개수 (1 <= m <= 200,000)
# c : 출발 도시 (1 <= c <= n)
# x -> y z시간 소요 (1 <= x, y <= n) (1 <= z <= 1,000)
import sys, heapq
input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
  x, y, z = map(int, input().split())
  graph[x].append((y, z))

def dijkstra(graph, start):
  q = []  # 우선순위 큐
  heapq.heappush(q, (0, start))
  distance[start] = 0
  while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
      continue
    
    for i in graph[now]:
      cost = dist + i[1]
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(graph, c)
count = -1
max_time = 0
for i in range(1, n + 1):
  if distance[i] != INF:
    count +=  1
    max_time = max(max_time, distance[i])

print(count, max_time)
