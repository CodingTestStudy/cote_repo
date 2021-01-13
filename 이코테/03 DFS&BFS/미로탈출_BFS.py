from collections import deque

def bfs(x, y):
  queue = deque()
  queue.append((x, y))
  # 큐 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 4가지 방향으로 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if not(0 <= nx < n and 0 <= ny < m):
        continue

      if graph[nx][ny] == 0:
        continue

      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))

  return graph[n-1][m-1]


n, m = map(int, input().split())

graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# 상, 하, 좌, 우 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))

