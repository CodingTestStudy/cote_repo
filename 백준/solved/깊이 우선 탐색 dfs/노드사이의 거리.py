import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    start, end, dist = map(int, input().split())
    graph[start].append((dist, end))
    graph[end].append((dist, start))


def bfs(start, end):
    q = deque()
    q.append((start, 0))
    visited = [False] * (n + 1)
    visited[start] = True
    while q:
        target, distance = q.popleft()
        if target == end:
            return distance
        for d, t in graph[target]:
            if not visited[t]:
                visited[t] = True
                q.append((t, distance + d))


for i in range(m):
    start, end = map(int, input().split())
    print(bfs(start, end))
