# 미로 탈출
from collections import deque

n, m = map(int, input().split())
graph = []
#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for _ in range(n):
  graph.append(list(map(int, input())))

x = 0
y = 0
graph[x][y] = 1

def bfs(x, y):
  q = deque()
  q.append((x, y))
  while q:
    x, y = q.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if not(0 <= nx < n and 0 <= ny < m):
        continue
      if graph[nx][ny] == 0:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        q.append((nx, ny))


  return graph[n - 1][m - 1]

print(bfs(0, 0))