import sys
import heapq

INF = int(1e9)
V, E = map(int, sys.stdin.readline().strip().split())
K = int(sys.stdin.readline().strip())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)

for _ in range(E):
    u, v, w = map(int, sys.stdin.readline().strip().split())
    graph[u].append((v, w))


def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, end = heapq.heappop(q)

        if distance[end] < dist:
            continue

        for i in graph[end]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(K)

for i in range(1, V + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])