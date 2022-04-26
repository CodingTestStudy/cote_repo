import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
graph = [[] * (n + 1)  for _ in range(n + 1)]
while True:
    x, y = map(int, input().split())
    if x == -1 and y == -1:
        break
    graph[x].append(y)
    graph[y].append(x)


def bfs(i):
    # 출발지점 i
    visited = [-1] * (n + 1)
    visited[i] = 0
    q = deque([i])
    while q:
        target = q.popleft()
        for v in graph[target]:
            if visited[v] == -1:
                visited[v] = visited[target] + 1
                q.append(v)
    return max(visited)


score = 1e9
candidate = []

for i in range(1, n + 1):
    temp = bfs(i)
    if temp < score:
        score = temp
        candidate = [i]
    elif temp == score:
        candidate.append(i)
print(score, len(candidate))
print(*candidate)
