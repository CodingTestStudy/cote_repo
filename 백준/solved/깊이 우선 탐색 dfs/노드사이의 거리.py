import sys
import heapq

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))
    graph[end].append((dist, start))


def dijkstra(start, end):
    distance = [1e9] * (n + 1)
    visited = [False] * (n + 1)
    distance[start] = 0
    q = [[0, start]]
    while q:
        d, s = heapq.heappop(q)
        # 이전에 방문했거나 현재 거리가 이미 저장된 거리보다 크다면 생략
        if visited[s] or d > distance[s]:
            continue
        for dist, target in graph[s]:
            # 이전 거리보다 적다면 갱신
            if distance[target] > d + dist:
                distance[target] = d + dist
                heapq.heappush(q, (distance[target], target))
    return distance[end]


for _ in range(m):
    start, end = map(int, input().split())
    print(dijkstra(start, end))
